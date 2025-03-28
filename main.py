from app.app import create_app
import logging
from waitress import serve
from cheroot.wsgi import Server as WSGIServer
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

app = create_app()

if __name__ == '__main__':
    logging.info("我是info的日志")
    logging.debug("我是debug的日志")

    # 选择1：开发环境使用 Flask 开发服务器
    app.run(host='0.0.0.0', port=5000, debug=True)

    # 选择2：使用 waitress（稳定、简单）
    # serve(app, host='0.0.0.0', port=5000)

    # 选择3：使用 CherryPy 的 WSGI 服务器（性能好、功能丰富）
    # server = WSGIServer(('0.0.0.0', 5000), app)
    # try:
    #     server.start()
    # except KeyboardInterrupt:
    #     server.stop()

    # 选择4：使用 Tornado（高性能、异步支持）
    # http_server = HTTPServer(WSGIContainer(app))
    # http_server.listen(5000)
    # IOLoop.instance().start()
