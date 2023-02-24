# S3 Backup Script

This Python script uses the Boto3 library to backup all objects in an AWS S3 bucket to a local `.tar.gz` file. The backup file is named with the format `{bucket-name}-backup-{timestamp}.tar.gz`.

## Requirements

- Python 3.x
- Boto3 library

## Usage

1. Clone the repository or download the script directly.
2. Install the Boto3 library by running `pip install boto3` in your terminal.
3. Replace `BUCKET-NAME` with the name of the S3 bucket you want to backup in the script.
4. Run the script by running `python s3_backup.py` in your terminal.
5. The script will create a backup file in the same directory where the script is located.

## Note

- This script downloads all objects in the specified S3 bucket to a local file. If your bucket contains a large amount of data, this may take some time and consume a significant amount of disk space.
- This script does not provide a fully-automated backup solution. For more advanced backup scenarios, consider using AWS's built-in S3 Backup service, or consult the AWS documentation to create a customized backup solution.
