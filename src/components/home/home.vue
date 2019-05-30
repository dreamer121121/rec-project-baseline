<template>
        <div> 
        	<!-- 轮播图 开始-->
        	<mt-swipe :auto="4000">
        	  <mt-swipe-item><a href="#"><img src="../../static/img/timg.jpg" alt=""></a></mt-swipe-item>
			  <mt-swipe-item><a href="#"><img src="../../static/img/room.jpg" alt=""></a></mt-swipe-item>
			  <mt-swipe-item><a href="#"><img src="../../static/img/car.jpg" alt=""></a></mt-swipe-item>
			  <mt-swipe-item><a href="#"><img src="../../static/img/cat.jpg" alt=""></a></mt-swipe-item>
			</mt-swipe>
			<!-- 轮播图 结束-->


			<!-- 团队介绍 开始-->
			<div class="news" id="ourteam">
				<div class="container"> 
					<h3 class="wthree_head">Our Team</h3>
					<p class="w3l_sub_para_agile" id="motto"></p>
					<div class="w3-agileits-news-grids">
						<div class="col-md-6 news-left">
							<div class="w3-agile-news-date">
								<div class="agile-news-icon">
									<i class="fa fa-calendar" aria-hidden="true"></i>
									<p>华 旎</p>
								</div>
								<div class="agileits-line"> </div>
								<div class="agile-news-icon">
									<a href="#"><i class="fa fa-comments-o" aria-hidden="true"></i></a>
									<p>2 comments</p>
								</div>
								<div class="agileits-line"> </div>
								<div class="agile-news-icon">
									<a href="#"><i class="fa fa-thumbs-o-up" aria-hidden="true"></i></a>
									<p>3482</p>
								</div>
							</div>
							<div class="w3-agile-news-img">
								<a href="#"><img src="../../static/images/huani.jpg" alt="" /></a>
								<h4><a href="#myModal" data-toggle="modal">Pellentesque habitant </a></h4>
								<p>Donec justo ante, maximus et aliquam et, elementum ac purus. Nam eget ante ac velit laoreet sodales ut vel nibh. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
							</div>
							<div class="clearfix"> </div>
						</div>
						<div class="col-md-6 news-left">
							<div class="w3-agile-news-date">
								<div class="agile-news-icon">
									<i class="fa fa-calendar" aria-hidden="true"></i>
									<p>王 冠</p>
								</div>
								<div class="agileits-line"> </div>
								<div class="agile-news-icon">
									<a href="#"><i class="fa fa-comments-o" aria-hidden="true"></i></a>
									<p>2 comments</p>
								</div>
								<div class="agileits-line"> </div>
								<div class="agile-news-icon">
									<a href="#"><i class="fa fa-thumbs-o-up" aria-hidden="true"></i></a>
									<p>3482</p>
								</div>
							</div>
							<div class="w3-agile-news-img">
								<a href="#" data-toggle="modal"><img src="../../static/images/wangguan.jpg" alt="" /></a>
								<h4><a href="#" data-toggle="modal">Pellentesque habitant </a></h4>
								<p>Nam eget ante ac velit laoreet sodales ut vel nibh. Donec justo ante, maximus et aliquam et, elementum ac purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
							</div>
							<div class="clearfix"> </div>
						</div> 
						<div class="clearfix"> </div>
					</div>
					<div class="w3-agileits-news-grids  news-w3row2">
						<div class="col-md-6 news-left">
							<div class="w3-agile-news-date">
								<div class="agile-news-icon">
									<i class="fa fa-calendar" aria-hidden="true"></i>
									<p>陈 林</p>
								</div>
								<div class="agileits-line"> </div>
								<div class="agile-news-icon">
									<a href="#"><i class="fa fa-comments-o" aria-hidden="true"></i></a>
									<p>2 comments</p>
								</div>
								<div class="agileits-line"> </div>
								<div class="agile-news-icon">
									<a href="#"><i class="fa fa-thumbs-o-up" aria-hidden="true"></i></a>
									<p>3482</p>
								</div>
							</div>
							<div class="w3-agile-news-img">
								<a href="#" data-toggle="modal"><img src="../../static/images/chenlin.jpg" alt="" /></a>
								<h4><a href="#myModal" data-toggle="modal">Pellentesque habitant </a></h4>
								<p>Donec justo ante, maximus et aliquam et, elementum ac purus. Nam eget ante ac velit laoreet sodales ut vel nibh. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
							</div>
							<div class="clearfix"> </div>
						</div>
						<div class="col-md-6 news-left">
							<div class="w3-agile-news-date">
								<div class="agile-news-icon">
									<i class="fa fa-calendar" aria-hidden="true"></i>
									<p>夏 涛</p>
								</div>
								<div class="agileits-line"> </div>
								<div class="agile-news-icon">
									<a href="#"><i class="fa fa-comments-o" aria-hidden="true"></i></a>
									<p>2 comments</p>
								</div>
								<div class="agileits-line"> </div>
								<div class="agile-news-icon">
									<a href="#"><i class="fa fa-thumbs-o-up" aria-hidden="true"></i></a>
									<p>3482</p>
								</div>
							</div>
							<div class="w3-agile-news-img">
								<a href="#" data-toggle="modal"><img src="../../static/images/huani2.jpg" alt="" /></a>
								<h4><a href="#myModal" data-toggle="modal">Pellentesque habitant </a></h4>
								<p>Nam eget ante ac velit laoreet sodales ut vel nibh. Donec justo ante, maximus et aliquam et, elementum ac purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
							</div>
							<div class="clearfix"> </div>
						</div> 
						<div class="clearfix"> </div>
					</div>
				</div>
			</div>
			<!-- 团队介绍 结束-->

			<!-- 模型展示 开始 -->
			<div class="news" id="model">
				<div class="container">
						<h3 class="wthree_head">Model Introduction</h3>
						<p class="w3l_sub_para_agile">solidarity means strength !</p>
				</div>
			</div>
			<!-- 模型展示 结束 -->
    	</div>
</template>
<script>
      export default {
	     data(){
	          return {        
	            }
	        },
	    mounted(){
      	var matha = 50;
        var txt =  "solidarity means strength !";
        
        var a  = document.getElementById("motto");
        console.log(txt);
        
        function tim(){
        	console.log(111111)
            var s = txt.split("");
            
            var length = s.length;
            var i  = 0;
        
            setInterval(function(){
                if(i<length)
                {   var tem  = s[i++];
                
                    a.innerHTML+=tem;
                    a.style.color=getColor();
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
                
        tim();  
       		
      } //mounted等模板渲染完毕后再调用函数，created是vue实例化后立即执行因此找不到id

   }


</script>

<style scoped>

/*轮播图样式 开始*/
.mint-swipe {
		height: 550px;
		width: 100%;
		text-align: center;
		margin-top: 0px;
	}
.mint-swipe img {
		width: 100%;
		height: 550px;
	}

/*轮播图样式 结束*/


/*团队介绍样式 开始*/
.news-left {
    margin-bottom: 2em;
}
p.w3l_sub_para_agile {
    color: #33cc99;
    letter-spacing: 5px;
    font-size: 1em;
    text-align: center;
    font-weight: 400;
    margin-top: 1.5em;
}
h3.wthree_head.two {
    color: #fff;
}

.wthree_head{
	font-size:3em;
    color: #212121;
    text-transform: uppercase;
    text-align: center;
       letter-spacing: 2px;
    font-weight: bold;
}
.w3-agileits-news-grids {
    margin: 5em 0 0 0;
}
.w3-agileits-news-grids.news-w3row2 {
    margin-top: 3em;
}
.w3-agile-news-date{
    float: left;
    width: 20%;
}
.agile-news-icon{
	text-align: right;
    padding: 1em 0;
}
.w3-agile-news-img{
	float: right;
    width: 75%;
/*    height: 300px;*/
}
.agile-news-icon i.fa{
    color: #999;
    font-size: 1.5em;
	text-decoration:none;
}
.agile-news-icon p{ 
	margin:.2em 0 0 0;
}
.agileits-line {
    height: 2px;
    background:#33cc99;
    width: 30%;
    margin: 0 0 0 auto;
    top: 11px;
}
.w3-agile-news-img a img{
	width:100%;
	margin:0 0 1em 0;
}
.w3-agile-news-img h4 {
    margin: 0;
    font-size: 1.6em;
    line-height: 1.6em; 
}
.w3-agile-news-img h4 a {
    color: #ef5734;
    text-decoration: none;
    -webkit-transition: .5s all;
    -moz-transition: .5s all;
    -o-transition: .5s all;
    -ms-transition: .5s all;
    transition: .5s all;
    border-left: 3px solid #33cc99;
    padding-left: 0.8em;
}
.w3-agile-news-img h4 a:hover{
	color:#333;
}
.w3-agile-news-img p {
    font-size: 1em;
    font-weight: 400;
    color: #838383;
    line-height: 2em;
    letter-spacing: 1px;
    margin-bottom: 0em;
}
.news-right-grid a{
    color: #2f2f2f;
    font-size: 1.1em;
    font-weight: 600;
    text-decoration: none;
    line-height: 1.5em;
}
.news-right-grid a:hover{
	color:#F44336;	
}
.news-right-grid h5{
	color:#F44336;
	font-size:.9em;
	margin:.5em 0;
}
.news-right-grid p{
	color:#999999;
	font-size:.9em;
	margin:1em 0 0 0;
	line-height:1.8em;	
}
.news-right-grid:nth-child(2){
	margin:1em 0;
}
.news {
    padding: 5em 0;
}
/*团队介绍样式 结束*/
</style>