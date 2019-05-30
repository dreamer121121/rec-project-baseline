'use strict';


//引入第三方包 开始
import Vue from 'vue';
//VueRouter:引入路由对象
import VueRouter from 'vue-router';
//VueRouter:安装插件
Vue.use(VueRouter);
//Mint:引入mint-ui
import Mint from 'mint-ui';
//Mint:引入css
import 'mint-ui/lib/style.css';
//Mint:安装插件
Vue.use(Mint);


//MUI:引入mui的样式
import './static/vendor/mui/dist/css/mui.css';
//全局样式
import './static/css/global.css';
//引入bootstrap样式
import './static/css/bootstrap.css';
//引入style样式
// import './static/css/font-awesome.css';


//Axios:引入axios
import Axios from 'axios';
//挂载原型
Vue.prototype.$ajax = Axios;
//默认配置
Axios.defaults.baseURL = 'http://localhost:8000/api/get/';
//Moment:引入moment(用于格式化时间)
import Moment from 'moment';

//引入第三方包 结束




//引入自己的vue文件 开始  
import App from './app.vue';
import Home from './components/home/home.vue';
import Member from './components/member/member.vue';
import Shopcart from './components/shopcart/shopcart.vue';
import Search from './components/search/search.vue';
import NewsList from './components/news/newslist.vue';
import NavBar from './components/common/navBar.vue';
import NewsDetail from './components/news/newsDetail.vue';
import PicShare from './components/picshare/picShare.vue';
//引入自己的vue文件 结尾


//定义全局组件或过滤器开始
//定义成全局过滤器，大家都能使用
Vue.filter('convertDate',function(value){

    return Moment(value).format('YYYY-MM-DD');
})

//定义全局组件 开始
Vue.component('navBar',NavBar) //使用最好以nav-bar使用，此处注意驼峰命名


//定义全局组件或过滤器结束


//VueRouter:创建对象并配置路由规则！！！导航
let router = new VueRouter({
    linkActiveClass:'menu__item--current', //设置链接激活时使用的样式
    routes: [
        //VueRouter：配置路由规则
        { path: '/', redirect: { name: 'home' } }, //重定向
        { name: 'home', path: '/home', component: Home },//首页
        { name:'targetdetection',path:'/detection',component: Member}, //会员
        { name:'contactus',path:'/contactus',component:Shopcart},

    ]
});


//创建vue实例
new Vue({
    el: '#app',
    router,
    render: c => c(App)
})