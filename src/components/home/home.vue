<template>
        <div> 
        	<!-- 轮播图 开始-->
        	<mt-swipe :auto="4000">
        	  <mt-swipe-item><a href="#"><img src="../../static/img/weilai.jpg" alt=""></a></mt-swipe-item>
			  <mt-swipe-item><a href="#"><img src="../../static/img/room.jpg" alt=""></a></mt-swipe-item>
			  <mt-swipe-item><a href="#"><img src="../../static/img/football.jpg" alt=""></a></mt-swipe-item>
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
									<p>01</p>
								</div>
								<div class="agileits-line"> </div>
								<div class="agile-news-icon">
									<a href="#"><i class="fa fa-thumbs-o-up" aria-hidden="true"></i></a>

								</div>
							</div>
							<div class="w3-agile-news-img">
								<div class="single-team-box"><img src="../../static/images/huani.jpg" alt="" width="330px" height="220px" /></div>
								<h4><a data-toggle="modal">Report writting and data collection</a></h4>
								<p>In this course design, I am mainly responsible for the writing of the report, including data collection, literature review,  report integration and format arrangement.</p>
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
									<p>02</p>
								</div>
								<div class="agileits-line"> </div>
								<div class="agile-news-icon">
									<a href="#"><i class="fa fa-thumbs-o-up" aria-hidden="true"></i></a>
								</div>
							</div>
							<div class="w3-agile-news-img">
								<div class="single-team-box"><img src="../../static/images/wangguan.jpg" alt="" width="330px" height="220px"/></div>
								<h4><a data-toggle="modal">Model training and testing</a></h4>
								<p>In this project, I was mainly responsible for model training and testing, and solved many mistakes, which made me feel a sense of achievement and thanked my teammates for their help.</p>
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
									<p>03</p>
								</div>
								<div class="agileits-line"> </div>
								<div class="agile-news-icon">
									<a href="#"><i class="fa fa-thumbs-o-up" aria-hidden="true"></i></a>
							
								</div>
							</div>
							<div class="w3-agile-news-img">
								<div class="single-team-box"><img src="../../static/images/chenlin.jpg" alt="" width="330px" height="220px"/></div>
								<h4><a data-toggle="modal">Algorithm design and improvement</a></h4>
								<p>In this engineering practice, I am mainly responsible for the design, understanding and improvement of the overall algorithm.</p>
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
									<p>04</p>
								</div>
								<div class="agileits-line"> </div>
								<div class="agile-news-icon">
									<a href="#"><i class="fa fa-thumbs-o-up" aria-hidden="true"></i></a>
							
								</div>
							</div>
							<div class="w3-agile-news-img">
								<div class="single-team-box"><img src="../../static/images/xiatao.png" alt="" width="330px" height="220px"/></div>
								<h4><a data-toggle="modal">Demonstration system design</a></h4>
								<p>In this project, I was mainly responsible for the design and implementation of the demonstration system.Thanks to my teammates and teachers, I benefited a lot from their help.</p>
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
						<p class="w3l_sub_para_agile" id="motto2"></p>
				</div>
				<div class="model-box">
					<div class='model1' ><img   src="../../static/images/faster-rcnn.jpg" alt=""/></div>
					<div class='model' ><img   src="../../static/images/faster-rcnn2.jpg" alt="" style="width:500px;" /></div>
					<div class="fixed-box1">
						<img src="../../static/images/hello.png" alt="" width="300px" height="400px">
						<p class="model-intro">
						（1）Conv layers。作为一种CNN网络目标检测的方法，Faster R-CNN首先使用一组基础conv+relu+pooling层提取图片的特征。该特征(feature maps)被共享用于后续的RPN层和全连接层。
						（2）Region Proposal Networks。RPN层是Faster R-CNN最大的亮点，RPN网络用于生成目标区域建议(region proposals)，该层通过softmax判断锚(anchors)属于前景(foreground)或者背景(background)，再利用边框回归(bounding box regression)修正锚获得精确的建议(proposals)。
						</p>
					</div>
					<div class="fixed-box2">
						<p class="model-intro">
						（3）RoI Pooling层。该层收集输入的特征(feature maps)和建议(proposals)，综合这些信息提取建议特征(proposal feature maps)，送入后续的全连接层判定目标类别。
						（4）Classification。利用建议特征（proposal feature maps）计算建议（proposal）类别，同时再次通过边框回归（bounding box regression）获得检验框的最终精确地位置。
						</p>
					</div>
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
        var txt_list = ["solidarity means strength !","make perfection more perfect !"];
        var obj_list = [document.getElementById("motto"),document.getElementById("motto2")];
        
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
        	for (var i=0;i<=1;i++){
        		obj_list[i].innerHTML = '';
        		tim(txt_list[i],obj_list[i]);  
        	}
        },5000)

       		
      } //mounted等模板渲染完毕后再调用函数，created是vue实例化后立即执行因此无法操作DOM

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
#motto {
	height: 10px;
}
#motto2 {
	height: 10px;
}
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
.ourteam img {
	width: 330px;
	height: 220px;
}
/*团队介绍样式 结束*/



/*模型介绍样式 开始*/
	.model-box {
		 height:800px;
		 position:relative;
		 overflow: hidden;
		 margin:0 auto;
		 line-height: 800px;
		 text-align: center;
	}
	.model {
		float: left;
		text-align: center;
		margin-left: 300px;
		margin-top: 200px;
	}
	.model1 {
		float: left;
		text-align: center;
		margin-left: 485px;
		margin-top: 100px;
	}
	.model1:hover {
		box-shadow:0px 5px 35px 5px rgba(6,5,49,.2);
		transition: 3s;
	}

	.model:hover {
		box-shadow:0px 5px 35px 5px rgba(6,5,49,.2);
		transition: 3s;
	}

	.model-intro {
		width: 500px;
		position: absolute;
		bottom: 460px;
		left: 200px;
		display: none;
		color: #007bff;
		transition: 3s;
	}
	.model1:hover+.model-intro {
		display: block;
		transition: 3s;
	}

	.single-team-box {
		width: 330px;
		height: 220px;
		transition: 0.5s; 
	}
	.single-team-box:hover {
		box-shadow:0px 5px 35px 5px rgba(6,5,49,.2);
	}
	.fixed-box1 {
/*		background-color: rgb(255,255,255);*/
		position: fixed;
		height: 100px;
		width: 100px;
		top: 50%;
	}
/*模型介绍样式 结束*/
</style>