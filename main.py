# 导入 Flask
from flask import Flask, make_response, request, session
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# 设置secret key用于session加密
app.config['SECRET_KEY'] = os.urandom(24)  # 生成随机密钥

@app.route('/')
def hello_world():
    return 'Hello World！'

# 设置cookie
@app.route('/add_cookie', methods=['POST', 'GET'])
def add_cookie():
    response = make_response('设置cookie成功')
    # response.set_cookie('username', 'admin',max_age=10) # 设置cookie的过期时间 10s

    # 设置cookie的过期时间 1天后过期
    expires_time = datetime.now() + timedelta(days=1) # 设置cookie的过期时间 1天后过期
    response.set_cookie('username', 'marlon',expires=expires_time)
    response.set_cookie('city', 'beijing',expires=expires_time)
    return response


# 获取cookie
@app.route('/get_cookie', methods=['POST', 'GET'])
def get_cookie():
    cookies = request.cookies
    cookies_dict = request.cookies.to_dict()
    print(cookies)
    print(cookies_dict)

    for key, value in cookies_dict.items():
        print(key, value)

    username = cookies.get('username')
    city = cookies.get('city')
    # return '获取cookie成功'
    return 'username: %s, city: %s' % (username, city)

# 删除cookie
@app.route('/del_cookie', methods=['POST', 'GET'])
def del_cookie():
    response = make_response('删除cookie成功')
    # 删除一个
    # response.delete_cookie('username')

    # 删除所有
    cookies_dict = request.cookies.to_dict()
    for key, value in cookies_dict.items():
        response.delete_cookie(key)
    return response

# 操作session
# 设置session
@app.route('/add_session')
def add_session():
    session['username'] = 'marlon'
    session['nickname'] = 'zxh'
    session['role'] = 'admin'
    return '设置session成功'

# 获取session (要获取必须先设置)
@app.route('/get_session')
def get_session():
    print(session)
    username = session.get('username')
    nickname = session.get('nickname')
    role = session.get('role')
    print('username: %s, nickname: %s, role: %s' % (username, nickname, role))
    return '获取session成功 >>> ' + 'username: %s, nickname: %s, role: %s' % (username, nickname, role)

# 删除session
@app.route('/del_session')
def del_session():
    # 清除单个
    # session.pop('username')
    # session.pop('nickname')

    # 清除所有
    session.clear()
    # session.pop('role')
    print(session)
    return '删除session成功'

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=5000, debug=True)
