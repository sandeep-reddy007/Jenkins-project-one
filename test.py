from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Guys! This is my Python web application running through Jenkins and Docker.I am the a devops engineer having 5 years of ex "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
