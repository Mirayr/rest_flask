#!/usr/bin/python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    nome = "Mirayr"
    posts =["Flask Básico", "Flask Intermediário", "Flask Avançado"]
    return render_template("index.html", nome=nome, posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
