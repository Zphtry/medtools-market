import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/_Main'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Main
    },

    // {
    //   path: '/',
    //   name: 'Hello',
    //   component: Hello
    // }
  ]
})
