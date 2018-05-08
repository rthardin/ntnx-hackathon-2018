from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
  return "Nutanix Hackathon 2018 - Did It All For The Cookies"
