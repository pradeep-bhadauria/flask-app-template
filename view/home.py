import os
from flask import Blueprint, render_template, request, json

dir_path = os.path.dirname(os.path.realpath(__file__))
mod = Blueprint('home', __name__, url_prefix='', template_folder='templates')


@mod.route('/', methods=['GET'])
def home():
    return render_template('index.html')

