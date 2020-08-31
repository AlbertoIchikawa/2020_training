import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import HomePage from '@/components/HomePage'
import Search from '@/components/Search'
import News from '@/components/News'

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
    },
    {
      path: '/search',
      name: 'Search',
      component: Search
    },
    {
      path: '/news',
      name: 'News',
      component: News
    }
  ]
})
