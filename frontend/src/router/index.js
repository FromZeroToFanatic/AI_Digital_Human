import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // 路由级别的代码分割
      // 这会为此路由生成一个单独的代码块 (About.[hash].js)
      // 当访问该路由时才会懒加载
      component: () => import('../views/AboutView.vue'),
    },
  ],
})

export default router
