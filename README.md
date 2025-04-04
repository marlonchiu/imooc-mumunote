# imooc-mumunote

> [慕课网 | Python Flask 全流程全栈项目实战](https://coding.imooc.com/class/713.html)

> [Youtube | Python Flask 全流程全栈项目实战](https://www.youtube.com/playlist?list=PLULgBZmS3YWS_QqAyw34MrmMOuZIjYubb)

## 参考文档

> [关于 Flask](https://flask.palletsprojects.com/en/stable/)

> [关于 Jinja2](https://docs.jinkan.org/docs/jinja2/)

> [PyMySQL](https://pypi.org/project/PyMySQL/)

> [在 windows 上安装 Redis](https://redis.com.cn/redis-installation.html)

## 创建虚拟环境

```bash
pip install virtualenv
pip install virtualenvwrapper-win
```

## 配置环境变量(window)

在数据磁盘创建一个文件夹，名字叫做`python_env`，环境变量中增加一个变量，名字叫`WORKON_HOME`，值为路径：`D:\python_env`。
检查 `echo %WORKON_HOME%`

## 虚拟环境的基本使用

1、创建虚拟环境: `mkvirtualenv 环境名`
2、删除虚拟环境: `rmvirtualenv 环境名`
3、查看所有的虚拟环境: `workon`
4、进入虚拟环境: `workon 环境名`
5、退出虚拟环境: `deactivate`

## `requirements.txt` 文件

1、创建命令: `pip freeze > requirements.txt`
2、导入环境命令: `pip install -r ./requirements.txt`

## 安装虚拟机和操作系统及工具

VirtualBox 、Ububtu server、xshell、mysql、Navicat

## 什么是 SQLAlchemy 框架?

- SQLAlchemy 是 Python 编程语言下的一款开源软件。
- SQLAlchemy 提供了 SQL 工具包及对象关系映射(ORM)工具
- 为高效和高性能的数据库访问而设计，实现了完整的企业级持久模型
- 安装 SQLAlchemy 命令: `pip install SQLAlchemy`

## 图片验证码

1. 安装命令: `pip install pillow`

## Python Web 中间件

说明： gunicorn 实际上是一个仅支持 Unix-like 系统（Linux/macOS）的 WSGI 服务器，在 Windows 上并不能直接使用。

1. 安装命令: `pip install gunicorn`
2. 启动命令: `gunicorn --worker=2 -b 0.0.0.0:5000 main:app`

## 在 windows 上启动

在 window 上，需要安装 `waitress`

```bash

pip install waitress

pip install cherrypy

pip install tornado

# pip freeze > requirements.txt

python main.py
```

现在我们有了四个选择，每个都有其特点：

- Flask 开发服务器
  - 优点：开发友好，自动重载
  - 缺点：不适合生产环境
  - 适用场景：本地开发
- Waitress
  - 优点：纯 Python 实现，配置简单，稳定可靠
  - 缺点：性能一般
  - 适用场景：小型应用，需要稳定性
- CherryPy
  - 优点：功能丰富，性能好
  - 缺点：配置相对复杂
  - 适用场景：中型应用，需要更多控制
- Tornado
  - 优点：高性能，支持异步
  - 缺点：配置较复杂
  - 适用场景：大型应用，需要处理大量并发

1. 对于一般的开发和小型应用，我建议使用 Waitress，因为它：配置简单、稳定可靠、纯 Python 实现，没有复杂依赖、Windows 上运行良好
2. 如果您的应用需要处理大量并发请求，可以考虑使用 Tornado。
3. 如果需要更多的配置选项和控制，可以使用 CherryPy。
