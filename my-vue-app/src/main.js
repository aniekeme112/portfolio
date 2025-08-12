import { createApp } from 'vue'
import App from './App.vue'
import './main.css'
import dragscroll from 'vue-dragscroll'

// Create app instance first
const app = createApp(App)

// Then use the plugin on the app instance
app.use(dragscroll)

// Mount the app
app.mount('#app')
