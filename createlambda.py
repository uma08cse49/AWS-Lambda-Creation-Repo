# import boto3
# import os

# client = boto3.client('lambda')

# access_key=os.getenv("ACCESS_KEY_ID")
# secret_access_key=os.getenv("SECRET_ACCESS_KEY_ID")
# region=os.getenv("REGION")

# response = client.create_function(
#     FunctionName='test_pgm_lambda',
#     Runtime='python3.9',
#     Role='arn:aws:iam::898400654322:role/lambda-admin',
#     Handler='index.handler',
#     Code={
#         'ZipFile': open('index.py', 'rb').read()
#         # 'ZipFile': b'C:\Users\Sandeza\Desktop\serviceNow\index.zip'
#         # 'ZipFile': b'bytes',
#         # 'S3Bucket': 'string',
#         # 'S3Key': 'string',
#         # 'S3ObjectVersion': 'string'
#     },
# )
# print('Lambda function created:', response['FunctionArn'])

# ============================================================================================================================

import boto3
import logging
import sys

def lambda_build():
    client = boto3.client('lambda')

    create_lambda_function = client.create_function(
    FunctionName='testLambda',
    Runtime='python3.9',
    Role='arn:aws:iam::898400654322:role/lambda-admin',
    Handler='{}.lambda_handler'.format('lambda_build'),
    Description='Start a virtual machine',
    Code = {'S3Bucket':'testpgmlambda', 'S3Key':'index.zip'}
)

lambda_build()