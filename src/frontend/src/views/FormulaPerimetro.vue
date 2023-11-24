<script setup>
import FormPerimetro from '@/components/FormPerimetro.vue'
import PerimetroResult from '@/components/PerimetroResult.vue'
import ErrorMsg from '@/components/ErrorMsg.vue'
import { useStore } from '@/stores/core'

const store = useStore()

store.perimetro = null
store.msg_error = null
</script>

<template>
  <v-col cols="6">
    <h1 class="title">Lados do Triangulo</h1>
    <FormPerimetro />
    <PerimetroResult />
    <ErrorMsg />
  </v-col>
</template>
