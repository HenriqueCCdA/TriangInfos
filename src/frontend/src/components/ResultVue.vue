<script setup>
import { useStore } from '@/stores/core'
const store = useStore()
</script>

<template>
  <div v-if="store.area" class="mt-5 expressao">Valor da area: {{ store.area }}</div>
</template>

<style scoped>
.expressao {
  margin-bottom: 16px;
  font-size: 1.25rem;
  text-align: center;
  border-radius: 2px;
  background-color: rgb(115, 170, 152);
}
</style>
