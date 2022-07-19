from crypt import methods
from turtle import pos
from flask import flash, redirect, render_template, url_for
from app import app
from app.forms import LoginForm
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)