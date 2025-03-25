import json
import re
from flask import Blueprint, make_response, session, request

from common import response_message
from common.email_utils import gen_email_code, send_email
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


@user.route("/ecode",methods=["post"])
def email_code():
  # email = request.form.get("email")
  email = json.loads(request.data).get("email")
  # 简单的邮箱格式验证
  if not email:
      return response_message.UserMessage.other("请输入邮箱")
  # 简单的邮箱格式验证
  if not re.match(".+@.+\..+",email):
      return response_message.UserMessage.other("无效的邮箱")
  # 生成邮箱验证码的随机字符串
  code = gen_email_code()

  # 发送邮件
  try:
    send_email(email,code)
    session['ecode'] = code.lower()
    return response_message.UserMessage.success("邮件发送成功")
  except Exception as e:
    print('__邮件发送失败__',e)
    return response_message.UserMessage.error("邮件发送失败")
