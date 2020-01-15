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