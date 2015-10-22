import flask
import subprocess
import time          #You don't need this. Just included it so you can see the output stream.
from TrudgeBiosMarkovBot import *


app = flask.Flask(__name__)

@app.route('/')
def index():

    return createBio(first, grams)

