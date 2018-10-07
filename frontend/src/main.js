import Vue from 'vue'
// import store from '@/store'
import router from '@/router'

import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue);

import axios from 'axios'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

import VueAnalytics from 'vue-analytics'

import App from '@/App.vue'
import './registerServiceWorker'

Vue.config.productionTip = false


// more info: https://github.com/MatteoGabriele/vue-analytics
Vue.use(VueAnalytics, {
  id: process.env.VUE_APP_GOOGLE_ANALYTICS,
  router
})


new Vue({
  router,
  // store,
  render: h => h(App)
}).$mount('#app')
