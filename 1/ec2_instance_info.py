import boto3
import os

# Add a separator to distinguish the client and resource sections of the output
separator = os.linesep + "-" * 30 + os.linesep

# Create an EC2 client using boto3
ec2_client = boto3.client("ec2")

# Use the describe_instances method to retrieve a list of running instances
# Filter instances by their state and retrieve their IDs and types
response = ec2_client.describe_instances(Filters=[{"Name": "instance-state-name", "Values": ["running"]}])
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"Instance Type: {instance['InstanceType']}")
        print(separator)

# Create an EC2 resource using boto3
ec2_resource = boto3.resource("ec2")

# Use the instances.filter method to retrieve a list of running instances
# Filter instances by their state and retrieve various attributes such as ID, type, AMI ID, etc.
instances = ec2_resource.instances.filter(Filters=[{"Name": "instance-state-name", "Values": ["running"]}])
for instance in instances:
    print(f"Instance ID: {instance.id}")
    print(f"Instance type: {instance.instance_type}")
    print(f"AMI ID: {instance.image_id}")
    print(f"Key name: {instance.key_name}")
    # Retrieve security group names by iterating over the security groups attribute
    print(f"Security groups: {[sg['GroupName'] for sg in instance.security_groups]}")
    print(f"Private IP address: {instance.private_ip_address}")
    print(f"Public IP address: {instance.public_ip_address}")
    print(f"Subnet ID: {instance.subnet_id}")
    print(f"VPC ID: {instance.vpc_id}")
    print(f"State: {instance.state['Name']}")
    print(f"Launch time: {instance.launch_time}")
    print(f"Tags: {instance.tags}")
    print(separator)
