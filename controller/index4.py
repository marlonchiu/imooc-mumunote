from flask import Blueprint, render_template, session

index4 = Blueprint('index4', __name__)

# 蓝图上下文处理器
@index4.context_processor
def my_context_processor():
    #上下文处理器里边的返回值必须是字典类型
    return {
        'username': session.get('username'),
        'title': 'python语言的基础入门',
        }

@index4.context_processor
def my_context_processor2():
    my_dict = {
        "count": 100,
        'content': '<strong>Python</strong> is a good language'
        }
    return my_dict

@index4.context_processor
def my_context_processor3():
    my_dict = {
        "count": 100,
        'content2': '<strong>Python</strong> is a good language'
        }
    return dict(my=my_dict)


@index4.route('/index4-new')
def my_index():
    html = render_template('index4.html')
    return html
