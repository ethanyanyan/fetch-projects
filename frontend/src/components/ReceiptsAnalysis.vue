<template>
  <div>
    <h1 class="text-center">Receipt Forecast 2022</h1>
    <h5 class="text-center">Model trained on 2021 data</h5>
    <div v-if="isLoading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else>
      <div>
        <VueApexCharts type="line" :options="chartOptions" :series="series" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import VueApexCharts from 'vue3-apexcharts';

const apexchart = VueApexCharts;

// Reactive variables
const receipts = ref<number[]>([]);
const isLoading = ref(true);
const error = ref('');

// Function to fetch data
const fetchData = async () => {
  try {
    const response = await fetch('http://localhost:5000/get-receipt-data'); // Adjust this URL to your Flask API endpoint
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    receipts.value = await response.json();
    isLoading.value = false;

    // Update series with the fetched data
    series.value = [
      {
        name: 'Receipts 2022',
        data: receipts.value,
      },
    ];
  } catch (err) {
    isLoading.value = false;
    if (err instanceof Error) {
      error.value = err.message;
    } else {
      error.value = 'An unexpected error occurred';
    }
  }
};

const chartOptions = ref({
  chart: {
    id: 'basic-line',
  },
  xaxis: {
    categories: [
      'January',
      'February',
      'March',
      'April',
      'May',
      'June',
      'July',
      'August',
      'September',
      'October',
      'November',
      'December',
    ],
  },
});

const series = ref({
  name: 'Receipts 2022',
  data: receipts.value,
});

// Fetch data when component is mounted
onMounted(fetchData);
</script>

<style scoped>
/* You can add your styles here */
</style>
