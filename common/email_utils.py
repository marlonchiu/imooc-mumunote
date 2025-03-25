import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config.config import config
from app.settings import env

def gen_email_code():
    list = random.sample(string.ascii_letters+string.digits, 6)
    return "".join(list)

def send_email(email,code):
    email_name = config[env].email_name  # 发送方邮箱
    passwd = config[env].email_passwd  # 填入发送方邮箱的授权码
    # 不要，千万不要写我的授权码，你一定要写你自己的授权码！！！

    # 你要把邮件发给谁
    msg_to = email

    # 正文
    content = """
    慕慕手记注册验证码是:<h1 style='color:red'>{}</h1>
    """.format(code)
    msg = MIMEMultipart()
    msg["Subject"] = "慕慕手记验证码"
    # msg["From"] = "慕慕手记"
    msg["From"] = email_name
    msg["To"] = msg_to
    # 发送邮件正文，html格式的
    msg.attach(MIMEText(content, "html", "utf-8"))
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮箱服务器及端口号
    s.login(email_name, passwd)
    s.sendmail(email_name, msg_to, msg.as_string())
