import { defineStore } from 'pinia';
import axios from 'axios';

export const useDogsStore = defineStore('dogs', {
  state: () => ({
    selectedBreeds: [] as string[],
    breedOptions: [] as string[],
    images: [] as string[],
    isLoading: false as boolean,
  }),

  getters: {},

  actions: {
    async fetchBreeds() {
      const response = await axios.get('https://dog.ceo/api/breeds/list/all');
      this.breedOptions = Object.keys(response.data.message);
    },

    async fetchImages() {
      this.isLoading = true;
      if (this.selectedBreeds.length > 0) {
        try {
          const promises = this.selectedBreeds.map((breed) =>
            axios.get(`https://dog.ceo/api/breed/${breed}/images/random/3`)
          );
          const results = await Promise.all(promises);
          this.images = results.flatMap((result) => result.data.message);
        } catch (error) {
          console.error('Error fetching images:', error);
        }
        this.isLoading = false;
      } else {
        this.images = [];
        this.isLoading = false;
      }
    },
  },
});
