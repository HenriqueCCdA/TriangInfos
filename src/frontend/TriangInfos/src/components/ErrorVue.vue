<script setup>
import { useStore } from '@/stores/core'
const store = useStore()
</script>

<template>
  <v-alert v-if="store.msg_error" type="error" class="mt-5">
    {{ store.msg_error }}
  </v-alert>
</template>

<style scoped></style>
