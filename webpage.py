import flask
import subprocess
from TrudgeBiosMarkovBot import *


app = flask.Flask(__name__)

@app.route('/')
def index():

    return createBio(first, grams)

