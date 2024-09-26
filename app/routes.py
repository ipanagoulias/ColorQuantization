from app import app
from flask import Flask, render_template, request, send_file, url_for
from .utils import mykmeans
import os

@app.route('/', methods=['GET', 'POST'])
def index():

    images_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'images'))
    image_files = [f for f in os.listdir(images_folder) if f.startswith('image') and f.endswith('.jpg')]
    original_image = image_files[0]
    ncol = 1
    clustered_image = mykmeans(ncol, original_image)

    if request.method == 'POST':
        original_image = request.form['original_image']
        ncol = int(request.form['ncol'])
        clustered_image = mykmeans(ncol, original_image)

    return render_template('index.html', image_files=image_files, original_image=original_image, clustered_image=clustered_image, ncol=ncol)

@app.route('/image/<filename>')
def get_image(filename):
    images_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'images'))
    return send_file(os.path.join(images_folder, filename))







