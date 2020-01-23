# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except
# in compliance with the License. A copy of the License is located at
#
# https://aws.amazon.com/apache-2-0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.


from flask import Flask, render_template, request
import boto3
import json

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


@app.route("/")
@app.route("/main")
def main():
    return render_template('index.html')

@app.route('/list_blog_posts',methods=['GET'])
def list_blog_posts():
    table = dynamodb.Table('Blog')
    response = table.scan()
    print(response)
    return json.dumps(response['Items'])
   

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)