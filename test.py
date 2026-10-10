from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Guys! This is my Python web application running through Jenkins and Docker."

if __name__ == "__main__":
    app.run(host="18.60.62.57", port=5000)
