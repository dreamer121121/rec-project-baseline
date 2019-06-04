<template>
	<div id="wrapper">
        <div class="wthree_head_section">
        <h3 class="w3l_header">Welcome To <span>Our Website</span></h3>
        <p>You can upload a image in the left,and our system will detect the target in ur photo</p>
        </div>
        <div class="upload-image">
            <h1>待检测图片</h1>
            <div class="upload-btn" >
                <input type="file" @change="uploadImg" id="upload">
                <button>上传一张图像</button>
                <button @click="delimg">删除</button>
            </div>
            <div>
                <img :src="src">
            </div>
        </div>
        <div class="prediction-image">
            <h1>检测结果</h1>
            <div class="upload-btn" >
                <label>
                    <button>开始检测</button>
                </label>
            </div>
            <div>
                <img :src="src2">
            </div>
        </div>
  </div>
</template>
<script>
      export default {
	     data(){
	          return {   
	          src: '',
            src2:'',
	            }
	        },
	    methods: {
        uploadImg (e) {
            let _this = this;
            let files = e.target.files[0];
            if (!e || !window.FileReader) return; // 看支持不支持FileReader
            let reader = new FileReader();
            reader.readAsDataURL(files); // 这里是最关键的一步，转换就在这里
            reader.onloadend = function () {
                _this.src = this.result;
                _this.isShow = true;
            }
            console.log("path:"+this.src)
        },
        delimg(){
          this.src='';
          this.src=require('../../static/images/bg.jpg'); 
        }

    },
    mounted() {
      this.src=require('../../static/images/bg.jpg'); 
      this.src2 = require('../../static/images/bg2.jpg')
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
    margin-left: 400px;
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
    color: #262c38;
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
</style>