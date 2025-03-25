from flask import Blueprint, make_response, session
from model.user import User
from common.utils import ImageCode

# 创建蓝图对象
user = Blueprint('user', __name__)

# @user.route('/aaa' )
# def get_one():
#   user = User()
#   result = user.get_one()
#   print('_____', result.username)
#   return "OK"

@user.route("/vcode")
def vcode():
  code,bstring = ImageCode().get_code()
  response = make_response(bstring)
  response.headers["Content-Type"]="image/jpeg"
  # 存储起来，我们暂时存储到内存中，也就是session里边
  session['vcode'] = code.lower()
  print(code.lower())
  
  return response
