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
import json

app = Flask(__name__)

@app.route("/")
@app.route("/main")
def main():
    print("Rendering home page...")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)