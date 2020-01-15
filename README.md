# Building Containerized Applications on AWS Demos

This repository exists to allow you to recreate demos from the Building Containerized Applications on AWS course, found here: <a href="https://www.edx.org/course/building-containerized-applications-on-aws"> Building Containerized Applications on AWS </a>

The repository includes two versions of a simple python "blog" app. The first version of the app is all static content and can be found under the path <code> aws-demos/building-containerized-applications-on-aws/pythonwebapp/docker-python-webapp-static/ </code> 

The second version of the app is backed by a dynamodb table and can be found under the path <code> aws-demos/building-containerized-applications-on-aws/pythonwebapp/docker-python-webapp-dynamo/ </code>. In order for this code to work in your own account, you'll need to create a DynamoDB table called <code> blogs </code> as well as create an IAM Role that allows the code running in the container to use Role Based Access to read the DynamoDB table.

