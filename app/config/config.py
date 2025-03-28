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

    label_types = {
      "recommend": {"name": "请选择需要投递的栏目", "selected": "selected"},
      "auto_test": {"name": "自动化测试", "selected": "no-selected"},
      "python": {"name": "Python", "selected": "no-selected"},
      "java": {"name": "Java", "selected": "no-selected"},
      "function_test": {"name": "功能测试", "selected": "no-selected"},
      "perf_test": {"name": "性能测试", "selected": "no-selected"},
      "funny": {"name": "幽默段子", "selected": "no-selected"},
    }

    article_types = {
      "recommend": {"name": "请选择", "selected": "selected"},
      "first": {"name": "首发", "selected": "no-selected"},
      "original": {"name": "原创", "selected": "no-selected"},
      "other": {"name": "其它", "selected": "no-selected"},
    }
    article_tags = [
        "Html5", "Angular", "JS", "CSS3", "Sass/Less",
        "JAVA", "Python", "Go", "C++", "C#", "MySQL",
        "Oracle", "MongoDB", "Android", "Unity 3", "DCocos2d-x"
      ]

    # 配置redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    REDIS_PASSWORD = ''
    REDIS_POLL = 10
    REDIS_DB = 2
    REDIS_DECODE_RESPONSES = True

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
