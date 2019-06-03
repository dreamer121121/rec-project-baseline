<template>
	<div id="wrapper">
        <div class="upload-image">
            <h1>待检测图片</h1>
            <div class="upload-btn" >
                <label>
                    <button type="file" @change="uploadImg">上传</button>
                    <button>删除</button>
                </label>
            </div>
            <div>
                <img :src="src">
<!--                 <i class="del-img" @click="forkImage"></i> -->
            </div>
        </div>
        <div class="prediction-image">
            <h1>检测结果</h1>
            <div class="upload-btn" >
                <label>
                    <button type="file" @change="uploadImg">上传</button>
                    <button>删除</button>
                </label>
            </div>
            <div>
                <img :src="src">
<!--                 <i class="del-img" @click="forkImage"></i> -->
            </div>
        </div>
    </div>
</template>
<script>
      export default {
	     data(){
	          return {   
	          src: '',
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

.upload-btn {
    margin: auto;
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
.upload-image img {
    width: 500px;
    height: 500px;
}
.prediction-image {
    float: left;
    margin-left: 200px;
}
.prediction-image img {
    width: 500px;
    height: 500px;

}
</style>