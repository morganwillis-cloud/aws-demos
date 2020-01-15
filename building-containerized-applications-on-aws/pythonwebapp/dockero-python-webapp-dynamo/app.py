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