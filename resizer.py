import os
from PIL import Image
import boto3
from time import time

THUMB_SIZE = int(os.getenv("THUMB_SIZE"))
DEST_BUCKET = os.getenv('DEST_BUCKET_NAME')
size = (THUMB_SIZE, THUMB_SIZE)
s3 = boto3.client('s3')

def lambda_handler(event, context):
    image = event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']

    thumb_name = "thumbnail_{time}_{image}".format(time=str(int(time())), image=image)
    try:
        with open('/tmp/'+image, 'wb') as data:
            s3.download_fileobj(bucket_name, image, data)
        im = Image.open('/tmp/'+image)
        im.thumbnail(size)
        im.save('/tmp/'+thumb_name, 'JPEG')
        s3.put_object(ACL='public-read',Body=open('/tmp/'+thumb_name, 'rb'), Bucket=DEST_BUCKET, Key=thumb_name)
        print(thumb_name)
    except IOError:
        print("Cannot create thumbnail for "+image)
