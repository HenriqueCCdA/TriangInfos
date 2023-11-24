<script setup>
import FormAreaBH from '@/components/FormAreaBH.vue'
import AreaResult from '@/components/AreaResult.vue'
import ErrorMsg from '@/components/ErrorMsg.vue'
import { useStore } from '@/stores/core'

const store = useStore()

store.area = null
store.msg_error = null
</script>

<template>
  <v-col cols="6">
    <h1 class="title">Base e altura do Triangulo</h1>
    <FormAreaBH />
    <AreaResult />
    <ErrorMsg />
  </v-col>
</template>
