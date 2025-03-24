console.log("index.js文件引入了");

//  锁定后端数据请求中的状态。 是否允许请求后端
var allowRequest=true;
var page=1;
//  但是这种翻页的写法会有兼容性问题

function getUrlParams(){
	// ?page=2&article_type=recommend
	var uri = location.search;
	var final_result = {};
	// 第一次请求没有参数的时候
	if(uri==""){
		final_result['page']=page;
		final_result['article_type']='recommend';
		final_result['start_num']=0;
		final_result['end_num']=10;
	}else {
		if(uri.indexOf("?")!=-1){
			params = uri.substr(1);
			//  page=2&article_type=recommend
			param_list = params.split("&");
			// [page=2,article_type=recommend]
			for(var i=0;i<param_list.length;i++){
				var key = param_list[i].split("=")[0];
				var value= param_list[i].split("=")[1];
				final_result[key] = value;
			}
			
		}
		if(uri.includes("keyword") && !uri.includes("page")){
			final_result["page"]=1;
			final_result['start_num']=0;
			final_result['end_num']=10;
		}
		
	}
	
	return final_result;
}

function toNextPage(params){
	console.log(params);
	// 拼接url的过程
	var url="?";
	for(var key in params){
		if(key=="page"){
			params[key]=parseInt(params[key])+1;
		}
		if(key=="start_num"){
			params[key] = window.endNum;
		}
		//  page=2&article_type=recommend
		url += key
		url += "="
		url += params[key]
		url += "&"
	}
	if(!url.includes("scroll")){
		url += "scroll=1";
	}
	// 去掉url地址最后的&符号
	if(url.endsWith("&")){
		url = url.substr(0,url.length-1)
	}

	
	console.log(url);
	console.log("后端数据请求完毕，同时页面渲染完毕，打开请求锁");
	allowRequest=true;
	
	location.href=url;
}

function windowScroll(){
	if(window.startNum===window.endNum){
		document.querySelector(".load-more").innerHTML="没有更多数据了";
		return
	}
	// 可视区域的高度，就是我们能看见的内容的高度
	// console.log(document.documentElement.clientHeight);
	//  滚动条在文档中的高度的位置（滚出可见区域的高度）
	// console.log(document.documentElement.scrollTop);
	//  所有内容的高度
	// console.log(document.body.scrollHeight);
	var clientHeight =document.documentElement.clientHeight;
	var scrollTop=document.documentElement.scrollTop;
	var scrollHeight=document.body.scrollHeight;
	if(clientHeight+scrollTop >= scrollHeight && allowRequest){
		console.log("开始向后端请求数据，重新渲染页面");
		allowRequest=false;
		//  获取url中的参数
		var params = getUrlParams();
		toNextPage(params);
	}
}

window.addEventListener("scroll",windowScroll);
