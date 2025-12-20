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
    return items.value.reduce((total, item) => {
      let itemTotal = item.price * item.quantity
      // Discount logic: 10% off if quantity >= 2
      if (item.quantity >= 2) {
        itemTotal = itemTotal * 0.9
      }
      return total + itemTotal
    }, 0)
  })

  const tax = computed(() => {
    return subtotal.value * 0.06 // 6% tax
  })

  const total = computed(() => {
    return subtotal.value + tax.value
  })

  const hasDiscount = computed(() => {
    return items.value.some(item => item.quantity >= 2)
  })

  function addItem(product, quantity = 1, selectedColor = null) {
    const wasEmpty = items.value.length === 0
    const existingItem = items.value.find(
      item => item.product_id === product.id && item.selected_color === selectedColor
    )

    if (existingItem) {
      existingItem.quantity += quantity
      if (existingItem.quantity === 2) {
        toastStore.showToast(`Discount Unlocked! 10% off ${product.name}s!`, 'success')
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
        showSpecialOffer.value = true
        toastStore.showToast(`${product.name} added! Buy 2 to save 10%!`, 'success', 5000)
      } else {
        toastStore.showToast(`${product.name} added to cart`, 'success')
      }
    }
  }

  function updateQuantity(productId, change) {
    const item = items.value.find(item => item.product_id === productId)
    if (item) {
      const oldQuantity = item.quantity
      item.quantity = Math.max(1, item.quantity + change)

      if (oldQuantity < 2 && item.quantity >= 2) {
        toastStore.showToast(`Discount Unlocked! 10% off ${item.name}s!`, 'success')
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
