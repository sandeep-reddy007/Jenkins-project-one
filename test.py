from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Guys! My name is Sandeep reddy I am a Python with Deops engineer"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
