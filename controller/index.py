from flask import Blueprint, render_template

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

@index.route('/index3')
def my_index3():
    username = 'marlonchiu'
    str = '<strong>{}</strong>'.format(username)
    return str

@index.route('/index4')
def my_index4():
    str = """
      <!DOCTYPE html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <meta http-equiv="X-UA-Compatible" content="ie=edge" />
          <title>Document</title>
        </head>
        <body>
          <button>点击跳转到百度</button>
          <span>5</span>
          <script>
            const myBtn = document.querySelector('button')
            const myBlock = document.querySelector('span')

            // 1. 手动跳转
            myBtn.onclick = function () {
              window.location.href = 'https://www.baidu.com'
            }

            // 倒计时5 秒自动跳转
            var timer = 5
            setInterval(function () {
              if (timer <= 0) {
                window.location.href = 'https://www.baidu.com'
              } else {
                myBlock.innerHTML = timer
                timer--
              }
            }, 1000)
          </script>
        </body>
      </html>
    """

    return str

@index.route('/index5')
def my_index5():
    str = """

      <!DOCTYPE html>
      <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <meta http-equiv="X-UA-Compatible" content="ie=edge" />
          <title>Document</title>
        </head>
        <body>
          <button>点击跳转到百度</button>
          <span>5</span>
          <script>
            const myBtn = document.querySelector('button')
            const myBlock = document.querySelector('span')

            // 1. 手动跳转
            myBtn.onclick = function () {
              window.location.href = 'https://www.baidu.com'
            }

            // 倒计时5 秒自动跳转
            var timer = {{timer}}
            setInterval(function () {
              if (timer <= 0) {
                window.location.href = 'https://www.baidu.com'
              } else {
                myBlock.innerHTML = timer
                timer--
              }
            }, 1000)
          </script>
        </body>
      </html>
    """

    str = str.replace("{{timer}}", "10")
    return str

@index.route('/index6')
def my_index6():
    with open('template/index.html', encoding="utf-8") as file:
        html = file.read()

    html = html.replace("{{timer}}", "10")
    return html

@index.route('/index7')
def my_index7():
    t=8
    html = render_template('index.html', timer=t)
    return html
