<template>
        <div>
       		<!--  头部内容 开始-->
		<div class="banner-top">
		        <div class="header">
		        	<div class="logo">
					<a href="https://www.buaa.edu.cn/"><img src="./static/images/logo.png" alt=""></a>
					</div>
					<div class="contact">
						<div class="agileinfo-phone">
							<p><i class="fa fa-volume-control-phone" aria-hidden="true"></i> 联系电话：1 661 986 4868</p>
						</div>
						<div class="agileinfo-phone agileinfo-map">
							<p><i class="fa fa-map-marker" aria-hidden="true"></i> 联系地址：北京市海淀区学院路37号.</p>
						</div>
						<div class="clearfix"> </div>
					</div>
			</div>
	       <div class="w3_navigation">
			<div class="container">
				<nav class="navbar navbar-default">
					<div class="navbar-header navbar-left">
						<h1>
						<router-link class="navbar-brand" :to="{name:'home'}"> Target Detection </router-link>
						</h1>
					</div>
					<!-- Collect the nav links, forms, and other content for toggling -->
					<div class="collapse navbar-collapse navbar-right" id="bs-example-navbar-collapse-1">
						<nav class="menu menu--iris">
							<ul class="nav navbar-nav menu__list">
								<li class="menu__item ">
								<router-link class="menu__link" :to="{name:'home'}">Home</router-link>
								</li>
								<li class="menu__item">
								<a href="javascript:;" class="menu__link" @click="goAnchor('ourteam')">我们的团队</a>
								</li>
								<li class="menu__item">
								<a href="javascript:;" class="menu__link" @click="goAnchor('model')">我们的模型</a>
								</li>

								<li class="menu__item">
									<router-link :to="{name:'targetdetection'}" class="menu__link" >目标检测展示</router-link>
								</li>
								<li class="menu__item">
								<router-link :to="{name:'contactus'}" class="menu__link">联系我们</router-link>
								</li>
							</ul>
						</nav>
					</div>
				</nav>
			</div>
			</div>
		</div>
        	<!--  头部内容 结束-->
			
			<!-- 主页内容 开始 -->
        	<router-view class="content"></router-view>
        	<!-- 主页内容 结束 -->

      		<!-- 底部内容 开始-->
                <div class="footer">
                    <div class=" text-center wow fadeIn" data-wow-delay="0.4s">
                        <p class="copyright">Copyright &copy; 2015 - Designed By Veronika Poljakova &amp; Developed by Imransdesign.- More Templates <a href="http://www.cssmoban.com/" target="_blank" title="模板之家">模板之家</a> - Collect from <a href="http://www.cssmoban.com/" title="网页模板" target="_blank">网页模板</a></p>
                    </div>
                </div>

			<!-- 底部内容 结束-->
        </div>
</template>
<script>
      export default {
	     data(){
	          return {        
	            }
	        },
	        methods:{
	        	goAnchor (selector) {
	        		document.getElementById(selector).scrollIntoView();
	        }
      }
  }
</script>



<style scoped>
.mui-bar {
	margin: 0 auto;
}

/*头部样式 开始*/
.content-header {
	float: left;
	margin-left: 500;
	text-align: center;
	color: #fff;
}
.contact {
	float: left;
	left: 400px;
	margin-top: 30px;
	margin-left: 66px;
}
.logo {
	float: left;
}
.w3_navigation {
		padding: 0.5em 0;
	}
.navbar {
    margin-bottom: 0;
}.navbar-default {
    background: none;
    border: none;
}
.navbar {
    margin-bottom: 0;
}
.navbar-collapse {
    padding: 0;
}
.navbar-right {
    margin-right: 0;
}
.navbar-default .navbar-nav > .active > a, .navbar-default .navbar-nav > .active > a:hover, .navbar-default .navbar-nav > .active > a:focus {
    color:#fff;
    background:none;
}
.navbar-default .navbar-nav > li > a {
    font-weight: 500;
    letter-spacing: 1px;
}
.navbar-nav > li > a {
    margin: 0;
    padding:0 1.5em;
    text-transform: uppercase;
}
.navbar-default .navbar-nav > li > a:hover{
    color:#33cc99;
}
.navbar-default .navbar-nav > li > a:focus {
    color: #33cc99;
	outline:none;
}
nav.navbar.navbar-default {
    background: none;
    padding:1em 0 0 0;
}
.navbar-default .navbar-nav > .open > a, .navbar-default .navbar-nav > .open > a:hover, .navbar-default .navbar-nav > .open > a:focus {
    color:#33cc99;
    background: none;
}
.navbar-default .navbar-nav > li > a {
    color: #000;
}
.navbar-default .navbar-nav  > .active.open > a:focus {
	background: #0a9dbd;
	color: #fff;
}
.navbar-default .navbar-brand,.navbar-default .navbar-brand:hover, .navbar-default .navbar-brand:focus {
    color: #ef5734;
}
.tlinks{text-indent:-9999px;height:0;line-height:0;font-size:0;overflow:hidden;}
.navbar-brand {
    padding: 0;
    font-size:1em;
    text-transform: uppercase;
    letter-spacing:1px;
    line-height:35px;
    position: relative;
    font-weight: 700;
}
.navbar-brand span {
    color: #82b9e2;
}
p.logo_w3l_agile_caption {
    text-transform:uppercase;
    letter-spacing:9px;
    font-size: 11px;
    color: #8c908c;
    font-family: 'Open Sans', sans-serif;
    font-weight: 600;
    text-align: center;
}
.agile_short_dropdown {
    border-radius: 0;
    background: #ffffff;
    text-align: center;
	padding:0;
	border: none;
}
.agile_short_dropdown li a{
	text-transform:uppercase;
	color:#212121;
	font-size:13px;
	font-weight:600;
	padding: .8em 0;
}
.agile_short_dropdown > li > a:hover{
    color: #fff;
    text-decoration: none;
   background-color: #ef5734;
}
.header {
    padding: 1em 0em;
    background:#021523;
    overflow: hidden;
}
.w3-header-bottom {
	background: #212121;
    padding: 0.8em 2em;
}
.agileinfo-phone {
	float: left;
    margin: .5em 2em 0 0;
}
.agileinfo-phone p {
	color: #FFFFFF;
    font-size: .9em;
    margin: 0;
    font-weight: 600;
}
.agileinfo-map{
	margin-right:0;
}
.search-grid {
    float: right;
    width: 18%;
    border: 1px solid #fff;
}
.search-grid input[type="text"] {
    display: inline-block;
    background: none;
    border: none;
    border-right: solid 1px #ffffff;
    width: 84%;
    padding: .5em;
    outline: none;
    font-size: .9em;
    color: #FFFFFF;
}
.big-dog::-webkit-input-placeholder {
	color: #FFFFFF !important;
}
.search-grid i.fa.fa-paper-plane-o{
    color: #FFFFFF !important;
    font-size: 1.2em !important;
}
.search-grid button.btn1 {
    color: #ffffff;
    font-size: .9em;
	padding: 6px 6px;
    border: none;
	outline:none;
    text-align: center;
    text-decoration: none;
    background: none;
    transition: 0.5s all;
    -webkit-transition: 0.5s all;
    -moz-transition: 0.5s all;
    -o-transition: 0.5s all;
    -ms-transition: 0.5s all;
}
.search button:hover{
    border: solid 1px #212121;
    background: #212121;
}
.search button:hover i.fa.fa-paper-plane-o{
    color: #FFFFFF !important;
}
/*-- nav-effect --*/
.menu__list {
	position: relative;
	margin:0.5em 0 0;
}

.menu__item {
	display: block;
	margin: 1em 0;
}

.menu__link {
	font-size: 1.05em;
	font-weight: bold;
	display: block;
	padding: 1em;
	cursor: pointer;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	-webkit-touch-callout: none;
	-khtml-user-select: none;
	-webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
/* Iris */
.menu--iris .menu__item {
	margin:0 0.5em;
}

.menu--iris .menu__link {
	position: relative;
	text-align: center;
	-webkit-transition: color 0.3s;
	transition: color 0.3s;
}

.menu--iris .menu__link:hover,
.menu--iris .menu__link:focus {
	color: #929292;
}

.menu--iris .menu__item--current .menu__link,.menu__link:hover {
	color:#33cc99;
}

.menu--iris .menu__link::before,
.menu--iris .menu__link::after {
	content: '';
	position: absolute;
	width: 10px;
	height: 10px;
	opacity: 0;
	border: 2px solid #33cc99;
	-webkit-transition: -webkit-transform 0.3s, opacity 0.3s;
	transition: transform 0.3s, opacity 0.3s;
	-webkit-transition-timing-function: cubic-bezier(0.17, 0.67, 0.05, 1.29);
	transition-timing-function: cubic-bezier(0.17, 0.67, 0.05, 1.29);
}

.menu--iris .menu__link::before {
	top: 0;
	left: 0;
	border-width: 2px 0 0 2px;
	-webkit-transform: translate3d(10px, 10px, 0);
	transform: translate3d(10px, 10px, 0);
}

.menu--iris .menu__link::after {
	right: 0;
	bottom: 0;
	border-width: 0 2px 2px 0;
	-webkit-transform: translate3d(-10px, -10px, 0);
	transform: translate3d(-10px, -10px, 0);
}

.menu--iris .menu__item--current .menu__link::before,
.menu--iris .menu__item--current .menu__link::after,.menu__link:hover::before,.menu__link:hover::after {
	opacity: 1;
	-webkit-transform: translate3d(0, 0, 0);
	transform: translate3d(0, 0, 0);
}
.dropdown-menu {
    position: absolute;
    top: 226%;
    left: 0;
    z-index: 1000;
    display: none;
}
/*-- //nav-effect --*/
/*-- banner-text --*/ 
.header-w3layouts{
    position: absolute;
    top: 0;
    z-index: 99;
    text-align: center;
    left: 0;
    width: 100%;
}
.agileits-banner-info h3 {
    color: #fff;
    font-size: 4em;
    margin: 0.1em 0 0.2em 0;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 700;
	text-shadow: 1px 1px 2px rgb(12, 12, 12);
	-webkit-text-shadow: 1px 1px 2px rgb(12, 12, 12);
	-o-text-shadow: 1px 1px 2px rgb(12, 12, 12);
	-moz-text-shadow: 1px 1px 2px rgb(12, 12, 12);
	
}
.agileits-banner-info h3 span{
	    background: #2529d8;
    padding: 0 15px;
}
.agileits-banner-info {
    text-align: center;
    padding: 18em 0 0em;
}
.agileits-banner-info p {
    color: #e2dfdf;
    font-size: 1em;
    line-height: 2.2em;
    letter-spacing: 2px;
    font-weight: 500;
    width: 49%;
	margin: 0 auto;
    text-align:  center;
}
.agileits_w3layouts_more{
	position:relative;
}
.agileits_w3layouts_more a{
	    font-size: 17px;
    color: #fff;
    text-decoration: none;
    text-transform: uppercase;
    letter-spacing: 4px;
    position: relative;
}

.agileits-banner-info span {
	background:#ef5734;
    padding: 0.5em 2em;
    color: #fff;
    font-size: 1.1em;
    padding: 5px 2em;
    text-transform: uppercase;
    letter-spacing: 2px;
}

nav.navbar.navbar-default {
    padding: 0em 0 0 0;
}
.navbar-brand {
    height: 34px;
}
.navbar {
    min-height: 39px;
}
.navbar-brand {
    line-height: 39px;
}
.navbar-left {
	margin-bottom: 25px;
}
.navbar-right {
	margin-top: 25px;
}
/*头部样式 结束*/



/*底部样式 结束*/
.copyrights{
	text-indent:-9999px;
	height:0;
	line-height:0;
	font-size:0;
	overflow:hidden;
}
.footer {
	background-color: #2d3035;
	height: 50px;
	position: fixed;
	bottom: 0;
	width: 100%;
	line-height: 50px;
}
.footer p {
	color: #fff;
}
/*底部样式 结束*/
</style>