from turtle import pos
from flask import render_template
from app import app
from teste import Controller

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Otniel"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', title="Home", user=user, posts=posts)