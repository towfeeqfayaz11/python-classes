from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def hello_home():
    return "<p>Hello, From Home!</p>"

if __name__ == "__main__":
    app.run()
