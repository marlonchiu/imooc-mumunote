import io
import random
import string
from datetime import datetime

# 这个PIL就是pillow  pip install pillow
from PIL import Image, ImageFont, ImageDraw

class ImageCode():
  def get_text(self):
    # list = random.sample("123456789asdfghjk",4)
    list = random.sample(string.ascii_letters+string.digits, 4)
    # print(list)
    return "".join(list)

  def rand_color(self):
    # rgb的颜色
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red,green,blue

  # 绘制干扰线
  def draw_lines(self,draw,num,width,height):
    for i in range(num):
      x1 = random.randint(0, width)
      y1 = random.randint(0, height)
      x2 = random.randint(0, width)
      y2 = random.randint(height, height)
      draw.line(((x1,y1),(x2,y2)), fill="black", width=2)

  def draw_verify_code(self):
    # 生成随机字符串
    code = self.get_text()
    print(code)

    # 设置图片的宽和高 ,在实际项目当中最好跟前端显示图片的大小一致，这样就不用前端再重写图片大小了
    width,height = 80,38
    im = Image.new("RGB",(width, height),"white")

    font = ImageFont.truetype(font="C:\Windows\Fonts\Arial.ttf", size=20)
    draw = ImageDraw.Draw(im)
    # 绘制字符串
    for i in range(4):
      draw.text((random.randint(3, 10) + 15*i, random.randint(3, 10)),
                  text=code[i], fill=self.rand_color(), font=font)

    # 绘制干扰线
    self.draw_lines(draw,2,width,height)

    # im.show()
    return im,code

  def get_code(self):
    im,code = self.draw_verify_code()
    buf = io.BytesIO()
    im.save(buf, "jpeg")
    image_b_string = buf.getvalue()
    return code, image_b_string




# image_code = ImageCode()
# image_code.draw_verify_code()

def model_to_json(result):
  dict = {}
  for k,v in result.__dict__.items():
    if not k.startswith("_sa_"):
      if isinstance(v, datetime):
        v = v.strftime("%Y-%m-%d %H:%M:%S")
      dict[k] = v
  return dict

# ue图片压缩
def compress_image(source, dest, width=1200):
  im = Image.open(source)
  # 获取图片的宽和高
  x, y = im.size
  if x>width:
    # 进行等比例缩放
    ys = int(y*width/x)
    xs = width
    # 调整图片大小
    temp = im.resize((xs,ys), Image.ANTIALIAS)
    temp.save(dest,quality=80)
  else:
    im.save(dest,quality=80)
