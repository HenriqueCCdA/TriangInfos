import { defineStore } from 'pinia'

export const useStore = defineStore('store', {
  state: () => {
    return {
      area: null,
      msg_error: null
    }
  }
})
