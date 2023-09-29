<template>
  <div class="q-pa-md">
    <div class="carousel-container row">
      <q-spinner v-if="isLoading" color="primary" size="2rem" />

      <q-carousel
        animated
        keep-alive
        v-model="slide"
        navigation
        infinite
        :autoplay="autoplay"
        arrows
        transition-prev="slide-right"
        transition-next="slide-left"
        @mouseenter="autoplay = false"
        @mouseleave="autoplay = true"
      >
        <q-carousel-slide
          v-for="(url, index) in images"
          :key="index"
          :name="index.toString()"
          :img-src="url"
        />
      </q-carousel>
    </div>

    <div class="row">
      <q-input
        class="q-pl-lg"
        v-model="searchTerm"
        filled
        dense
        placeholder="Search for a breed..."
      />
    </div>
    <div class="row button-title">Dog Breeds Available</div>
    <div class="q-mt-md breeds-button-group row q-pl-lg">
      <q-btn
        v-for="breed in filteredBreeds"
        :key="breed"
        outline
        rounded
        :label="breed"
        :color="selectedBreeds.includes(breed) ? 'primary' : 'black'"
        :icon="selectedBreeds.includes(breed) ? 'check' : ''"
        @click="toggleBreedSelection(breed)"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, computed } from 'vue';
import axios from 'axios';

const slide = ref(0);
const autoplay = ref(true);
const selectedBreeds = ref([]);
const breedOptions = ref([]);
const images = ref([]);
const isLoading = ref(false); // Loading state

const fetchBreeds = async () => {
  const response = await axios.get('https://dog.ceo/api/breeds/list/all');
  breedOptions.value = Object.keys(response.data.message);
};

const fetchImages = async () => {
  isLoading.value = true;
  if (selectedBreeds.value.length > 0) {
    try {
      const promises = selectedBreeds.value.map((breed) =>
        axios.get(`https://dog.ceo/api/breed/${breed}/images/random/3`)
      );
      const results = await Promise.all(promises);
      images.value = results.flatMap((result) => result.data.message);
      slide.value = 0; // reset slide when images change
    } catch (error) {
      console.error('Error fetching images:', error);
    }

    setTimeout(() => {
      isLoading.value = false;
    }, 3000);
  } else {
    images.value = [];
    isLoading.value = false;
  }
};

const toggleBreedSelection = (breed) => {
  if (selectedBreeds.value.includes(breed)) {
    selectedBreeds.value = selectedBreeds.value.filter((b) => b !== breed);
  } else {
    selectedBreeds.value.push(breed);
  }
  fetchImages();
};

const searchTerm = ref('');
const filteredBreeds = computed(() => {
  if (!searchTerm.value) return breedOptions.value;
  return breedOptions.value.filter((breed) =>
    breed.toLowerCase().includes(searchTerm.value.toLowerCase())
  );
});

watch(selectedBreeds, fetchImages);

onMounted(fetchBreeds);
</script>

<style scoped>
.breeds-button-group {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  position: relative;
  justify-content: center;
}
.button-title {
  justify-content: center;
  font-size: large;
}
.carousel-container {
  height: 500px;
  width: 100%;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

q-spinner {
  position: absolute;
  z-index: 10;
}

.q-carousel,
.q-carousel-slide {
  width: 600px;
  background-color: lightgray;
}
</style>
