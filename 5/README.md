# CloudWatch Dashboard for EC2 CPU Utilization

This CloudFormation template deploys a CloudWatch dashboard that displays the CPU utilization of an EC2 instance. The dashboard shows the average CPU utilization over a period of 5 minutes.

## Usage

To use this template, provide the ID of the EC2 instance to monitor as the `InstanceId` parameter. The template will create a CloudWatch dashboard with the name "EC2-CPU-Utilization" that displays the CPU utilization of the specified instance.

## CloudFormation Resources

This template creates a single CloudWatch dashboard resource named "Dashboard". The resource type is "AWS::CloudWatch::Dashboard". The `DashboardBody` property is a JSON object that specifies the layout and content of the dashboard.
