import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import Profile from '../components/Profile/Profile.vue'
import Order from '../components/Order/Order.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,

      children: [
        {
          path: '',
          name: 'default-orders',
          components: {
            default: Order
          }
        },
        {
          path: '/orders',
          name: 'orders',
          component: Order,
        },
        {
          path: '/profile',
          name: 'profile',
          component: Profile
        },
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    }

  ]
})

export default router
