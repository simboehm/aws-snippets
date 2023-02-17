import boto3
import os


# Create an EC2 client using boto3 (option 1)
ec2_client = boto3.client("ec2")

# Create an EC2 resource using boto3 (option 2)
ec2_resource = boto3.resource("ec2")

# Call the describe_instances method on the client object to get information
# about all instances in the account. The response object contains a dictionary
# with information about the instances, including their tags and instance types.
response = ec2_client.describe_instances()

# Loop through the reservations and instances to print the instance ID and AMI ID (option1)
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        ami_id = instance["ImageId"]
        print(f"Instance ID: {instance_id}")
        print(f"AMI ID: {ami_id}")

# Print some separator lines for readability
separator = os.linesep + "-" * 30 + os.linesep
print(separator)

# Loop through all instances in the EC2 resource and print their name and type (option 2)
for instance in ec2_resource.instances.all():
    print(f"Instance name: {instance.tags[0]['Value']}")
    print(f"Instance type: {instance.instance_type}")
