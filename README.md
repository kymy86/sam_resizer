# Lambda Thumbnailer

This is a Lambda function that create a thumbnail when a JPG image is put on a S3 bucket.

## Quick start

- Install **Zappa** and the **aws cli** command
- Add the source and destination bucket name to the _parameters.json_ file.
- Create the CloudFormation stack by using the _sam_resizer.yml_ template with the _parameters.json_ file input.
- Customize the _zappa_settings.yml_ file by initializing the DEST_BUCKET_NAME environment with the name of the destination bucket
- Execute Zappa with the command `zappa deploy`.