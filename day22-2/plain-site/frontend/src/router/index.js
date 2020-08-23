import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import HomePage from '@/components/HomePage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/homepage',
      name: 'HomePage',
      component: HomePage
    }
  ]
})
