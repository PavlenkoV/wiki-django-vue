import Vue from 'vue'
import VueRouter from 'vue-router'

import WikiPages from '@/components/WikiPages.vue'
import Form from '@/components/Form.vue'

const routes = [
  {path: '*', component: WikiPages},
  {path: '/new-page', component: Form},
]

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return {x: 0, y: 0} },
  mode: 'history',
  routes
})

export default router
