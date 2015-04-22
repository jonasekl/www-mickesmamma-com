import yaml
from flask import Flask, Response, request
from flask import render_template
from random import randint


app = Flask(__name__)

@app.route('/')
def start():
    terms = yaml.load(open('./mickesmamma.yml').read())['terms']
    i = randint(0,2)
    print i
    return '<h1>%s</h1>' % terms[i]


if __name__ == '__main__':
    app.run()
