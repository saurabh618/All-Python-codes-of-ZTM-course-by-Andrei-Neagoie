# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 13:59:58 2020

@author: saura
"""
from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		data = request.form.to_dict()
		write_to_csv(data)
		write_to_txt(data)
		return redirect('./thank_you.html')     # or we can use 'render_template('thank_you.html')'
	else:
		return 'Something went wrong. Try again!'

def write_to_txt(data):
	email = data["email"]
	subject = data["subject"]
	message = data["message"]
	with open("./database.txt", mode = 'a') as database:
		text = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
	email = data["email"]
	subject = data["subject"]
	message = data["message"]
	with open("./database.csv", mode = 'a', newline='') as database2:
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])
