from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! AJKE 5TAR DIKE CSE471 PROJECT SHOWCASING ASE 9C-16T te"

if __name__ == "__main__":
    app.run()
