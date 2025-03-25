console.log('index.js文件引入了')

// // 可视区域的高度，就是我们能看见的内容的高度
// console.log(document.documentElement.clientHeight)
// // 滚动条在文档中的高度的位置(滚出可见区域的高度)
// console.log(document.documentElement.scrollTop)
// // 所有内容的高度
// console.log(document.body.scrollHeight)

var allowRequest = true // 锁定后端数据请求中的状态。 是否允许请求后端
var page = 1
var endNum = 10 // 假设初始值为10，根据实际情况调整

function getUrlParams() {
  var uri = location.search
  var final_result = {}
  // 第一次请求没有参数的时候
  if (uri === '') {
    final_result['page'] = page
    final_result['article_type'] = 'recommend'
    final_result['start_num'] = 0
    final_result['end_num'] = 10
  } else {
    if (uri.indexOf('?') != -1) {
      //  /?page=2&article_type=recommend&start_num=10&end_num=10
      params = uri.substr(1)
      params_list = params.split('&')
      for (var i = 0; i < params_list.length; i++) {
        var key = params_list[i].split('=')[0] // article_type=recommend
        var value = params_list[i].split('=')[1] // recommend
        final_result[key] = value
      }
    }

    if (uri.includes('keyword') && !uri.includes('page')) {
      final_result['page'] = 1
      final_result['start_num'] = 0
      final_result['end_num'] = 10
    }
  }
  return final_result
}

function toNextPage(params) {
  console.log(params)
  // 开始拼接url
  var url = '?'
  for (var key in params) {
    if (key === 'page') {
      params[key] = parseInt(params[key]) + 1
    }
    if (key === 'start_num') {
      params[key] = window.endNum
    }
    url += key
    url += '='
    url += params[key]
    url += '&'
  }

  // 滚动标识
  if (!url.includes('scroll')) {
    url += 'scroll=1'
  }

  // 去掉末尾的&符号
  if (url.endsWith('&')) {
    url = url.substr(0, url.length - 1)
  }

  console.log(url)
  console.log('后端数据请求完毕，同时页面渲染完毕，打开请求锁')
  allowRequest = true
  location.href = url
}

function windowScroll() {
  if (window.startNum === window.endNum) {
    document.querySelector('.load-more').innerHTML = '没有更多数据了'
    return
  }

  var clientHeight = document.documentElement.clientHeight // 可视区域的高度，就是我们能看见的内容的高度
  var scrollTop = document.documentElement.scrollTop // 滚动条在文档中的高度的位置（滚出可见区域的高度）
  var scrollHeight = document.body.scrollHeight // 所有内容的高度

  if (clientHeight + scrollTop >= scrollHeight && allowRequest) {
    console.log('开始向后端请求数据，重新渲染页面')
    allowRequest = false
    var params = getUrlParams()
    toNextPage(params)
  }
}

window.addEventListener('scroll', windowScroll)
