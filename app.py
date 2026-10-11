
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello! Welcome to My Cloud Application.</h1>
    <p>Version 2 - Automatic CI/CD Deployment Successful!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)