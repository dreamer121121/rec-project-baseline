<template>
        <div>
			<div class="banner-1">
			</div>
		<div class="contact-w3ls">
		<div class="container">
		<div class="agileits_heading_section">
					<h3 class="wthree_head">Contact Us</h3>
					<p class="w3l_sub_para_agile" id="Givemessage"></p>
				</div>
		<div class="inner_w3l_agile_grids-1">
			<div class="contact-w3-agile2" data-aos="flip-left">
				<div class="contact-agileits">
					<h4>Drop a Line</h4>
					
					  <div class="col-md-6 w3l_area_its">
						<div class="control-group form-group">
		                    <div class="controls">
		                        <label class="contact-p1">Full Name:</label>
		                        <input type="text" class="form-control" name="name" id="name" value="Please enter your name.">
		                        <p class="help-block"></p>
		                    </div>
		                </div>	
		                <div class="control-group form-group">
		                    <div class="controls">
		                        <label class="contact-p1">Message :</label>
	                            <textarea value="Message:" onFocus="this.value = '';" onBlur="if (this.value == '') {this.value = 'Message'; }" rows="15" id="message">Message..</textarea>
								<p class="help-block"></p>
							</div>
		                </div>
						</div>
						 <div class="col-md-6 w3l_area">
		                <div class="control-group form-group">
		                    <div class="controls">
		                        <label class="contact-p1">Email Address:</label>
		                        <input type="email" class="form-control" name="email" id="email" value="Please enter your email address.">
								<p class="help-block"></p>
							</div>
		                </div>
		                <div id="success"></div>
		                <!-- For success/fail messages -->
		                <button type="submit" class="btn btn-primary" @click='sendMessage'>Send</button>
						</div>	
		<div class="clearfix"> </div>					         
				</div>
			</div>
			<div class="clearfix"></div>
		</div>
		</div>
		</div>
		<div class="alert" v-show='ifshow'>
			<div class="alert-head"></div>
			<p>{{message}}</p>
			<button @click='OK'>确定</button>
		</div>
      </div>
</template>
<script>
      export default {
	     data(){
	          return {       
	          		back:[], 
	          		ifshow:false,
	          		message:''
	            }
	        },
	        methods:{
	        	sendMessage(){
	        		var name = document.getElementById('name').value;
	        		console.log('name:'+name)
	        		var email = document.getElementById('email').value;
	        		console.log("email:"+email)
	        		var message = document.getElementById('message').value;
	        		console.log("message:"+message)
	        		this.$ajax.get('http://192.168.1.40:8080/api/get/sendMessage?'+'nm='+name+'&email='+email+'&message='+message)
			        .then(res=>{
			            this.message = res.data.message[0];
			            this.ifshow = true;
			        })
			        .catch(err=>{
			        	this.message = "远程服务器错误 ！！！";
			        	this.ifshow = true;
			            console.log('err：'+err);
			        })
	        	},
	        	OK(){
	        		this.ifshow=false;
	        	}
	        },
	        mounted() {

				    var matha = 50;
			        var txt_list = ["Give me a message"];
			        var obj_list = [document.getElementById("Givemessage")];
			        
			        function tim(txt,obj){
			        	console.log(obj);
			            var s = txt.split("");       
			            var length = s.length;
			            var i  = 0;

			            setInterval(function(){
			                if(i<length)
			                {   var tem  = s[i++];
			                
			                    obj.innerHTML+=tem;
			                    obj.style.color=getColor();
			                    //document.body.style.backgroundColor=getColor();
			                }
			            },matha)
			        }
			        
			        function getColor(){
			            var RED=parseInt(Math.random()*255)+1;
			            var GREEN=parseInt(Math.random()*255)+1;
			            var BLUE=parseInt(Math.random()*255)+1;
			            
			            return "rgb("+RED+","+GREEN+","+BLUE+")";
			        }
			                
			        setInterval(function(){
			        		var i =0;
			        		obj_list[i].innerHTML = '';
			        		tim(txt_list[i],obj_list[i]);  

			        },5000)

	        }
      }

</script>



<style scoped>

/*弹窗样式 开始*/

.alert-head {
	background-color: blue;
	height: 30px;
}
.alert {
	height: 150px;
	width: 300px;
	background-color: #fff;
	position: absolute;
	left: 50%;
	top: 70%;
	margin-left: -150px;
	padding:0;
	border: 1px solid #000;
}

.alert p {
	margin-left: 30%;
	margin-top: 20px;
	color:#000;
	font-size: 20px;
}

.alert button {
	background-color: green;
	margin-left: 42%;
	bottom: 0;
	position:absolute;
}
/*弹窗样式 结束*/

.banner-1 {
    background: url('../../static/images/banner2.jpg') no-repeat 0px -104px;
    min-height: 300px;
    -webkit-background-size:cover;
}
.wthree_head{
	font-size:3em;
    color: #212121;
    text-transform: uppercase;
    text-align: center;
       letter-spacing: 2px;
    font-weight: bold;
}

p.w3l_sub_para_agile {
    color: #33cc99;
    letter-spacing: 5px;
    font-size: 1em;
    text-align: center;
    font-weight: 400;
    margin-top: 1.5em;
}
.w3-agileits-news-grids {
    margin: 5em 0 0 0;
}
.contact-w3ls p.contact-agile1 {
    font-size: 15px;
	letter-spacing: 1px;
    font-weight: normal;
    padding-bottom: 10px;
    line-height: 29px;
    color: #fff;
}
.contact-w3ls p.contact-agile1 strong {
    letter-spacing: 1.5px;
    color: #ffce14!important;
	font-size: 15px;
}
.contact-w3ls p.contact-agile1 a {
	color:#fff;
}
.contact-w3ls h4 {
	    font-size: 2em;
    letter-spacing: 2px;
    font-weight: normal;
    color: #333;
    margin-bottom:10px;
    font-weight: bold;
}
.contact-w3ls p.contact-agile2 {
      font-size: 14px;
    font-weight: normal;
    padding-bottom: 20px;
    line-height: 30px;
    color: #ef5734;
    letter-spacing: 3px;
}
.contact-w3ls label.contact-p1 {
        font-size: 14px;
    letter-spacing: 1px;
    font-weight: 600;
    color: #4b4d50;
    padding-bottom: 10px;
}
.form-group {
    margin-bottom: 5px;
}
.contact-w3ls p.help-block {
    color:#ff0500!important;
}
.contact-w3ls input#name,.contact-w3ls input#email,.contact-w3ls input#phone  {
	height:45px;
}
.contact-w3ls input#name, .contact-w3ls input#email, .contact-w3ls input#phone {
    font-size: 15px;
    font-weight: normal;
    color: #999;
    border-radius: 0;
    border-color: #fff;
    outline: none;
    box-shadow: none;
    border: 1px solid #ddd;
    letter-spacing: 1px;
}
.contact-w3ls button.btn.btn-primary {
    color: #fff;
    background: #33cc99;
    border: none;
    font-size: 17px;
    padding: 15px 20px;
    width: 100%;
    margin: 25px 0 8px;
    text-transform: uppercase;
    letter-spacing: 1px;
	outline:none;
	 box-shadow: none;
	 border-radius:0px;
	
}
.contact-w3ls button.btn.btn-primary:hover {
	 background: #ef5734;
    -webkit-transition: all 0.5s ease 0.01s;
    -o-transition: all 0.5s ease 0.01s;
	 -moz-transition: all 0.5s ease 0.01s;
    transition: all 0.5s ease 0.01s;
	
}
.w3l_area_its {
    padding-left: 0;
}
.control-group.form-group.has-warning ul li {
    list-style: none;
}
.control-group.form-group ul li {
    list-style: none;
}
input::-webkit-input-placeholder {
color: #111!important;
} 
input:-moz-placeholder { /* Firefox 18- */
color: #111 !important;  
} 
input::-moz-placeholder {  /* Firefox 19+ */
color: #111 !important;  
} 
input:-ms-input-placeholder {  
color: #111 !important;  
}
.footer-icons-agileinfo{
	margin-left:0!important;
}
.contact-w3-agile1 iframe {
     width: 100%;
    height:350px;
    outline: none;
    border: none;
}
.map {
    -webkit-filter: grayscale(100%);
    -moz-filter: grayscale(100%);
    -ms-filter: grayscale(100%);
    -o-filter: grayscale(100%);
    filter: grayscale(100%);
}
#contact {
    padding:6em 0;
}
/*-- //contact --*/
.contact-w3ls {
    padding: 5em 0;
}

.contact-agileits h4 {
	margin-bottom: 35px;
}
#Givemessage {
	height: 10px;
}
</style>