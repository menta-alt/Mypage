<template>
  <div id="login">
    <div class="video_player">
      <!-- 背景视频 -->
      <video id="background_video" autoplay loop muted>
        <source src="../assets/starbroken.mp4" type="video/mp4" />
      </video>
      <!-- 蒙版 -->
      <div class="video_mask">
         <!-- 登录页面 -->
        <div class="login_interface">
          <h2>Login</h2>
          <div class="form_content">
            <div class="inputBox">
              <input type="text" placeholder="用户名" id="username" v-model="username"/>
            </div>
            <div class="inputBox">
              <input type="password" placeholder="密码" id="password" v-model="password"/>
            </div>
            <button @click="login">登录</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  name: "Login",
  data() {
    return {
      password:null,
      username:null,
      relsit:[]
    };
  },
  methods: {
    login:function(){
      var data = {
        username:this.username,
        password:this.password,
      }
      axios({
        method:'post',
        url:'http://localhost:8000/login/',
        data:data
      }).then(res=>{
        console.log(res);
        if(res.data.code=='1000'){
          this.$router.push('/homepage')
          //路由跳转
        }
        else{
          alert('用户名或密码错误')
        }
      }).catch(function(error){
        console.log(error);
      })
    }
  }
};
</script>

<style  scoped>
* {
  margin: 0px;
  padding: 0px;
}

html,
body {
  width: 100%;
  height: 100%;
  margin: 0;
  overflow: hidden;
}

#login {
  overflow: hidden;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

#background_video {
  position: absolute;
  width: 100%;
}

.video_mask {
  position: absolute;
  z-index: 1;
  width: 100%;
  height: 100%;
  background-color: #0019212c;
}

.login_interface {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 350px;
  height: 390px;
  background-color: #001921af;
  border-radius: 10px;
}

.login_interface h2 {
  margin-top: 30px;
  padding: 0;
  color: #fff;
  text-align: center;
  font-size: 30px;
}

.login_interface .form_content {
  padding: 30px;
}

.inputBox input {
  width: 100%;
  padding: 10px 0;
  font-size: 20px;
  color: #fff;
  letter-spacing: 2px; /* 字与字间的间距*/
  margin-bottom: 30px; /*输入框设置*/
  border: none;
  border-bottom: 1px solid #fff;
  outline: none;
  background: transparent;
}

.login_interface button {
  background: transparent;
  border: none;
  outline: none;
  color: #fff;
  background: #03a9f4;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 5px;
  width: 100%;
  font-size: 18px;
  margin-top: 25px;
}
</style>
