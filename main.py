from app.app import create_app
import logging

app = create_app()

if __name__ == '__main__':
    logging.info("我是info的日志")
    logging.debug("我是debug的日志")

    # app.run()
    app.run(host='0.0.0.0', port=5000, debug=True)
