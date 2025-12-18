<template>
  <router-link 
    :to="`/product/${product.id}`" 
    class="group border border-gray-200 p-3 md:p-4 bg-white hover:border-brand-black transition-all duration-300 hover:shadow-xl hover:-translate-y-1 block"
  >
    <div class="relative bg-gray-50 aspect-square mb-3 flex items-center justify-center overflow-hidden">
      <span 
        v-if="product.badges && product.badges.length > 0" 
        :class="badgeClass"
        class="absolute top-2 left-2 text-[10px] font-bold px-1.5 py-0.5 uppercase z-10"
      >
        {{ product.badges[0] }}
      </span>
      <img 
        :src="product.image_url" 
        :alt="product.name"
        class="w-3/4 object-contain group-hover:scale-110 transition-transform duration-500"
      >
    </div>
    <div class="space-y-1">
      <h3 class="font-semibold text-sm md:text-base leading-tight truncate">{{ product.name }}</h3>
      <p class="text-[10px] md:text-xs text-gray-500 truncate">{{ product.short_description }}</p>
      <div class="flex items-center justify-between pt-2">
        <span class="font-bold text-sm md:text-lg text-brand-black">${{ formatPrice(product.price) }}</span>
        <button 
          @click.prevent="addToCart"
          class="bg-white border border-gray-200 text-brand-black p-1.5 rounded-full hover:bg-brand-black hover:text-white hover:border-brand-black transition-colors"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
          </svg>
        </button>
      </div>
    </div>
  </router-link>
</template>

<script setup>
import { computed } from 'vue'
import { useCartStore } from '@/stores/cart'

const props = defineProps({
  product: {
    type: Object,
    required: true
  }
})

const cartStore = useCartStore()

const badgeClass = computed(() => {
  const badge = props.product.badges?.[0]?.toLowerCase()
  if (badge === 'sale') return 'bg-brand-black text-white'
  if (badge === 'hot') return 'bg-brand-danger text-white'
  if (badge === 'refurb') return 'bg-gray-100 text-gray-600 border border-gray-200'
  return 'bg-brand-black text-white'
})

function formatPrice(price) {
  return price.toLocaleString('en-US', { minimumFractionDigits: 0, maximumFractionDigits: 0 })
}

function addToCart() {
  cartStore.addItem(props.product)
}
</script>
