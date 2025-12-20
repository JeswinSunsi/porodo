<template>
  <div class="bg-white min-h-screen pt-6 md:pt-20 pb-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col md:flex-row gap-8">
        
        <!-- Sidebar Filters -->
        <aside class="w-full md:w-64 flex-shrink-0" v-show="showFilters">
          <div class="sticky top-24 space-y-8">
            
            <!-- Categories Filter -->
            <div>
              <h3 class="text-lg font-bold mb-4 border-b pb-2">Categories</h3>
              <div class="space-y-2">
                <label v-for="category in categories" :key="category" class="flex items-center space-x-2 cursor-pointer group">
                  <input 
                    type="checkbox" 
                    :value="category" 
                    v-model="selectedCategories"
                    class="rounded border-gray-300 text-brand-black focus:ring-brand-black"
                  >
                  <span class="text-gray-600 group-hover:text-brand-black transition-colors">{{ category }}</span>
                </label>
              </div>
            </div>

            <!-- Price Filter -->
            <div>
              <h3 class="text-lg font-bold mb-4 border-b pb-2">Price Range</h3>
              <div class="flex items-center space-x-2">
                <input 
                  type="number" 
                  v-model.number="minPrice" 
                  placeholder="Min" 
                  class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-brand-black"
                >
                <span class="text-gray-400">-</span>
                <input 
                  type="number" 
                  v-model.number="maxPrice" 
                  placeholder="Max" 
                  class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-brand-black"
                >
              </div>
            </div>

            <!-- Clear Filters -->
            <button 
              @click="clearFilters"
              class="w-full py-2 text-sm text-gray-500 hover:text-brand-black border border-gray-200 hover:border-gray-400 rounded-sm transition-colors"
            >
              Clear All Filters
            </button>
          </div>
        </aside>

        <!-- Main Content -->
        <main class="flex-1">
          
          <!-- Header & Sorting -->
          <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4">
            <div>
              <h1 class="text-3xl font-bold text-brand-black">All Products</h1>
              <p class="text-gray-500 text-sm mt-1">Showing {{ filteredProducts.length }} results</p>
            </div>
            
            <div class="flex flex-wrap items-center gap-4">
              <button 
                @click="showFilters = !showFilters"
                class="flex items-center space-x-2 text-sm font-medium text-brand-black border border-gray-300 rounded-sm px-4 py-2 hover:bg-gray-50"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
                </svg>
                <span>{{ showFilters ? 'Hide Filters' : 'Show Filters' }}</span>
              </button>

              <div class="flex items-center space-x-2">
                <label for="sort" class="text-sm text-gray-600">Sort by:</label>
                <select 
                  id="sort" 
                  v-model="sortBy"
                  class="border-gray-300 rounded-sm text-sm focus:ring-brand-black focus:border-brand-black py-1.5 pl-3 pr-8"
                >
                  <option value="featured">Featured</option>
                  <option value="price-asc">Price: Low to High</option>
                  <option value="price-desc">Price: High to Low</option>
                  <option value="name-asc">Name: A-Z</option>
                  <option value="name-desc">Name: Z-A</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Products Grid -->
          <div v-if="loading" class="text-center py-20">
            <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-brand-black mx-auto"></div>
            <p class="mt-4 text-gray-500">Loading products...</p>
          </div>

          <div v-else-if="filteredProducts.length === 0" class="text-center py-20 bg-gray-50 rounded-lg">
            <p class="text-xl text-gray-600 mb-2">No products found</p>
            <p class="text-gray-500 mb-6">Try adjusting your filters</p>
            <button 
              @click="clearFilters"
              class="bg-brand-black text-white px-6 py-2 rounded-sm hover:bg-gray-800 transition-colors"
            >
              Clear Filters
            </button>
          </div>

          <div v-else :class="[
            'grid gap-3 md:gap-6',
            showFilters 
              ? 'grid-cols-2 lg:grid-cols-3' 
              : 'grid-cols-2 md:grid-cols-3 lg:grid-cols-4'
          ]">
            <ProductCard 
              v-for="(product, index) in filteredProducts" 
              :key="product.id" 
              :product="product"
              v-animate-on-scroll="{ delay: (index % 5) * 100 }"
            />
          </div>

        </main>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { getProducts } from '@/services/api'
import ProductCard from '@/components/ProductCard.vue'

const products = ref([])
const loading = ref(true)
const showFilters = ref(false)
const selectedCategories = ref([])
const minPrice = ref(null)
const maxPrice = ref(null)
const sortBy = ref('featured')

// Fetch products
onMounted(async () => {
  try {
    products.value = await getProducts()
  } catch (error) {
    console.error('Failed to fetch products:', error)
  } finally {
    loading.value = false
  }
})

// Extract unique categories
const categories = computed(() => {
  const cats = new Set(products.value.map(p => p.category).filter(Boolean))
  return Array.from(cats).sort()
})

// Filter and Sort Logic
const filteredProducts = computed(() => {
  let result = [...products.value]

  // Filter by Category
  if (selectedCategories.value.length > 0) {
    result = result.filter(p => selectedCategories.value.includes(p.category))
  }

  // Filter by Price
  if (minPrice.value !== null && minPrice.value !== '') {
    result = result.filter(p => p.price >= minPrice.value)
  }
  if (maxPrice.value !== null && maxPrice.value !== '') {
    result = result.filter(p => p.price <= maxPrice.value)
  }

  // Sort
  switch (sortBy.value) {
    case 'price-asc':
      result.sort((a, b) => a.price - b.price)
      break
    case 'price-desc':
      result.sort((a, b) => b.price - a.price)
      break
    case 'name-asc':
      result.sort((a, b) => a.name.localeCompare(b.name))
      break
    case 'name-desc':
      result.sort((a, b) => b.name.localeCompare(a.name))
      break
    default:
      // 'featured' - keep original order or implement specific logic
      break
  }

  return result
})

const clearFilters = () => {
  selectedCategories.value = []
  minPrice.value = null
  maxPrice.value = null
  sortBy.value = 'featured'
}
</script>
