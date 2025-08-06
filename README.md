https://docs.python-requests.org/en/latest/user/advanced/

To specify the AWS Region when running your Python script on the AWS Production server, you can use one of the following methods:

Set the AWS_DEFAULT_REGION environment variable: [1] Before running your Python script, set the AWS_DEFAULT_REGION environment variable to the desired AWS Region. For example:
export AWS_DEFAULT_REGION=us-east-1 python your_script.py

Use the region parameter when creating the Textract client: [2] In your Python script, when creating the Textract client, specify the region parameter:
import boto3 textract = boto3.client('textract', region_name='us-east-1')

Configure the default region in the AWS CLI: [3] If you have the AWS CLI installed on the AWS Production server, you can configure the default Region by running the following command:
aws configure set default.region us-east-1

After setting the Region using one of these methods, your Python script should be able to invoke the Textract start Document analysis operation on the AWS Production server.

python -m pip install awscli

 WARNING: The scripts pyrsa-decrypt.exe, pyrsa-encrypt.exe, pyrsa-keygen.exe, pyrsa-priv2pub.exe, pyrsa-sign.exe and pyrsa-verify.exe are installed in 'C:\Users\Developer\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script docutils.exe is installed in 'C:\Users\Developer\AppData\Roaming\Python\Python39\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed PyYAML-6.0.2 awscli-1.42.3 botocore-1.40.3 colorama-0.4.6 docutils-0.19 pyasn1-0.6.1 rsa-4.7.2
WARNING: You are using pip version 21.1.1; however, version 25.2 is available.
You should consider upgrading via the 'C:\Program Files\Python39\python.exe -m pip install --upgrade pip' command.

set PATH=%PATH%;C:\Users\Developer\AppData\Roaming\Python\Python39\Scripts

