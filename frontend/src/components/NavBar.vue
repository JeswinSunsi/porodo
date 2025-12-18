<template>
  <nav class="sticky top-0 z-40 bg-white/90 backdrop-blur-md border-b border-gray-100 transition-all duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <router-link to="/" class="flex-shrink-0 flex items-center cursor-pointer group">
          <span class="text-2xl font-bold tracking-tighter group-hover:opacity-80 transition-opacity">
            Tech<span class="text-brand-accent">Nova</span>.
          </span>
        </router-link>

        <div class="hidden md:flex space-x-8">
          <router-link to="/products" class="text-gray-600 hover:text-brand-black font-medium transition-colors hover:scale-105 transform duration-200">All Products</router-link>
          <a href="#" class="text-gray-600 hover:text-brand-black font-medium transition-colors hover:scale-105 transform duration-200">Smartphones</a>
          <a href="#" class="text-gray-600 hover:text-brand-black font-medium transition-colors hover:scale-105 transform duration-200">Laptops</a>
          <a href="#" class="text-gray-600 hover:text-brand-black font-medium transition-colors hover:scale-105 transform duration-200">Audio</a>
          <a href="#" class="text-red-600 font-medium transition-colors hover:scale-105 transform duration-200">Sale</a>
        </div>

        <div class="flex items-center space-x-6">
          <button class="text-gray-500 hover:text-brand-black transition-transform hover:scale-110 duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
            </svg>
          </button>
          <router-link to="/cart" class="relative text-gray-500 hover:text-brand-black group transition-transform hover:scale-110 duration-200">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path>
            </svg>
            <span v-if="cartCount > 0" class="absolute -top-1 -right-1 bg-brand-accent text-white text-[10px] font-bold px-1.5 py-0.5 rounded-full animate-bounce">
              {{ cartCount }}
            </span>
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
defineProps({
  cartCount: {
    type: Number,
    default: 0
  }
})
</script>
