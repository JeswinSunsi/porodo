<template>
  <section class="py-12 border-b border-gray-100">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
      <h2 class="text-2xl font-bold mb-12">What our customers say</h2>
      <div v-if="loading" class="text-gray-500">Loading reviews...</div>
      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div 
          v-for="(review, index) in reviews" 
          :key="index"
          class="bg-gray-50 p-8 border border-gray-100 hover:shadow-lg transition-shadow duration-300"
        >
          <div class="flex justify-center text-yellow-400 mb-4">
            {{ '★'.repeat(review.rating) }}
          </div>
          <p class="text-gray-600 mb-6 italic">"{{ review.comment }}"</p>
          <div class="font-bold text-sm text-brand-black">— {{ review.author }}, {{ review.role }}</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getReviews } from '@/services/api'

const reviews = ref([])
const loading = ref(true)

onMounted(async () => {
  try {
    reviews.value = await getReviews()
  } catch (error) {
    console.error('Failed to fetch reviews:', error)
  } finally {
    loading.value = false
  }
})
</script>
