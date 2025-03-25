# 全局通用配置
class Config(object):
    db_url = "mysql+pymysql://root:123456@127.0.0.1:3306/mumushouji"
    # 前端页面显示的条数
    page_count = 10

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
