import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GameView from '../views/GameView.vue'
import ChallengeView from '../views/ChallengeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/game',
      name: 'game',
      component: GameView
    },
    {
      path: '/challenge/:challengeId',
      name: 'challenge',
      component: ChallengeView
    }
  ]
})

export default router