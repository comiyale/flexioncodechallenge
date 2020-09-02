import Vue from "vue";
import Axios from "axios";
import App from "./views/App.vue";

import "bootstrap/dist/css/bootstrap.css";
import "./assets/css/global.css";

Vue.config.productionTip = false;
Vue.prototype.$http = Axios;

new Vue({
	render: (h) => h(App),
}).$mount("#app");
