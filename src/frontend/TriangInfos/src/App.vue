<script setup>
import FormVue from '@/components/FormVue.vue'
import { useStore } from '@/stores/core'

const store = useStore()
</script>

<template>
  <v-container>
    <h1 class="title">Lados do Triangulo</h1>

    <FormVue />

    <div v-if="store.area" class="mt-5 expressao">Valor da area: {{ store.area }}</div>

    <v-alert v-if="store.msg_error" type="error" class="mt-5">
      {{ store.msg_error }}
    </v-alert>
  </v-container>
</template>

<style scoped>
.expressao {
  margin-bottom: 16px;
  font-size: 1.25rem;
  text-align: center;
  border-radius: 2px;
  background-color: rgb(115, 170, 152);
}

.title {
  text-align: center;
}
</style>
