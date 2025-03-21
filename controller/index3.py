from flask import Blueprint, render_template, session

index3 = Blueprint('index3', __name__)

@index3.route('/index3-new')
def my_index():
    session['username'] = '狂徒张三'

    article ={
        'title': 'python语言的基础入门',
        "count": 100,
        'content': '<strong>Python</strong> is a good language'
    }

    html = render_template('index3.html', article=article)
    return html
