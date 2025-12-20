import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useToastStore = defineStore('toast', () => {
  const toasts = ref([])
  let nextId = 0

  function showToast(msg, toastType = 'success', duration = 3000) {
    const id = nextId++
    const toast = {
      id,
      message: msg,
      type: toastType
    }
    
    toasts.value.push(toast)
    
    // Limit to 3 toasts
    if (toasts.value.length > 3) {
      toasts.value.shift()
    }

    setTimeout(() => {
      removeToast(id)
    }, duration)
  }

  function removeToast(id) {
    const index = toasts.value.findIndex(t => t.id === id)
    if (index > -1) {
      toasts.value.splice(index, 1)
    }
  }

  return {
    toasts,
    showToast,
    removeToast
  }
})
