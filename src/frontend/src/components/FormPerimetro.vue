<script setup>
import { ref } from 'vue'
import { useStore } from '@/stores/core'
import config from '@/utils/api'

let a = ref(null)
let b = ref(null)
let c = ref(null)

async function calcular() {
  const store = useStore()

  const options = config({ a: a.value, b: b.value, c: c.value })

  store.perimetro = null
  store.msg_error = null

  try {
    const response = await fetch('http://127.0.0.1:8000/perimetro', options)

    const body = await response.json()

    if (!response.ok) {
      if (Array.isArray(body.detail)) {
        throw new Error(body.detail[0].msg)
      }
      throw new Error(body.detail.msg)
    }

    store.perimetro = parseFloat(body.perimetro).toFixed(2)
  } catch (error) {
    store.msg_error = error
  }
}
</script>

<template>
  <v-form @submit.prevent="calcular">
    <v-text-field type="number" v-model="a" placeholder="Lado a" required outlined />
    <v-text-field type="number" v-model="b" placeholder="Lado b" required />
    <v-text-field type="number" v-model="c" placeholder="Lado c" required />
    <v-btn variant="tonal" type="submit" block>Calcular</v-btn>
  </v-form>
</template>
