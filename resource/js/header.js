function sendEmailVCode(){
	// 获取邮箱
	var targetEmail = document.querySelector("#reg-username").value;
	// 获取到发送按钮
	var sendEmailButton = document.querySelector("#send-email-vcode");
	
	// 也可以进行邮箱格式的验证
	if (!targetEmail.match(".+@.+\..+")){
		alert("邮箱格式错误");
		document.querySelector("#reg-username").focus();
		return false;
	}
	
	// 比对两次密码是否一致
	var firstPassword = document.querySelector("#reg-password").value;
	var secondPassword = document.querySelector("#reg-password1").value;
	if(firstPassword != secondPassword){
		alert("两次输入的密码不一致")
		document.querySelector("#reg-password").focus();
		return false;
	}
	// 发送邮箱验证码
	console.log(targetEmail);
	axios.post("/ecode",{
		email:targetEmail
	}).then((res)=>{
		console.log(res);
		alert("向后端发送验证码成功");
		// 设置倒计时 一般是60秒
		times=5;
		countDown(sendEmailButton,times);
		
	})
}

function countDown(sendEmailButton,times){
	sendEmailButton.disabled=true;
	sendEmailButton.innerHTML=times;
	if(times > 0){
		times = times-1;
		setTimeout(function(){
			countDown(sendEmailButton,times)
		},1000)
	}else{
		// 到了0秒了，那么一切还原
		sendEmailButton.disabled=false;
		sendEmailButton.innerHTML="发送";
	}
	
}

//  用户注册实现
function userReg(){
	// 获取邮箱
	var targetEmail = document.querySelector("#reg-username").value;
	
	// 也可以进行邮箱格式的验证
	if (!targetEmail.match(".+@.+\..+")){
		alert("邮箱格式错误");
		document.querySelector("#reg-username").focus();
		return false;
	}
	
	// 比对两次密码是否一致
	var firstPassword = document.querySelector("#reg-password").value;
	var secondPassword = document.querySelector("#reg-password1").value;
	if(firstPassword != secondPassword){
		alert("两次输入的密码不一致")
		document.querySelector("#reg-password").focus();
		return false;
	}
	
	//  开始执行用户注册
	// 获取用户输入的验证码
	var emailVCode = document.querySelector("#email-vcode").value;
	
	axios.post("/reg",{
		username:targetEmail,
		password:firstPassword,
		second_password:secondPassword,
		ecode:emailVCode
	}).then((res)=>{
		// res.data就是后端返回json
		// console.log(res.data)
		if(res.data.status==1000){
			alert(res.data.data);
			// 注册成功后要做做一个页面跳转，转到首页
			location.href="/"
		}else{
			alert(res.data.data);
		}
	})
	
	
}


// 登录功能实现
function doLogin(){
	var username = document.querySelector("#username").value;
	var password = document.querySelector("#password").value;
	var authCode = document.querySelector("#auth-code").value;
	axios.post("/login",{
		username:username,
		password:password,
		vcode:authCode
	}).then((res)=>{
		if(res.data.status==1000){
			alert(res.data.data);
			setTimeout("location.reload()",1000);
		}else{
			alert(res.data.data);
		}
	})
	
}