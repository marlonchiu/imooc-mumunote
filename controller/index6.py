from flask import Blueprint, render_template, session

index6 = Blueprint('index6', __name__)

@index6.route('/shouji_index')
def my_index():
    html = render_template('shouji_index.html')
    return html

@index6.route('/article-info')
def my_index2():
    html = render_template('article-info.html')
    return html
