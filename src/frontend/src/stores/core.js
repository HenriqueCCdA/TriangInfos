import { defineStore } from 'pinia'

export const useStore = defineStore('store', {
  state: () => {
    return {
      area: null,
      perimetro: null,
      msg_error: null
    }
  }
})
