from flask import Flask
from flask import request, jsonify, render_template, redirect



app = Flask(__name__)


@app.route('/')
def home():
    return jsonify('Hello World!!!')
