import boto3
import datetime

# Replace 'BUCKET-NAME' with the name of your S3 bucket
bucket_name = 'my-unique-bucket-2023-02-16'

# Create a backup filename with the current date and time
current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
backup_filename = f'{bucket_name}-backup-{current_time}.tar.gz'

# Create a new S3 client using Boto3
s3 = boto3.client('s3')

# Create a list of all objects in the bucket
objects = s3.list_objects(Bucket=bucket_name)

# Create a list of object keys to download
object_keys = [obj['Key'] for obj in objects.get('Contents')]

# Download each object and write it to a file
with open(backup_filename, 'wb') as backup_file:
    for key in object_keys:
        object_data = s3.get_object(Bucket=bucket_name, Key=key)['Body'].read()
        backup_file.write(object_data)

print(f'Successfully backed up {len(object_keys)} objects to {backup_filename}')
