<template>
  <div class="relative w-full h-[30vh] overflow-hidden bg-brand-black group">
    <div 
      v-for="(slide, index) in slides" 
      :key="index"
      :class="['absolute inset-0 transition-opacity duration-1000 ease-in-out', currentSlide === index ? 'opacity-100' : 'opacity-0']"
    >
      <img :src="slide.image" :alt="slide.alt" class="w-full h-full object-cover">
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const slides = [
  {
    image: 'https://i.ibb.co/r2YvjkFh/22.png',
    alt: 'Phone Banner 1'
  },
  {
    image: 'https://i.ibb.co/v6r7XwSK/Yann.png',
    alt: 'Phone Banner 2'
  },
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
