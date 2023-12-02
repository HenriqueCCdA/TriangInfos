<script setup>
import { ref } from 'vue'
import { useStore } from '@/stores/core'
import config from '@/utils/api';

let b = ref(null)
let h = ref(null)

async function calcular() {
  const store = useStore()

  const options = config({ b: b.value, h: h.value })

  store.area = null
  store.msg_error = null

  try {
    const response = await fetch('http://127.0.0.1:8000/area-bh', options)

    const body = await response.json()

    if (!response.ok) {
      if (Array.isArray(body.detail)){
        throw new Error(body.detail[0].msg)
      }
      throw new Error(body.detail.msg)
    }

    store.area = parseFloat(body.area).toFixed(2)
  } catch (error) {
    store.msg_error = error
  }
}
</script>

<template>
  <v-form @submit.prevent="calcular">
    <v-text-field type="number" v-model="b" placeholder="Base" required />

    <v-text-field type="number" v-model="h" placeholder="Altura" required />
    <v-btn variant="tonal" type="submit" block>Calcular</v-btn>
  </v-form>
</template>
