from os import getenv

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p> I am running #{0}. Very secret signing key: {1}".format(
        getenv('GIT_COMMIT_SHA'),
        getenv('DETA_PYTHON_POC_SIGNING_KEY')
    )
