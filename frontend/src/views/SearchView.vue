<template>
  <div class="min-h-screen bg-white pt-6 px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mx-auto">
      <div class="relative flex items-center">
        <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
          <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
          </svg>
        </div>
        <input
          ref="searchInput"
          type="text"
          v-model="searchQuery"
          @input="handleInput"
          @keydown.enter="triggerFullSearch"
          class="block w-full pl-10 pr-12 py-4 border border-gray-300 rounded-sm leading-5 bg-white placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:border-brand-accent focus:ring-1 focus:ring-brand-accent sm:text-lg transition-all duration-200"
          placeholder="Search for products..."
          autofocus
        />
        <button 
          @click="triggerFullSearch"
          class="absolute right-2 p-2 text-gray-400 hover:text-brand-accent transition-colors"
          title="Search"
        >
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5l7 7-7 7M5 5l7 7-7 7"></path>
          </svg>
        </button>
      </div>
      
      <div v-if="!searchQuery && !suggestions.length && !isFullSearch" class="mt-8">
        <img 
          src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop" 
          alt="Search Banner" 
          class="w-full h-48 object-cover rounded-lg shadow-md"
        />
      </div>

      <div v-if="loading" class="mt-8 text-center">
        <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-brand-accent"></div>
      </div>

      <!-- Suggestions List -->
      <div v-else-if="!isFullSearch && suggestions.length > 0" class="mt-4 bg-white rounded-md border border-gray-100 overflow-hidden">
        <ul class="divide-y divide-gray-100">
          <li v-for="product in suggestions" :key="product.id">
            <router-link 
              :to="`/product/${product.id}`" 
              class="block px-6 py-4 hover:bg-gray-50 transition-colors duration-150 flex items-center justify-between group"
            >
              <span class="text-gray-700 font-medium group-hover:text-brand-black">{{ product.name }}</span>
              <svg class="w-5 h-5 text-gray-400 group-hover:text-brand-accent transform group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
              </svg>
            </router-link>
          </li>
        </ul>
      </div>

      <!-- Full Search Results Grid -->
      <div v-else-if="isFullSearch && fullResults.length > 0" class="mt-8">
        <!-- Top Pagination -->
        <div v-if="totalPages > 1" class="mb-6 flex justify-center space-x-2">
          <button 
            @click="changePage(currentPage - 1)" 
            :disabled="currentPage === 1"
            class="px-4 py-2 border border-gray-300 rounded-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Previous
          </button>
          <span class="px-4 py-2 text-sm font-medium text-gray-700 flex items-center">
            Page {{ currentPage }} of {{ totalPages }}
          </span>
          <button 
            @click="changePage(currentPage + 1)" 
            :disabled="currentPage === totalPages"
            class="px-4 py-2 border border-gray-300 rounded-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Next
          </button>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <ProductCard v-for="product in fullResults" :key="product.id" :product="product" />
        </div>
        
        <!-- Bottom Pagination -->
        <div v-if="totalPages > 1" class="mt-8 flex justify-center space-x-2">
          <button 
            @click="changePage(currentPage - 1)" 
            :disabled="currentPage === 1"
            class="px-4 py-2 border border-gray-300 rounded-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Previous
          </button>
          <span class="px-4 py-2 text-sm font-medium text-gray-700 flex items-center">
            Page {{ currentPage }} of {{ totalPages }}
          </span>
          <button 
            @click="changePage(currentPage + 1)" 
            :disabled="currentPage === totalPages"
            class="px-4 py-2 border border-gray-300 rounded-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            Next
          </button>
        </div>
      </div>

      <div v-else-if="searchQuery.length >= 4 && !loading && ((isFullSearch && !fullResults.length) || (!isFullSearch && !suggestions.length))" class="mt-8 text-center text-gray-500">
        No products found for "{{ searchQuery }}"
      </div>
      
      <div v-else-if="searchQuery.length > 0 && searchQuery.length < 4" class="mt-4 text-sm text-gray-400 px-2">
        Type at least 4 characters to search...
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getSearchSuggestions, searchProducts } from '@/services/api'
import ProductCard from '@/components/ProductCard.vue'

const searchInput = ref(null)
const searchQuery = ref('')
const suggestions = ref([])
const fullResults = ref([])
const loading = ref(false)
const isFullSearch = ref(false)
const currentPage = ref(1)
const totalPages = ref(1)
let debounceTimeout = null

onMounted(() => {
  searchInput.value?.focus()
})

const fetchSuggestions = async () => {
  // Only search if query length is a multiple of 4 (4, 8, 12...)
  if (!searchQuery.value.trim() || searchQuery.value.length < 4 || searchQuery.value.length % 4 !== 0) {
    if (searchQuery.value.length < 4) suggestions.value = []
    return
  }
  
  loading.value = true
  try {
    suggestions.value = await getSearchSuggestions(searchQuery.value)
  } catch (error) {
    console.error('Suggestions failed:', error)
  } finally {
    loading.value = false
  }
}

const handleInput = () => {
  isFullSearch.value = false
  if (debounceTimeout) clearTimeout(debounceTimeout)
  debounceTimeout = setTimeout(fetchSuggestions, 300)
}

const triggerFullSearch = async () => {
  if (!searchQuery.value.trim()) return
  
  isFullSearch.value = true
  currentPage.value = 1
  await fetchFullResults()
}

const changePage = async (page) => {
  if (page < 1 || page > totalPages.value) return
  currentPage.value = page
  await fetchFullResults()
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const fetchFullResults = async () => {
  loading.value = true
  try {
    const response = await searchProducts(searchQuery.value, currentPage.value, 10)
    fullResults.value = response.items
    totalPages.value = response.pages
  } catch (error) {
    console.error('Full search failed:', error)
  } finally {
    loading.value = false
  }
}
</script>
