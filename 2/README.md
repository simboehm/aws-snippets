# Simple EC2 Instance CloudFormation Template

This is a simple AWS CloudFormation template to deploy an EC2 instance. The template includes the following resources:

- EC2Instance: An EC2 instance running on the specified instance type, with the specified AMI and key pair, security group, and user data to launch a simple website.

## Parameters

The following parameters are available to customize the EC2 instance:

- `InstanceType`: The EC2 instance type to use (default: t2.micro).
- `ImageId`: The Amazon Machine Image (AMI) ID to use (default: ami-0b5eea76982371e91).
- `KeyName`: The name of the key pair to use for SSH access to the instance.
- `WebsiteContent`: The content to display on the website running on the instance (default: simple HTML page).

## Usage

The security group must allow incoming traffic on port 80. 

To use this CloudFormation template:

1. Upload the template to an S3 bucket or copy and paste it into the CloudFormation console.
2. Specify the desired parameter values, such as `InstanceType` and `WebsiteContent`.
3. Launch the stack. 

Once the stack is launched, you should have a running EC2 instance with the specified parameters.
