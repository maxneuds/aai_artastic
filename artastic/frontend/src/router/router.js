import Vue from "vue";
import Router from "vue-router";
import Home from '@/views/Home'
import Contact from '@/views/Contact'


Vue.use(Router);
const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/contact',
        name: 'contact',
        component: Contact
    }
];
let router = new Router({
    routes,
    mode: 'history'
})

export default router;