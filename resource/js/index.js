

console.log("index.js文件引入了")

var ClientHeight = document.documentElement.clientHeight; // 可视区域的高度，就是我们能看见的内容的高度
var allowRequest = true; // 锁定后端数据请求中的状态。 是否允许请求后端
var page = 1;
var endNum = 10; // 假设初始值为10，根据实际情况调整

function getUrlParams() {
    var uri = location.search;
    var final_result = {};
    // 第一次请求没有参数的时候
    if (uri === "") {
        final_result['page'] = page;
        final_result['article_type'] = 'recommend';
        final_result['start_num'] = 0;
        final_result['end_num'] = 10;
    } else {
        if (uri.indexOf("?") != -1) {
            params = uri.substr(1);
            params_list = params.split("&");
            for (var i = 0; i < params_list.length; i++) {
                var key = params_list[i].split("=")[0]; // article_type=recommend
                var value = params_list[i].split("=")[1]; // recommend
                final_result[key] = value;
            }
        }
    }
    return final_result;
}

function toNextPage(params) {
    console.log(params);
    // 开始拼接url
    var url = "?";
    for (var key in params) {
        if (key === "page") {
            params[key] = parseInt(params[key]) + 1;
        }
        if (key === "start_num") {
            params[key] = endNum;
        }
        url += key;
        url += "=";
        url += params[key];
        url += "&";
    }

    // 去掉末尾的&符号
    if (url.endsWith("&")) {
        url = url.substr(0, url.length - 1);
    }
    // 滚动标识

    console.log(url);
    allowRequest = true;
    location.href = url;
}

function windowScroll() {
    var scrollTop = document.documentElement.scrollTop; // 滚动条在文档中的高度的位置（滚出可见区域的高度）
    var scrollHeight = document.body.scrollHeight; // 所有内容的高度

    if (scrollTop + ClientHeight >= scrollHeight && allowRequest) {
        console.log("开始向后端请求数据，重新渲染页面");
        allowRequest = false;
        var params = getUrlParams();
        toNextPage(params);
    }
}

window.addEventListener("scroll", windowScroll);
