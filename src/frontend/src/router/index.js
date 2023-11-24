import { createRouter, createWebHistory } from 'vue-router'
import FormulaABC from '../views/FormulaABC'
import FormulaBH from '../views/FormulaBH'
import Home from '../views/Home'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/bh',
    name: 'bv',
    component: FormulaBH
  },
  {
    path: '/abc',
    name: 'abc',
    component: FormulaABC
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
