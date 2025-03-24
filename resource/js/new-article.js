var ue = UE.getEditor('editor', {
		        // ... 更多配置
				shortcutMenu: false,
				elementPathEnabled : false,
				wordCount:false,
				autoHeightEnabled:false,
				// 初始化编辑器宽度,默认 1000
				initialFrameWidth:800,
				// 初始化编辑器高度,默认 320
				initialFrameHeight:800,
				serverUrl:"http://127.0.0.1:5000/feedback",
				toolbars: [
				  [
					   "insertcode",  
					    "bold",         // 加粗
					    "italic",       // 斜体
					    "insertimage",  
						"link",
					    "insertorderedlist",   // 有序列表
					    "insertunorderedlist", // 无序列表
					    "undo",         // 撤销
					    "redo",         // 重做
					    "emotion",             // 表情
				  ]
					  ]
		    });
			
			
// 控制投递的栏目菜单栏的显示与隐藏
var isArticleLabelListShow=true;

function showArticleLabelList(){
	var labelList = document.querySelector(".article-label-list");
	var labelValue = document.querySelector(".article-label-value");
	if(isArticleLabelListShow==true){
		labelList.style.display="block";
		isArticleLabelListShow=false;
		labelValue.style.boxShadow="0 0 0 4px rgb(28 31 33 / 10%)";
	}else{
		labelList.style.display="none";
		isArticleLabelListShow=true;
		labelValue.style.boxShadow="";
	}
}

var isArticleTypeListShow=true;
function showArticleTypeList(){
	var typeList = document.querySelector(".article-type-list");
	var typeValue = document.querySelector(".article-type-value");
	if(isArticleTypeListShow==true){
		typeList.style.display="block";
		isArticleTypeListShow=false;
		typeValue.style.boxShadow="0 0 0 4px rgb(28 31 33 / 10%)";
	}else{
		typeList.style.display="none";
		isArticleTypeListShow=true;
		typeValue.style.boxShadow="";
	}
}
var isDraftedListShow=true;
function showDraftedList(){
	var draftedList = document.querySelector(".drafted-info");
	if(isDraftedListShow==true){
		draftedList.style.display="block";
		isDraftedListShow=false;
	}else{
		draftedList.style.display="none";
		isDraftedListShow=true;
	}
}


// 声明存储文章内容的变量
var articleContent;
var articleTitle;
var articleId=-1;
// 选择投递的栏目
var label_name=""
var article_type=""
// 创建文章或者是文章的草稿存储
function createArticle(drafted){
	//  获取文章的标题
	articleTitle = document.querySelector(".article-header").value;
	// 获取文章的内容
	articleContent = ue.getContent();
	
	// 向后端发送请求
	axios.post("/article/save",{
		// 这是草稿存储的逻辑
		title:articleTitle,
		article_content:articleContent,
		article_id:articleId,
		drafted:drafted,
		// 下边的几个字段是正式发布的时候才用
		label_name:label_name,
		article_type:article_type,
		article_tag:articleTag
	}).then((res)=>{
		articleId = res.data.article_id
		alert(res.data.data)
		// 如果是文章发布的逻辑，那么我们需要默认跳转到文章详情页面
		if(drafted==1){
			setTimeout(function(){
				location.href="/detail?article_id="+articleId;
			},1000);
		}
	})
}

// 添加事件监听，上传文章头部图片
// 是页面加载完毕后立即执行。要不然就会报找不到addEnevtListener的错误
window.onload=function(){
	var articleHeaderImage = document.querySelector("#xFile");
	articleHeaderImage.addEventListener("change",function(event){
		// 拿到用户上传的图片
		var articleHeaderImageFile = event.target.files[0];
		// 构造请求的参数
		var formData = new FormData();
		// 添加一个上传文件的key，要和后台接收的key相同，后台要用到这个key然后获取到接收的文件
		formData.append("header-image-file",articleHeaderImageFile);
		formData.append("article_id",articleId);
		// 把数据提交给后台
		axios.post("/article/upload/article_header_image",formData).then((res)=>{
			var image = document.querySelector(".upload-header-image label img");
			image.setAttribute("src",res.data.url)
			image.style.width="130px";
			image.style.height="130px";
		})
		
	})
}
//  文章头图随机图片
function randomHeaderImage(){
	var formData = new FormData();
	formData.append("article_id",articleId);
	// 把数据提交给后台
	axios.post("/article/random/header/image",formData).then((res)=>{
		var image = document.querySelector(".upload-header-image label img");
		image.setAttribute("src",res.data.url)
		image.style.width="130px";
		image.style.height="130px";
	})
}

// 选择投递的栏目
function selectLabelName(label_name_args,label_value_args){
	label_name = label_name_args;
	var firstChildSpan = document.querySelector(".article-label-value>span:first-child");
	firstChildSpan.innerHTML = label_value_args;
	var lis = document.querySelectorAll(".article-label-list>div>li");
	// 注意这里的for循环，如果我们使用了in那么就会多遍历出来一些属性，因为in会把lis当成对象来遍历
	// 那么就把其它属性也循环出来了
	for(i of lis.keys()){
		// console.log(i);
		lis[i].className="no-selected";
		if(lis[i].getAttribute("data-label-type") == label_name_args){
			lis[i].className="selected";
		}
	}
	
}

// 选择文章的类型
function selectArticleType(article_type_name_args,article_type_value_args){
	article_type = article_type_name_args;
	var firstChildSpan = document.querySelector(".article-type-value>span:first-child");
	firstChildSpan.innerHTML = article_type_value_args;
	var lis = document.querySelectorAll(".article-type-list>div>li");
	// 注意这里的for循环，如果我们使用了in那么就会多遍历出来一些属性，因为in会把lis当成对象来遍历
	// 那么就把其它属性也循环出来了
	for(i of lis.keys()){
		// console.log(i);
		lis[i].className="no-selected";
		if(lis[i].getAttribute("data-article-type") == article_type_name_args){
			lis[i].className="selected";
		}
	}
}

// 添加文章标签
var articleTag=""; //这个就是存储到数据库里的样子
var finalTagsList=[]; //这个是用来做中间转换用的
var tagNum=0;
function addTag(tagName){
	if(finalTagsList.length==3){
		return false;
	}
	// 我们需要定位到change-tags，给它添加子元素
	var changeTags = document.querySelector(".change-tags");
	var childElement = "span";
	var mySpanTag = document.createElement(childElement);
	// <span>Python</span>
	mySpanTag.innerHTML=tagName;
	mySpanTag.setAttribute("data-tag",tagName);
	mySpanTag.addEventListener("click",deleteTag);
	finalTagsList.push(tagName);
	articleTag = finalTagsList.join(",");
	changeTags.appendChild(mySpanTag);
	// 如果标签数量等于了3个，那么就删除掉input标签
	if(finalTagsList.length==3){
		var tagInputElement = document.querySelector(".article-tag-value>input");
		document.querySelector(".article-tag-value").removeChild(tagInputElement)
	}
	// 修改前端标签的数量显示
	document.querySelector(".tag-num").innerHTML=finalTagsList.length;
}


function deleteTag(){
	var changeTags = document.querySelector(".change-tags");
	var changeSonTags = document.querySelectorAll(".change-tags>span");
	for(var i of changeSonTags.keys()){
		if(changeSonTags[i].getAttribute("data-tag")==this.innerHTML){
			changeTags.removeChild(changeSonTags[i]);
		}
		// 删除完之后，我们需要对数组中的元素进行删除，然后再改变最终的字符串
		for(i in finalTagsList){
			if(finalTagsList[i]==this.innerHTML){
				finalTagsList.splice(i,1);
				articleTag=finalTagsList.join(",");
			}
		}
	}
	/* 如果长度小于3，我们需要判断孩子里边有没有input标签，如果没有，那么就添加 */
	//  <input class="fl" type="text" placeholder="选择下列标签">
	var tagInputElement = document.querySelector(".article-tag-value>input");
	if(tagInputElement==null){
		var articleTagValue=document.querySelector(".article-tag-value");
		tagInputElement = document.createElement("input");
		tagInputElement.className = "fl";
		tagInputElement.type="text";
		tagInputElement.setAttribute("placeholder","选择下列标签")
		articleTagValue.appendChild(tagInputElement);
		// 手动绑定一下input监听事件
		addInputEventListenerFunc();
	}
	
	// 修改前端的标签数量
	document.querySelector(".tag-num").innerHTML=finalTagsList.length;
	
}

// 修复一下input标签删除后，再重建没有监听input事件的bug
var addInputEventListenerFunc;

window.onload=function(){
	function addInputEventListener(){
		var article_tags = window.globalArticleTags;
		console.log(article_tags);
		var inputElement = document.querySelector(".article-tag-value>input");
		inputElement.addEventListener("input",function(event){
			var resetArticleTagList=[];
			var tag_value = inputElement.value;
			console.log(tag_value);
			// 动态渲染，重新筛选标签
			for(var i in article_tags){
				if(article_tags[i].search(tag_value)!=-1){
					resetArticleTagList.push(article_tags[i]);
				}
			}
			/* 再次渲染页面 */
			var articleTagListElement = document.querySelector(".article-tag-list");
			// 先删除掉所有的孩子，然后再用新的列表内容进行标签渲染
			articleTagListElement.innerHTML="";
			// <span onclick="addTag('{{article_tag}}')">{{article_tag}}</span>
			for(var i in resetArticleTagList){
				var element = document.createElement("span");
				element.setAttribute("onclick","addTag('"+resetArticleTagList[i]+"')")
				element.innerHTML=resetArticleTagList[i];
				articleTagListElement.appendChild(element);
			}
		})
	}
	addInputEventListenerFunc = addInputEventListener;
	addInputEventListenerFunc();
}

// 在ue中显示我的草稿内容
function toDrafted(draftedId){
	/* 一个是把title的值给放上去 */
	var articleHeader = document.querySelector(".article-header");
	
	// 把article_contetn的内容放上去
	axios.post("/article/drafted",{
		id:draftedId
	}).then((res)=>{
		articleHeader.value = res.data.data.title;
		ue.body.innerHTML=res.data.data.article_content;
		// 千万不要忘记我们此时编辑的是哪个草稿
		articleId = res.data.data.id;
	})
	
}