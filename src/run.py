#!/usr/bin/python
from flask import Flask, render_template, request, send_file
from PIL import Image
import PIL

app = Flask(__name__)

# Este método retorna uma imagem quando solicitado na url e envia-se um valor type = 1
# Pesquisar no Browser http://localhost:5000/get_image?type=1
@app.route('/get_image')
def get_image():
    if request.args.get('type') == '1':
        filename = '/home/raul/PycharmProjects/rest_python/src/temp_image'
    else:
        filename = '/home/raul/PycharmProjects/rest_python/src/error_image'
    return send_file(filename, mimetype='image/gif')

# Envia a imagem para um metodo no servidor
# Chamar essa função através do cmd curl -F "file=@mirayr.jpg" http://localhost:5000/rotate
@app.route("/rotate", methods=["POST"])
def rotate():
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
