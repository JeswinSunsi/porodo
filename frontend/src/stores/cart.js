import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useToastStore } from './toast'

export const useCartStore = defineStore('cart', () => {
  const items = ref([])
  const loading = ref(false)
  const toastStore = useToastStore()

  const itemCount = computed(() => {
    return items.value.reduce((total, item) => total + item.quantity, 0)
  })

  const subtotal = computed(() => {
    return items.value.reduce((total, item) => total + (item.price * item.quantity), 0)
  })

  const tax = computed(() => {
    return subtotal.value * 0.06 // 6% tax
  })

  const total = computed(() => {
    return subtotal.value + tax.value
  })

  function addItem(product, quantity = 1, selectedColor = null) {
    const existingItem = items.value.find(
      item => item.product_id === product.id && item.selected_color === selectedColor
    )

    if (existingItem) {
      existingItem.quantity += quantity
      toastStore.showToast(`${product.name} added to cart`, 'success')
    } else {
      items.value.push({
        product_id: product.id,
        name: product.name,
        price: product.price,
        quantity: quantity,
        image_url: product.image_url,
        selected_color: selectedColor,
        tag: product.badges && product.badges.length > 0 ? product.badges[0] : null
      })

      toastStore.showToast(`${product.name} added to cart`, 'success')
    }
  }

  function updateQuantity(productId, change) {
    const item = items.value.find(item => item.product_id === productId)
    if (item) {
      item.quantity = Math.max(1, item.quantity + change)
    }
  }

  function removeItem(productId) {
    const index = items.value.findIndex(item => item.product_id === productId)
    if (index > -1) {
      items.value.splice(index, 1)
    }
  }

  function clearCart() {
    items.value = []
  }

  return {
    items,
    loading,
    itemCount,
    subtotal,
    tax,
    total,
    addItem,
    updateQuantity,
    removeItem,
    clearCart
  }
})
