from flask import Blueprint, render_template, session

index2 = Blueprint('index2', __name__)

@index2.route('/index-new')
def my_index():
    session['username'] = '狂徒张三'

    article ={
        'title': 'python语言的基础入门',
        "count": 10,
        'content': 'python is a good language'
    }

    html = render_template('index2.html', article=article)
    return html
