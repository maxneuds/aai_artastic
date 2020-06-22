import Vue from 'vue'
import router from './router/router'
import store from './store/store'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import TextHighlight from "vue-text-highlight";

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  store,
  TextHighlight,
  render: h => h(App)
}).$mount('#app')
