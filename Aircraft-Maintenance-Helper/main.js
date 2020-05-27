import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false

App.mpType = 'app'

const app = new Vue({
	...App
})

Vue.prototype.image_urls =['http://ww1.sinaimg.cn/large/006tNc79gy1g5yosxatc9j30u0140qv5.jpg'];  

app.$mount()


// #ifdef APP-PLUS
var appid = plus.runtime.appid;
console.log('应用的 appid 为：' + appid);
// #endif