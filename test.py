from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """Hello Guys! My name is Sandeep reddy I am a Python with Deops engineer,
              This is my Python web application running through Jenkins and Docker,
              Having 5 years of experiance in both applicaton development and AWS deops"""

if __name__ == "__main__":
    app.run(host="16.112.26.118", port=8000)
