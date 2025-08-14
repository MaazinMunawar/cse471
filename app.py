from flask import Flask
import { Analytics } from "@vercel/analytics/next"

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! MY NAME IS MAAZIN"

if __name__ == "__main__":
    app.run()
