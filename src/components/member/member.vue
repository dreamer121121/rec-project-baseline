<template>
	<div id="wrapper">
        <h1>请上传文件</h1>
        <div class="upload-btn common mb_10" v-if="!isShow">
            <label>
                <input type="file" @change="uploadImg">
            </label>
        </div>
        <div class="img-list-item common mb_10" v-if="isShow">
            <img :src="src" class="common">
            <i class="del-img" @click="forkImage"></i>
        </div>
    </div>
</template>
<script>
      export default {
	     data(){
	          return {   
	          src: '',
              isShow:True,     
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
        },

        forkImage () {
            this.src = '';
            this.isShow = false;
        }
    }
 }
</script>
<style>

.common {
        width: 148px;
        height: 148px;
        border: 1px solid #d8d8d9;
    }
    .img-list-item {
        position: relative;
        margin: auto;
    }
    .img-list-item img {
        box-sizing: border-box;
        vertical-align: middle;
        border: 0;       
    }
    .img-list-item i.del-img {
        width: 15px;
        height: 15px;
        display: inline-block;
        background: rgba(0,0,0,.6);
        background-image: url('../../static/images/g1.jpg');
        background-size: 10px;
        background-repeat: no-repeat;
        background-position: 50%;
        position: absolute;
        top: 0;
        right: 0;
    }
    .upload-btn {
        margin: auto;
    }
    input[type="file"] {
        color: transparent;
        opacity: 0;
        width: 100%;
        height: 100%;
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
</style>