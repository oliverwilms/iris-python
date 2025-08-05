https://docs.python-requests.org/en/latest/user/advanced/

To specify the AWS Region when running your Python script on the AWS Production server, you can use one of the following methods:

Set the AWS_DEFAULT_REGION environment variable: [1] Before running your Python script, set the AWS_DEFAULT_REGION environment variable to the desired AWS Region. For example:
export AWS_DEFAULT_REGION=us-east-1 python your_script.py

Use the region parameter when creating the Textract client: [2] In your Python script, when creating the Textract client, specify the region parameter:
import boto3 textract = boto3.client('textract', region_name='us-east-1')

Configure the default region in the AWS CLI: [3] If you have the AWS CLI installed on the AWS Production server, you can configure the default Region by running the following command:
aws configure set default.region us-east-1

After setting the Region using one of these methods, your Python script should be able to invoke the Textract start Document analysis operation on the AWS Production server.
