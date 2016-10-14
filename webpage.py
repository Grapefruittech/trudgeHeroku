import flask
from TrudgeBiosMarkovBot import *
from trudgeCheers import getCheer


app = flask.Flask(__name__)


@app.route('/')
def index():
    return '<a href="bios">Bios</a><p><a href="cheers">Cheers</a>'


@app.route('/bios')
def bios():
    return createBio(first, grams)


@app.route('/cheers')
def cheers():
    return getCheer()
