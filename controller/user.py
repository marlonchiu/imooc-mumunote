from flask import Blueprint
from common.user import User

# 创建蓝图对象
user = Blueprint('user', __name__)

@user.route('/aaa' )
def get_one():
  user = User()
  result = user.get_one()
  print('_____', result.username)
  return "OK"
