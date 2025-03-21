# imooc-mumunote

> [慕课网 | Python Flask 全流程全栈项目实战](https://coding.imooc.com/class/713.html)

## 参考文档

> [关于 Flask](https://flask.palletsprojects.com/en/stable/)

> [关于 Jinja2](https://docs.jinkan.org/docs/jinja2/)


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
