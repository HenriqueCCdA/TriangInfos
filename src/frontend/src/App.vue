<script setup>
import FormVue from '@/components/FormVue.vue'
import ResultVue from './components/ResultVue.vue'
import ErrorVue from './components/ErrorVue.vue'
</script>

<template>
  <v-container>
    <h1 class="title">Lados do Triangulo</h1>

    <FormVue />
    <ResultVue />
    <ErrorVue />
  </v-container>
</template>

<style scoped>
.title {
  text-align: center;
}
</style>
