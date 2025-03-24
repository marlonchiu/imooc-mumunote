function favoriteUpdate(articleId,canceled){
	axios.post("/favorite/update_status",{
		article_id:articleId,
		canceled:canceled
	}).then((res)=>{
		if(res.data.status==3000){
			window.location.reload()
		}else{
			alert(res.data.data);
		}
	})
}

//  发布评论的return true;
var ue = UE.getEditor('feedback-container', {
		        // ... 更多配置
				shortcutMenu: false,
				elementPathEnabled : false,
				wordCount:false,
				autoHeightEnabled:false,
				// 初始化编辑器宽度,默认 1000
				initialFrameWidth:600,
				// 初始化编辑器高度,默认 320
				initialFrameHeight:150,
				serverUrl:"http://127.0.0.1:5000/feedback",
				toolbars: [
				  [
					   "insertcode",  
					    "bold",         // 加粗
					    "italic",       // 斜体
					    // "insertimage",  
						"link",
					    "insertorderedlist",   // 有序列表
					    "insertunorderedlist", // 无序列表
					    "undo",         // 撤销
					    "redo",         // 重做
					    // "emotion",             // 表情
				  ]
					  ]
		    });

// 发布评论
function addFeedback(articleId){
	var feedbackContent = ue.getContent();
	axios.post("/feedback/add",{
		article_id:articleId,
		content:feedbackContent
	}).then((res)=>{
		alert(res.data.data);
		window.location.reload();
	})
}

// 显示评论具体作者的回复输入框是否展示
var ifShowInputWrap=false;
// 存储当前打开的输入框id，用来控制关闭
var currentWriteAuthorInputId=0;
// 存储当前评论相关的信息，用来向后端发起请求，默认值都给0
var baseReplyId = 0;
var replyArticleId = 0;
var feedbackReplyId=0;
	
// 显示输入框
function showWriteAuthorInput(inputId,articleId,userId,nickname,replyId){
	baseReplyId = inputId;
	replyArticleId = articleId;
	feedbackReplyId=replyId;
	// 关闭当前已经打开的输入框
	if(currentWriteAuthorInputId != 0){
		hiddenWriteAuthorInput(currentWriteAuthorInputId);
	}
	currentWriteAuthorInputId = inputId;
	var inputWarp = document.getElementById(inputId);
	inputWarp.style.display="block";
	
}


// 隐藏输入框
function hiddenWriteAuthorInput(inputId){
	var inputWarp = document.getElementById(inputId);
	inputWarp.style.display="none";
}

// 发布回复评论的评论
function writeReply(){
	var content = document.getElementById(baseReplyId).querySelector("textarea").value;
	axios.post("/feedback/reply",{
		article_id:replyArticleId,
		content:content,
		reply_id:feedbackReplyId,
		base_reply_id:baseReplyId
	}).then((res)=>{
		alert(res.data.data);
		window.location.reload();
	})
	
}