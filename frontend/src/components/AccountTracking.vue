<template>
  <div>
    <h1>Account Tracking Testing</h1>
    <button @click="testTransactions">Test Transactions</button>
    <div v-if="balance">
      <h2>Points Balance</h2>
      <pre>{{ balance }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, computed } from 'vue';
import axios from 'axios';

const balance = ref(null);

const testTransactions = async () => {
  try {
    // Test transactions
    const transactions = [
      {
        payer: 'DANNON',
        points: 300,
        timestamp: '2022-10-31T10:00:00Z',
      },
      {
        payer: 'UNILEVER',
        points: 200,
        timestamp: '2022-10-31T11:00:00Z',
      },
      {
        payer: 'DANNON',
        points: -200,
        timestamp: '2022-10-31T15:00:00Z',
      },
      {
        payer: 'MILLER COORS',
        points: 10000,
        timestamp: '2022-11-01T14:00:00Z',
      },
      {
        payer: 'DANNON',
        points: 1000,
        timestamp: '2022-11-02T14:00:00Z',
      },
    ];

    for (const transaction of transactions) {
      await axios.post('http://localhost:5000/add', transaction);
    }

    // Spend points
    await axios.post('http://localhost:5000/spend', { points: 5000 });

    // Fetch balance
    const response = await axios.get('http://localhost:5000/balance');
    balance.value = response.data;
  } catch (error) {
    console.error('Error:', error);
  }
};
</script>
