from flask import Flask, render_template, request, redirect, url_for
from web_app import app #from the app module import app(web_app.py main)


@app.route('/', methods=['GET'])
def getAll():
    return ""