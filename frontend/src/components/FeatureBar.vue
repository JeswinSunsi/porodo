<template>
  <section class="py-10 bg-white border-b border-gray-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-2 md:grid-cols-4">
        <div 
          v-for="(feature, index) in features" 
          :key="index"
          class="flex flex-col items-center text-center p-6 group cursor-default"
          :class="featureBorderClass(index)"
        >
          <div class="mb-4 text-blue-900 group-hover:text-brand-accent transition-colors duration-300 transform group-hover:scale-110">
            <component :is="feature.icon" class="w-8 h-8" />
          </div>
          <h3 class="font-bold text-sm text-brand-black uppercase tracking-wide mb-1">{{ feature.title }}</h3>
          <p class="text-xs text-gray-500 font-medium">{{ feature.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { h } from 'vue'

const FastDeliveryIcon = {
  render() {
    return h('svg', { fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '1.5', d: 'M13 10V3L4 14h7v7l9-11h-7z' })
    ])
  }
}

const WarrantyIcon = {
  render() {
    return h('svg', { fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '1.5', d: 'M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z' })
    ])
  }
}

const SecurePaymentIcon = {
  render() {
    return h('svg', { fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '1.5', d: 'M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z' })
    ])
  }
}

const ReturnsIcon = {
  render() {
    return h('svg', { fill: 'none', stroke: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', { 'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'stroke-width': '1.5', d: 'M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15' })
    ])
  }
}

const features = [
  { title: 'Fast Delivery', description: 'Same day dispatch', icon: FastDeliveryIcon },
  { title: '2 Year Warranty', description: 'On all electronics', icon: WarrantyIcon },
  { title: 'Secure Payment', description: 'Encrypted transactions', icon: SecurePaymentIcon },
  { title: 'Easy Returns', description: '30-day policy', icon: ReturnsIcon }
]

function featureBorderClass(index) {
  if (index === 0) return 'border-r border-b border-gray-100 md:border-b-0'
  if (index === 1) return 'border-b border-gray-100 md:border-b-0 md:border-r'
  if (index === 2) return 'border-r border-gray-100'
  return ''
}
</script>
