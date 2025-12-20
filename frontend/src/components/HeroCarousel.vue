<template>
  <div class="relative w-full h-[30vh] overflow-hidden bg-brand-black group">
    <div 
      v-for="(slide, index) in slides" 
      :key="index"
      :class="['absolute inset-0 transition-opacity duration-1000 ease-in-out', currentSlide === index ? 'opacity-100' : 'opacity-0']"
    >
      <img :src="slide.image" :alt="slide.alt" class="w-full h-full object-cover animate-float">
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const slides = [
  {
    image: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop',
    alt: 'Tech Banner 1'
  },
  {
    image: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=2070&auto=format&fit=crop',
    alt: 'Tech Banner 2'
  },
  {
    image: 'https://images.unsplash.com/photo-1550009158-9ebf69173e03?q=80&w=2070&auto=format&fit=crop',
    alt: 'Tech Banner 3'
  }
]

const currentSlide = ref(0)
let interval = null

onMounted(() => {
  interval = setInterval(() => {
    currentSlide.value = (currentSlide.value + 1) % slides.length
  }, 5000)
})

onUnmounted(() => {
  if (interval) clearInterval(interval)
})
</script>
