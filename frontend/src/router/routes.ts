import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: '',
        component: () => import('pages/AboutMePage.vue'),
      },
      {
        path: 'dogs',
        component: () => import('pages/IndexPage.vue'),
      },
      {
        path: 'receipts',
        component: () => import('pages/ReceiptsPage.vue'),
      },
      {
        path: 'account-tracking',
        component: () => import('pages/AccountTrackingPage.vue'),
      },
    ],
  },
  // Always leave this as last one, but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
