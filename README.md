# Lambda Thumbnailer

This is a Lambda function that creates a thumbnail when a JPG image is put on a S3 bucket and save it in another bucket.

## Quick start

- Install **Zappa** and the **aws cli** command
- Add the source and destination bucket name to the _parameters.json_ file.
- Create the CloudFormation stack by using the _sam_resizer.yml_ template with the _parameters.json_ file input.
- Customize the _zappa_settings.yml_ file by initializing the DEST_BUCKET_NAME environment with the name of the destination bucket
- Execute Zappa with the command `zappa deploy`.

## Configuration

You can configure:

- **DEST_BUCKET_NAME**: the name of S3 bucket where the thumbnail will be saved.
- **THUMB_SIZE**: the thumbnail size.