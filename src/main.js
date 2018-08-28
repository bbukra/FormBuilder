import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

const routes = [
{ path: '/', component: require('./components/Forms-List.vue').default },
{ path: '/Form-Builder', component: require('./components/Form-Builder.vue').default }
]

const router = new VueRouter({
  routes, 
  mode: 'history'
})

var data = { a: 1 }
new Vue({
  el: '#app',
  data: data,
  template: '<App/>',
  components: { App },
  router
}).$mount('#app')//mount the router on the app