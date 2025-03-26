
class UserMessage():
    """
    我们在企业当中，一般每个企业都会对响应的状态码做出一些规定
    比如说，用户响应的都以1开头，然后规定成功了 {status:1000,data:'asdf'}
    错误的状态码1002
    其它状态码1001

    """
    @staticmethod
    def success(data):
        return {"status": 1000, "data": data}

    @staticmethod
    def error(data):
        return {"status": 1002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 1001, "data": data}


# article文章的状态 就以2开头
class ArticleMessage():
    @staticmethod
    def success(data):
        return {"status": 2000, "data": data}
    @staticmethod
    def save_success(article_id,data):
        return {"status": 2003, "article_id": article_id, "data":data}

    @staticmethod
    def error(data):
        return {"status": 2002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 2001, "data": data}


# 收藏的就以3开头
class FavoriteMessage():
    @staticmethod
    def success(data):
        return {"status": 3000, "data": data}

    @staticmethod
    def error(data):
        return {"status": 3002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 3001, "data": data}
