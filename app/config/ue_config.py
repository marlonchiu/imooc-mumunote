UECONFIG = {
    # 编辑器初始化内容
    "initialContent": '<p>我是初始化内容，设不设置都可以</p>',
    # 初始化编辑器宽度,默认 1000
    "initialFrameWidth":700,
    # 初始化编辑器高度,默认 320
    # "initialFrameHeight":1000,
    # ##### 宽度和高度设置都没好用 ########
    # 初始化时，是否让编辑器获得焦点，默认为 false
    "focus":True,
    # #  执行上传图片的action名称，默认值：uploadimage
    "imageActionName": "image",
    # #  提交的图片表单名称，默认值：upfile
    "imageFieldName": "file",
    # #  上传大小限制，单位B，默认值：2048000
    "imageMaxSize": 10485760,
    # #  上传图片格式显示，默认值：[".png", ".jpg", ".jpeg", ".gif", ".bmp"]
    "imageAllowFiles": [".jpg", ".png", ".jpeg"],
    # #  是否压缩图片,默认是true
    "imageCompressEnable": True,
    # #  图片压缩最长边限制，默认值：1600
    "imageCompressBorder": 5000,
    # #  插入的图片浮动方式，默认值：none
    "imageInsertAlign": "none",
    # #  图片访问路径前缀，默认值：空
    "imageUrlPrefix": "",

    #  执行上传涂鸦的action名称，默认值：uploadscrawl
    "scrawlActionName": "crawl",
    #  提交的图片表单名称，默认值：upfile
    "scrawlFieldName": "file",
    #  上传大小限制，单位B，默认值：2048000
    "scrawlMaxSize": 10485760,
    #  图片访问路径前缀，默认值：空
    "scrawlUrlPrefix": "",
    #  插入的图片浮动方式，默认值：none
    "scrawlInsertAlign": "none",

    #  执行上传截图的action名称，默认值：uploadimage
    "snapscreenActionName": "snap",
    #  图片访问路径前缀
    "snapscreenUrlPrefix": "",
    #  插入的图片浮动方式，默认值：none
    "snapscreenInsertAlign": "none",

    #  例外的图片抓取域名
    "catcherLocalDomain": [
      "127.0.0.1",
      "localhost"
    ],
    #  执行抓取远程图片的action名称，默认值：catchimage
    "catcherActionName": "catch",
    #  提交的图片列表表单名称，默认值：source
    "catcherFieldName": "source",
    #  图片访问路径前缀，默认值：空
    "catcherUrlPrefix": "",
    #  上传保存路径,可以自定义保存路径和文件名格式，默认值：{filename}{rand:6}
    "catcherMaxSize": 10485760,
    #  抓取图片格式显示，默认值：[".png", ".jpg", ".jpeg", ".gif", ".bmp"]
    "catcherAllowFiles": [
      ".jpg",
      ".png",
      ".jpeg"
    ],

    #  执行上传视频的action名称，默认值：uploadvideo
    "videoActionName": "video",
    #  提交的视频表单名称，默认值：upfile
    "videoFieldName": "file",
    #  视频访问路径前缀
    "videoUrlPrefix": "",
    #  上传大小限制，单位B，默认值：102400000
    "videoMaxSize": 104857600,
    #  上传视频格式显示
    "videoAllowFiles": [
      ".mp4"
    ],

    #  执行上传文件的action名称，默认值：uploadfile
    "fileActionName": "file",
    #  提交的文件表单名称，默认值：upfile
    "fileFieldName": "file",
    #  文件访问路径前缀
    "fileUrlPrefix": "",
    #  上传保存路径,可以自定义保存路径和文件名格式，默认值：{filename}{rand:6}
    "fileMaxSize": 104857600,
    #  上传文件格式显示
    "fileAllowFiles": [
      ".zip",
      ".pdf",
      ".doc"
    ],

    #  执行图片管理的action名称，默认值：listimage
    "imageManagerActionName": "listImage",
    #  每次列出文件数量
    "imageManagerListSize": 20,
    #  图片访问路径前缀
    "imageManagerUrlPrefix": "",
    #  插入的图片浮动方式，默认值：none
    "imageManagerInsertAlign": "none",
    #  列出的文件类型
    "imageManagerAllowFiles": [
      ".jpg",
      ".png",
      ".jpeg"
    ],

    #  执行文件管理的action名称，默认值：listfile
    "fileManagerActionName": "listFile",
    #  指定要列出文件的目录
    "fileManagerUrlPrefix": "",
    #  每次列出文件数量
    "fileManagerListSize": 20,
    #  列出的文件类型
    "fileManagerAllowFiles": [
      ".zip",
      ".pdf",
      ".doc"
    ],

    #  公式配置
    "formulaConfig": {
      #  公式渲染的路径
      "imageUrlTemplate": "https://latex.codecogs.com/svg.image?{}"
    }
}

#  发表评论的ue配置
FEEDBACK_UECONFIG = {
    # 编辑器初始化内容
    "initialContent": '<p>请在此发表您的评论</p>',
    # 初始化编辑器宽度,默认 1000
    "initialFrameWidth":670,
    # 初始化编辑器高度,默认 320
    # "initialFrameHeight":1000,
    # ##### 宽度和高度设置都没好用 ########
    # 初始化时，是否让编辑器获得焦点，默认为 false
    "focus":True,
    # # 执行上传图片的action名称，默认值：uploadimage
    "imageActionName": "image",
    # #  提交的图片表单名称，默认值：upfile
    "imageFieldName": "file",
    # #  上传大小限制，单位B，默认值：2048000
    "imageMaxSize": 10485760,
    # #  上传图片格式显示，默认值：[".png", ".jpg", ".jpeg", ".gif", ".bmp"]
    "imageAllowFiles": [
        ".jpg",
        ".png",
        ".jpeg"
    ],
    # #  是否压缩图片,默认是true
    "imageCompressEnable": True,
    # #  图片压缩最长边限制，默认值：1600
    "imageCompressBorder": 5000,
    # #  插入的图片浮动方式，默认值：none
    "imageInsertAlign": "none",
    # #  图片访问路径前缀，默认值：空
    "imageUrlPrefix": "",

    #  执行上传涂鸦的action名称，默认值：uploadscrawl
    "scrawlActionName": "crawl",
    #  提交的图片表单名称，默认值：upfile
    "scrawlFieldName": "file",
    #  上传大小限制，单位B，默认值：2048000
    "scrawlMaxSize": 10485760,
    #  图片访问路径前缀，默认值：空
    "scrawlUrlPrefix": "",
    #  插入的图片浮动方式，默认值：none
    "scrawlInsertAlign": "none",

    #  执行上传截图的action名称，默认值：uploadimage
    "snapscreenActionName": "snap",
    #  图片访问路径前缀
    "snapscreenUrlPrefix": "",
    #  插入的图片浮动方式，默认值：none
    "snapscreenInsertAlign": "none",

    #  例外的图片抓取域名
    "catcherLocalDomain": [
      "127.0.0.1",
      "localhost"
    ],
    #  执行抓取远程图片的action名称，默认值：catchimage
    "catcherActionName": "catch",
    #  提交的图片列表表单名称，默认值：source
    "catcherFieldName": "source",
    #  图片访问路径前缀，默认值：空
    "catcherUrlPrefix": "",
    #  上传保存路径,可以自定义保存路径和文件名格式，默认值：{filename}{rand:6}
    "catcherMaxSize": 10485760,
    #  抓取图片格式显示，默认值：[".png", ".jpg", ".jpeg", ".gif", ".bmp"]
    "catcherAllowFiles": [
      ".jpg",
      ".png",
      ".jpeg"
    ],

    #  执行上传视频的action名称，默认值：uploadvideo
    "videoActionName": "video",
    #  提交的视频表单名称，默认值：upfile
    "videoFieldName": "file",
    #  视频访问路径前缀
    "videoUrlPrefix": "",
    # 上传大小限制，单位B，默认值：102400000
    "videoMaxSize": 104857600,
    #  上传视频格式显示
    "videoAllowFiles": [
      ".mp4"
    ],

    #  执行上传文件的action名称，默认值：uploadfile
    "fileActionName": "file",
    #  提交的文件表单名称，默认值：upfile
    "fileFieldName": "file",
    #  文件访问路径前缀
    "fileUrlPrefix": "",
    #  上传保存路径,可以自定义保存路径和文件名格式，默认值：{filename}{rand:6}
    "fileMaxSize": 104857600,
    #  上传文件格式显示
    "fileAllowFiles": [
      ".zip",
      ".pdf",
      ".doc"
    ],

    #  执行图片管理的action名称，默认值：listimage
    "imageManagerActionName": "listImage",
    #  每次列出文件数量
    "imageManagerListSize": 20,
    #  图片访问路径前缀
    "imageManagerUrlPrefix": "",
    #  插入的图片浮动方式，默认值：none
    "imageManagerInsertAlign": "none",
    #  列出的文件类型
    "imageManagerAllowFiles": [
      ".jpg",
      ".png",
      ".jpeg"
    ],

    #  执行文件管理的action名称，默认值：listfile
    "fileManagerActionName": "listFile",
    #  指定要列出文件的目录
    "fileManagerUrlPrefix": "",
    #  每次列出文件数量
    "fileManagerListSize": 20,
    #  列出的文件类型
    "fileManagerAllowFiles": [
      ".zip",
      ".pdf",
      ".doc"
    ],

    #  公式配置
    "formulaConfig": {
      #  公式渲染的路径
      "imageUrlTemplate": "https://latex.codecogs.com/svg.image?{}"
    }
}
