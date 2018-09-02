import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
Vue.use(VueRouter)
Vue.use(VueResource)

const routes = [
{ path: '/', component: require('./components/Forms-List.vue').default },
{ path: '/Form-Builder', component: require('./components/Form-Builder.vue').default },
{ path: '/Submit-Page/:formId', component: require('./components/Submit-Page.vue').default },
{ path: '/Submissions-Page/:formId', component: require('./components/Submissions-Page.vue').default }
]

const router = new VueRouter({
  routes, 
  mode: 'history'
})


new Vue({
  el: '#app',
  template: '<App/>',
  components: { App },
  router
}).$mount('#app')