# EC2 Instance Info

This Python script provides information about running EC2 instances in your AWS account. It uses the Boto3 library to interact with the AWS API and prints out details about each running instance.

## Requirements

- Python 3
- Boto3 library (`pip install boto3`)

## Usage

1. Configure your AWS credentials using one of the methods described in the [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration).
2. Run the script using `python ec2_instance_info.py`.
3. The script will output information about each running EC2 instance in your account, including instance ID, instance type, AMI ID, key name, security groups, IP addresses, subnet ID, VPC ID, instance state, launch time, and tags.

Note: This script only provides information about running instances. If you want to retrieve information about instances in other states (such as stopped or terminated), you will need to modify the Filters argument in the `describe_instances` and `instances.filter` functions.
