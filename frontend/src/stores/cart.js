import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useToastStore } from './toast'

export const useCartStore = defineStore('cart', () => {
  const items = ref([])
  const loading = ref(false)
  const showSpecialOffer = ref(false)
  const toastStore = useToastStore()

  const itemCount = computed(() => {
    return items.value.reduce((total, item) => total + item.quantity, 0)
  })

  const subtotal = computed(() => {
    const rawTotal = items.value.reduce((total, item) => total + (item.price * item.quantity), 0)
    // Discount logic: 15% off entire order if total items >= 2
    if (itemCount.value >= 2) {
      return rawTotal * 0.85
    }
    return rawTotal
  })

  const tax = computed(() => {
    return subtotal.value * 0.06 // 6% tax
  })

  const total = computed(() => {
    return subtotal.value + tax.value
  })

  const hasDiscount = computed(() => {
    return itemCount.value >= 2
  })

  function addItem(product, quantity = 1, selectedColor = null) {
    const wasEmpty = items.value.length === 0
    const existingItem = items.value.find(
      item => item.product_id === product.id && item.selected_color === selectedColor
    )

    if (existingItem) {
      existingItem.quantity += quantity
      if (itemCount.value === 2) {
        toastStore.showToast(`Discount Unlocked! 15% off entire order!`, 'success')
      } else {
        toastStore.showToast(`${product.name} added to cart`, 'success')
      }
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

      if (wasEmpty) {
        setTimeout(() => {
          showSpecialOffer.value = true
        }, 3000)
        toastStore.showToast(`${product.name} added! Buy 2 to save 15%!`, 'success', 5000)
      } else {
        if (itemCount.value === 2) {
          toastStore.showToast(`Discount Unlocked! 15% off entire order!`, 'success')
        } else {
          toastStore.showToast(`${product.name} added to cart`, 'success')
        }
      }
    }
  }

  function updateQuantity(productId, change) {
    const item = items.value.find(item => item.product_id === productId)
    if (item) {
      const oldTotalCount = itemCount.value
      item.quantity = Math.max(1, item.quantity + change)
      const newTotalCount = items.value.reduce((t, i) => t + i.quantity, 0)

      if (oldTotalCount < 2 && newTotalCount >= 2) {
        toastStore.showToast(`Discount Unlocked! 15% off entire order!`, 'success')
      }
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
    hasDiscount,
    addItem,
    updateQuantity,
    removeItem,
    clearCart,
    showSpecialOffer
  }
})
