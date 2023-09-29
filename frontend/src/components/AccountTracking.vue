<template>
  <div>
    <h1>Account Tracking Testing</h1>
    <button @click="testTransactions">Test Transactions</button>
    <div v-if="additions.length > 0" class="q-py-md">
      <q-separator />
      <div class="text-bold q-pt-md" style="font-size: larger">Additions</div>
      <div v-for="(key, add) in additions" :key="key">
        <div class="row q-pt-sm">
          {{ additions[add].payer }} has added
          {{ additions[add].points }} points at {{ additions[add].timestamp }}
        </div>
        <div class="row">
          JSON: <b>{{ additions[add] }}</b>
        </div>
      </div>
    </div>

    <div v-if="spend.length > 0" class="q-py-md">
      <q-separator />
      <div class="text-bold q-pt-md" style="font-size: larger">
        Spend Points
      </div>
      {{ spend[0] }}
    </div>

    <div v-if="balance" class="q-py-md">
      <q-separator />
      <div class="text-bold q-pt-md" style="font-size: larger">
        Points Balance
      </div>
      <pre>{{ balance }}</pre>
    </div>
  </div>
</template>

<script setup="ts">
import { ref, watch, onMounted, computed } from 'vue';
import axios from 'axios';

const balance = ref(null);
const additions = ref([]);
const spend = ref([]);

const testTransactions = async () => {
  additions.value = [];
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
      additions.value.push(transaction);
      await axios.post('http://localhost:8000/add', transaction);
    }

    // Spend points
    let spend_json = { points: 5000 };
    await axios.post('http://localhost:8000/spend', spend_json);
    spend.value.push(spend_json);

    // Fetch balance
    const response = await axios.get('http://localhost:8000/balance');
    balance.value = response.data;
  } catch (error) {
    console.error('Error:', error);
  }
};
</script>
