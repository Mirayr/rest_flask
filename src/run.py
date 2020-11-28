#!/usr/bin/python
from flask import Flask, render_template, request
from PIL import Image
import PIL

app = Flask(__name__)

# Envia a imagem para um metodo no servidor
# Chamar essa função através do cmd curl -F "file=@mirayr.jpg" http://localhost:5000/rotate
@app.route("/rotate", methods=["POST"])
def dump_image():
    img = Image.open(request.files['file'])
    img = img.rotate(45)
    img.save("/home/raul/PycharmProjects/rest_python/src/temp_image", "JPEG")
    return 'Success! '


@app.route("/")
def index():
    nome = "Mirayr"
    posts =["Flask Básico", "Flask Intermediário", "Flask Avançado"]
    return render_template("index.html", nome=nome, posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
