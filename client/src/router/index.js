import Vue from 'vue';
import VueRouter from 'vue-router';
import GetProjects from '../components/GetProjects.vue';

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'GetProjects',
      component: GetProjects,
    },
  ],
});

export default router;
