<template>
  <q-layout>
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title> Dog Breeds App </q-toolbar-title>

        <q-btn flat dense @click="goToHomePage">By Ethan Yan</q-btn>
      </q-toolbar>
      <q-tabs align="left">
        <q-route-tab to="/" label="About Me" />
        <q-route-tab to="/dogs" label="Dog Breeds" />
        <q-route-tab to="/receipts" label="Receipt Predictions" />
        <q-route-tab to="/account-tracking" label="Account Tracking" />
      </q-tabs>
    </q-header>

    <q-page-container style="width: 100%">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();

const goToHomePage = () => {
  router.push('/');
};
</script>

<style scoped>
.dark-header {
  background-color: #333;
}
</style>
