# Python script to retrieve and print information about AWS EC2 instances using boto3

This Python script uses the boto3 library to interact with the Amazon Web Services (AWS) EC2 service.

The script creates an EC2 client and resource objects using boto3, and then calls the describe_instances method to get 
information about all instances in the account. The response object contains a dictionary with information about the instances, 
including their tags and instance types. The script then loops through the reservations and instances to print the instance ID and AMI ID.

To run this script, you will need to set up your AWS credentials using the aws configure command to provide your access key ID and secret access key. 
This will allow the script to access your AWS account. Once your credentials are configured, you can run this script locally in your Python environment.

Note: Please note that the script's dependencies are listed in the requirements.txt file. Before running the script, please ensure that you have installed all dependencies, including AWS SDK for Python, using the following command: pip install -r requirements.txt. This will ensure that the script can run successfully without any missing dependencies.
