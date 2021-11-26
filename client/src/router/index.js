import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/category/:categoryName',
    name: 'Category',
    component: () => import( /* webpackChunkName: "category" */ '../views/Category.vue')
  },
  {
    path: '/product/:productID',
    name: 'CustomerProduct',
    component: () => import( /* webpackChunkName: "customerProduct" */ '../views/CustomerProduct.vue')
  },
  {
    path: '/cart',
    name: 'CustomerCart',
    component: () => import( /* webpackChunkName: "customerCart" */ '../views/CustomerCart.vue')
  },
  {
    path: '/orders',
    name: 'CustomerOrders',
    component: () => import( /* webpackChunkName: "customerOrders" */ '../views/CustomerOrders.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import( /* webpackChunkName: "login" */ '../views/Login.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import( /* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/support',
    name: 'Support',
    component: () => import( /* webpackChunkName: "support" */ '../views/Support.vue')
  },
  {
    path: '/seller',
    name: 'Seller',
    component: () => import( /* webpackChunkName: "seller" */ '../views/Seller.vue')
  },
  {
    path: '/seller/add',
    name: 'AddProduct',
    component: () => import( /* webpackChunkName: "addProduct" */ '../views/AddProduct.vue')
  },
  {
    path: '/seller/:productID',
    name: 'SellerProduct',
    component: () => import( /* webpackChunkName: "sellerProduct" */ '../views/SellerProduct.vue')
  },

  {
    path: '/account',
    name: 'Account',
    component: () => import( /* webpackChunkName: "account" */ '../views/Account.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return {
        x: 0,
        y: 0
      }
    }
  }
})

export default router