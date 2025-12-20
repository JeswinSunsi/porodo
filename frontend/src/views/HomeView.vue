<template>
  <div>
    <HeroCarousel />
    <FeatureBar />
    
    <!-- Trending Products Section -->
    <section id="shop" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-12 pt-8">
      <div class="flex justify-between items-end mb-8">
        <div>
          <h2 class="text-2xl md:text-3xl font-bold mb-2">Trending Now</h2>
          <p class="text-xs md:text-sm text-gray-500">Highest rated tech this week.</p>
        </div>
        <router-link to="/products" class="inline-flex items-center text-xs md:text-sm font-semibold border-b border-brand-black pb-0.5 hover:text-brand-accent hover:border-brand-accent transition-colors group">
          View All 
          <svg class="w-4 h-4 ml-1 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
          </svg>
        </router-link>
      </div>

      <div v-if="loading" class="text-center py-12 text-gray-500">Loading products...</div>
      
      <div v-else class="grid grid-cols-2 md:grid-cols-4 gap-3 md:gap-6">
        <ProductCard 
          v-for="product in products" 
          :key="product.id" 
          :product="product"
        />
      </div>
      
      <div class="mt-8 text-center">
        <router-link to="/products" class="inline-block bg-gray-100 text-brand-black px-8 py-3 text-sm font-semibold hover:bg-gray-200 transition-colors rounded-sm hover:shadow-md">
          View All Products
        </router-link>
      </div>
    </section>

    <VRPromoSection />

    <!-- Second Trending Products Section -->
    <section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-12 pt-8">
      <div class="flex justify-between items-end mb-8">
        <div>
          <h2 class="text-2xl md:text-3xl font-bold mb-2">Trending Now</h2>
          <p class="text-xs md:text-sm text-gray-500">More top picks for you.</p>
        </div>
        <router-link to="/products" class="inline-flex items-center text-xs md:text-sm font-semibold border-b border-brand-black pb-0.5 hover:text-brand-accent hover:border-brand-accent transition-colors group">
          View All 
          <svg class="w-4 h-4 ml-1 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
          </svg>
        </router-link>
      </div>

      <div v-if="loading2" class="text-center py-12 text-gray-500">Loading products...</div>
      
      <div v-else class="grid grid-cols-2 md:grid-cols-4 gap-3 md:gap-6">
        <ProductCard 
          v-for="product in products2" 
          :key="product.id" 
          :product="product"
        />
      </div>
    </section>

    <ReviewsSection />
    <NewsletterSection />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCartStore } from '@/stores/cart'
import { getHomeProducts, getHomeTrendingProducts2 } from '@/services/api'
import HeroCarousel from '@/components/HeroCarousel.vue'
import FeatureBar from '@/components/FeatureBar.vue'
import ProductCard from '@/components/ProductCard.vue'
import VRPromoSection from '@/components/VRPromoSection.vue'
import ReviewsSection from '@/components/ReviewsSection.vue'
import NewsletterSection from '@/components/NewsletterSection.vue'

const cartStore = useCartStore()
const products = ref([])
const loading = ref(true)
const products2 = ref([])
const loading2 = ref(true)

onMounted(async () => {
  try {
    const [homeProducts, trendingProducts2] = await Promise.all([
      getHomeProducts(),
      getHomeTrendingProducts2()
    ])
    products.value = homeProducts
    products2.value = trendingProducts2
  } catch (error) {
    console.error('Failed to fetch products:', error)
  } finally {
    loading.value = false
    loading2.value = false
  }
})
</script>
