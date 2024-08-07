import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from '../views/LoginView.vue'
import BodegueroView from '../views/BodegueroView.vue'

const routes = [
  {
    path: '/',
    redirect: '/api/login' 
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/bodeguero',
    name: 'bodeguero',
    component: BodegueroView
  },
  {
    path: '/api/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
