<template>
	<div id="wrapper">
        <div class="wthree_head_section">
        <h3 class="w3l_header">Welcome To <span>Our Website</span></h3>
        <p>You can upload a image in the left,and our system will detect the target in ur photo</p>
        </div>
        <form method="post" id='postdata' enctype='multipart/form-data' name="img"></form>
        <div class="detect">
          <div class="upload-image">
              <h1>待检测图片</h1>
              <div class="upload-btn" >
                  <input type="file" @change="uploadImg" id="upload">
                  <button>上传一张图像</button>
                  <button @click="delimg">删除</button>
              </div>
              <div>
                  <img :src='src' id="daijiance">
              </div>
          </div>
          <div class="prediction-image">
              <h1>检测结果</h1>
              <div class="upload-btn" >
                  <label>
                      <button @click="postimg">开始检测</button>
                  </label>
              </div>
              <div>
                  <img :src="src2">
              </div>
          </div>
        </div>
  </div>
</template>
<script src="../../jquery-1.12.4.js"></script>
<script>
  export default {
	     data(){
	          return {   
	          src: '',
            src2:'',
            file:'',
	            }
	        },
	    methods: {
        uploadImg (e) {
            let _this = this;
            let files = e.target.files[0];
            this.file = files;
            if (!e || !window.FileReader) return; // 看支持不支持FileReader
            let reader = new FileReader();
            reader.readAsDataURL(files); // 这里是最关键的一步，转换就在这里
            reader.onloadend = function () {
                _this.src = this.result;
            }
            console.log(this.src);
        },
        delimg(){
          this.src=require('../../static/images/bg.jpg'); 
          console.log(this.src);
        },
        postimg(){
          let uploadForm=document.getElementById("postdata");

          let formData = new FormData(uploadForm);
          formData.append('img',this.file);
          // var url = 'http://lab.rhzz.com.cn:8004/api/post/img';
          var url = window.location.origin+'/api/post/img';
          console.log("url:"+url)
          this.$ajax.post(url,formData)
          .then(res=>{
            console.log('result-path'+res.data.message[0]);
            // this.src2='http://lab.rhzz.com.cn:8004/result_img/'+res.data.message[0];
            this.src2=window.location.origin+'/result_img/'+res.data.message[0];
          })
          .catch(err=>{
            console.log('222222222222222 fuck！！！')
          })
        }
    },
    mounted() {

      //初始化背景图片
      this.src=require('../../static/images/bg.jpg'); 
      this.src2 = require('../../static/images/bg2.jpg');
    }
 }
</script>

<style>
.upload-btn {
    margin: auto;
}
.upload-btn input{
    position: absolute;
    width: 110px;
    height: 45px;
    opacity: 0;
    z-index: 1000;
}

.upload-btn button {
  width: 110px;
  height: 45px;
  background-color: blue;
  color: #fff;
  line-height: 30px;
  border-radius: 5px;
}
#wrapper:after {
    content: ".";
    display: block;
    height: 0;
    clear: both;
    visibility: hidden;
}
.mb_10 {
    margin-bottom: 10px; 
}
.upload-image {
    float: left;
}
.upload-image .upload-btn {
  margin-bottom: 10px;
}
.upload-image img {
    width: 500px;
    height: 500px;
    border: 1px solid #000;

}
.prediction-image {
    float: left;
    margin-left: 200px;
}
.prediction-image img {
    width: 500px;
    height: 500px;
    border: 1px solid #000;

}

.wthree_head_section {
    margin-bottom: 5em;
    border-top: 2px solid #000;
}
.w3l_header:after {
    border-top: 2px solid #89379a;
    display: block;
    width: 81px;
    content: "";
    margin: 8px auto 0;
}
.w3l_header {
    font-size: 3em;
    color: #ff7d27;
    letter-spacing: 1px;
    position: relative;
    font-weight: 600;
    text-align: center;
}
.w3l_header span {
    color: #545151;
    font-weight: 200;
}
.wthree_head_section p {
    font-size: 15px;
    text-align: center;
    margin: 20px auto;
    width: 60%;
    color: #5e5e5e;
    line-height: 1.8em;
}
.detect {
  width: 1200px;
  overflow: hidden;
  margin: 0 auto;
}
</style>