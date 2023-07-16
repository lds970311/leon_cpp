import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import * as filters from './utils/filters'
import $axios from "@/utils/ajax";
import Vant from 'vant';
import 'vant/lib/index.css';

Vue.use(Vant);


Vue.config.productionTip = false
Vue.prototype.$axios = $axios

Object.keys(filters).forEach(item => Vue.filter(item, filters[item]))
new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
