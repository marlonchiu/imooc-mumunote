import hashlib
import json
import re
from flask import Blueprint, make_response, session, request, url_for

from app.config.config import config
from app.settings import env
from common import response_message
from common.email_utils import gen_email_code, send_email
from model.user import User
from common.utils import ImageCode
from common.redisdb import redis_connect

# 创建蓝图对象
redis_user = Blueprint("redis_user", __name__)

redis_client = redis_connect()
@redis_user.route("/redis/ecode",methods=["post"])
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
    # session['ecode'] = code.lower()
    # redis_client.set(email,code.lower())
    # 我们的名字加一个冒号，RDM会帮助我们把所有冒号前边的内容形成一个文件夹，这样更方便我们的查看
    email_ecode = "email:"+email
    redis_client.set(email_ecode, code.lower())
    # redis_client.set(email_ecode,code.lower(),ex=60*5)
    # 单独设置过期时间
    redis_client.expire(email_ecode, 60)
    return response_message.UserMessage.success("邮件发送成功")
  except Exception as e:
    print('__邮件发送失败__',e)
    return response_message.UserMessage.error("邮件发送失败")


@redis_user.route("/redis/register",methods=["post"])
def register():
  request_data = json.loads(request.data)
  username = request_data.get("username")
  password = request_data.get("password")
  second_password = request_data.get("second_password")
  ecode = request_data.get("ecode")
  redis_ecode = redis_client.get("email:"+username)

  # 做数据的验证
  if ecode.lower() != redis_ecode:
      return response_message.UserMessage.error("邮箱验证码错误")
  # 用户名 和 密码的验证
  if not re.match(".+@.+\..+", username):
      return response_message.UserMessage.other("无效的邮箱")

  if len(password) < 6:
      return response_message.UserMessage.error("密码不合法")

  if password != second_password:
      return response_message.UserMessage.error("两次密码不一致")

  # 用户名是否已经注册
  user = User()
  if len(user.find_by_username(username=username)) > 0:
      return response_message.UserMessage.error("用户名已经存在")

  # 实现注册的功能了
  password = hashlib.md5(password.encode()).hexdigest()
  result = user.do_register(username=username,password=password)
  return response_message.UserMessage.success("用户注册成功")
