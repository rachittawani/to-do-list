import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router/index";
import 'fontawesome-free/css/all.css'
import 'fontawesome-free/css/brands.css'
import 'fontawesome-free/css/fontawesome.css'
import 'fontawesome-free/css/solid.css'
import { store, storeKey } from "./store/store";

const app = createApp(App)
app.use(router)

app.mount('#app')


