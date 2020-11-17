import Vue from 'vue'
import Router from 'vue-router'
import Login from '../view/Login.vue'
import HomePage from '../view/HomePage.vue'


Vue.use(Router)

export default new Router({
  routes: [
    {path:'/',redirect:'/login'},  //访问根页面时自动跳转到登录页面
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/homepage',
      name: 'HomePage',
      component: HomePage
    }
  ],
  mode: "history" //去掉地址栏里边的#号键
})
