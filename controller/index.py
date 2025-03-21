from flask import Blueprint

index = Blueprint('index', __name__)

@index.route('/index')
def my_index():
    return '<strong>我是首页!</strong>'

@index.route('/index2')
def my_index2():
    str = """
    <!DOCTYPE html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <meta http-equiv="X-UA-Compatible" content="ie=edge" />
          <title>点击跳转到百度</title>
        </head>
        <body>
          <button>点击跳转到百度</button>
          <script>
            document.querySelector('button').onclick = function () {
              window.location.href = 'https://www.baidu.com'
            }
          </script>
        </body>
      </html>

    """

    return str
