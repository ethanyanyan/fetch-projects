<template>
  <q-page class="row items-center justify-evenly" style="width: 100%">
    <DogGallery />
  </q-page>
</template>

<script setup lang="ts">
import DogGallery from 'components/DogGallery.vue';
</script>

<style scoped>
.absolute-top-right {
  position: absolute;
  top: 0;
  right: 0;
}
</style>
