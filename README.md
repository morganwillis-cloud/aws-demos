# Building Containerized Applications on AWS Demos

This repository exists to allow you to recreate demos from the Building Containerized Applications on AWS course, found here: <a href="https://www.edx.org/course/building-containerized-applications-on-aws"> Building Containerized Applications on AWS </a>

## PLEASE NOTE: 

These demos were not built with free tier usage in mind, and therefore if you run them in your personal account you may or may not encounter charges. Build these proof of concepts in your account at your own risk.

These demos are not built to adhere to security standards and are purely a proof of concept. These are not to be used in production or sensitive environments. These demos WILL create public resources in your account if you choose to use them.

It is also worth noting that these demos were built on top of existing resources that you would need to create in your own account. These existing resources include:

  - A VPC
  - An Internet Gateway attached to that VPC
  - Two public subnets across two AZs
  - Routes allowing all internet traffic to flow from the subnets to the internet gateway
  - A security group for a public facing ALB allowing all http traffic on port 80
  - A security group for your containers allowing all http traffic on port 8080
  - A Cloud9 Instance
  - A DynamoDB Table named <code> blogs </code>
  


The repository includes two versions of a simple python "blog" app. The first version of the app is all static content and can be found under the path <code> aws-demos/building-containerized-applications-on-aws/pythonwebapp/docker-python-webapp-static/ </code> 

The second version of the app is backed by a dynamodb table and can be found under the path <code> aws-demos/building-containerized-applications-on-aws/pythonwebapp/docker-python-webapp-dynamo/ </code>. In order for this code to work in your own account, you'll need to create a DynamoDB table called <code> blogs </code> as well as create an IAM Role that allows the code running in the container to use Role Based Access to read the DynamoDB table.

The repository also includes two command line demos: <code> fargate-demo </code>, as well as a <code> ecs-demo </code>. Both of these demos were featured in the <a href="https://www.edx.org/course/building-containerized-applications-on-aws"> Building Containerized Applications on AWS </a> course on edX. You'll notice however, that there are many places you need to fill in the blank for these demos to work in your own account if you choose to try them. Anything that is surrounded by < carrots like this > need to be removed and filled in with your own information. These demos are to be used as reference material only.


[*version_1.0.0]

©2020 Amazon Web Services, Inc. and its affiliates. All rights reserved. This work may not be reproduced or redistributed, in whole or in part, without prior written permission from Amazon Web Services, Inc. Commercial copying, lending, or selling is prohibited.
