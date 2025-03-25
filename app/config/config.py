# 全局通用配置
class Config(object):
    db_url = "mysql+pymysql://root:123456@127.0.0.1:3306/mumushouji"

    # 前端页面显示的条数
    page_count = 10

    # 配置一下文章图片的存储路径
    article_header_image_path = "/images/article/header/"

    # 邮箱配置
    email_name = '93513472@qq.com'  # 发送方邮箱
    email_passwd = 'hsceydswmritbdhb'  # 填入发送方邮箱的授权码

    # 配置头像存储路径
    user_header_image_path = "/images/headers/"

# 测试环境
class TestConfig(Config):
    # db_url = ""
    if_echo=True
    LOG_LEVEL="DEBUG"

class ProductionConfig(Config):
    if_echo=False
    LOG_LEVEL = "INFO"

config = {
    "test": TestConfig,
    "prod": ProductionConfig
}
