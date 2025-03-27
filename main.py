from app.app import create_app
import logging
from waitress import serve

app = create_app()

if __name__ == '__main__':
    logging.info("我是info的日志")
    logging.debug("我是debug的日志")

    # 开发环境使用 Flask 开发服务器
    # app.run(host='0.0.0.0', port=5000, debug=True)
    
    # 生产环境使用 waitress
    serve(app, host='0.0.0.0', port=5000)
