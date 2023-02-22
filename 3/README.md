## EC2 Instance CloudFormation Template

This is a simple CloudFormation template for creating an EC2 instance with the following properties:
- Instance type: t2.micro
- Amazon Machine Image (AMI) ID: ami-0b5eea76982371e91
- Key pair name: my_ec2_key_pair
- IAM instance profile with permissions to access S3
- A user data script that installs and starts the Apache HTTP server and copies an index.html file from an S3 bucket to the instance's web server directory.

### Resources
- `EC2Instance`: Creates the EC2 instance with the specified instance type, AMI ID, key pair, IAM instance profile, and user data script.
- `EC2InstanceProfile`: Creates an IAM instance profile with permissions to access S3 and associates it with the EC2 instance.
- `EC2Role`: Creates an IAM role with permissions to assume the role, and attaches the Amazon S3 ReadOnly access managed policy.

Note: Replace `my-unique-bucket-2023-02-16` in the `UserData` section with the name of your S3 bucket and the correct file path.
