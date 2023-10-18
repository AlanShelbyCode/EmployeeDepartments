from app import app, db
from models import Departaments, Employees
from flask import render_template, request, redirect

@app.route('/', methods=["GET"] )
def index():
    return render_template('index.html')


# @app.route("/")
# def main():
#     articles = Article.query.all()
#     categories = Category.query.all()
#     return render_template("main/index.html", articles=articles, categories=categories)
#
