
class UserMessage():
    """
    我们在企业当中，一般每个企业都会对响应的状态码做出一些规定
    比如说，用户响应的都以1开头，然后规定成功了 {status:1000,data:'asdf'}
    错误的状态码1002
    其它状态码1001

    """
    @staticmethod
    def success(data):
        return {"status":1000,"data":data}

    @staticmethod
    def error(data):
        return {"status": 1002, "data": data}

    @staticmethod
    def other(data):
        return {"status": 1001, "data": data}
