# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:55:58 2020

@author: saura
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('my_index.html')

# by default 'render_template' looks in the 'templates' folder in the same directory for the given file.
# and the '.html' file might be pointing to '.css' and '.js' file, 
# but 'render_template' will only allow those files if they are in 'static' folder.

@app.route('/blog')
def blog():
    return 'This is my blog section!'

@app.route('/blog/2020/dog')
def blog_dog():
    return 'This blog is about my dog, Rocky!'

@app.route('/blog/<username>/<int:age>')      # if we don't specify the variable type, it will be taken as string by default.
def user_blog(username, age):
    return render_template('user_blog.html', name = username, age = age)

