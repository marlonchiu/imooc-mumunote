from flask import Blueprint, render_template, session

index5 = Blueprint('index5', __name__)

# 蓝图上下文处理器

@index5.context_processor
def my_fun3():
    my_dict = {
        "count": 100,
        'content2': '<strong>Python</strong> is a good language'
        }
    return dict(my=my_dict)

@index5.context_processor
def my_fun4():
    def add(a, b):
        return a + b

    return dict(my_add=add)

@index5.context_processor
def my_fun5():
    def add(a, b):
        return a + b

    return {'my_add2': add}


@index5.route('/index5-new')
def my_index():
    html = render_template('index5.html')
    return html
