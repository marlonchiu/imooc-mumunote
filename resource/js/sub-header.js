function search_article(){
	var keyword = document.querySelector(".searchbox").value;
	// console.log(keyword);
	location.href="?keyword="+keyword;
}

function toWriteArticlePage(isLogin){
	console.log(isLogin);
	if(isLogin=='None' || isLogin!='true'){
		alert("您好，请登录");
		document.querySelector(".login>span:first-child").click();
	}else{
		window.open("/article/new","_blank")
	}
}