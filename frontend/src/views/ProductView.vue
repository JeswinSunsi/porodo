  <template>
    <div v-if="loading" class="flex justify-center items-center h-96">
      <p class="text-gray-500">Loading product...</p>
    </div>

    <div v-else-if="!product" class="flex justify-center items-center h-96">
      <p class="text-gray-500">Product not found</p>
    </div>

    <template v-else>
      <section class="py-12 bg-white">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            
            <!-- Image Gallery -->
            <div class="space-y-4" v-animate-on-scroll>
              <div class="relative bg-gray-50 aspect-square overflow-hidden border border-gray-100 flex items-center justify-center group">
                <span v-if="product.original_price" class="absolute top-4 left-4 bg-brand-danger text-white text-xs font-bold px-3 py-1 uppercase tracking-wide z-10">
                  Save {{ discountPercent }}%
                </span>
                <img 
                  :src="mainImage" 
                  :alt="product.name"
                  class="w-3/4 object-contain transition-transform duration-500 group-hover:scale-105"
                >
              </div>
              
              <div class="flex space-x-4">
                <button 
                  v-for="(thumb, index) in thumbnails" 
                  :key="index"
                  @click="mainImage = thumb"
                  :class="['border-2 p-2 bg-gray-50 hover:bg-gray-100 transition-all h-16 w-16', mainImage === thumb ? 'border-brand-black' : 'border-transparent']"
                >
                  <img :src="thumb" class="w-full h-full object-contain">
                </button>
              </div>
            </div>

            <!-- Product Info -->
            <div class="flex flex-col h-full pt-0" v-animate-on-scroll="{ delay: 200 }">
              <div class="mb-4">
                <div class="flex items-center text-yellow-400 text-sm mb-2">★★★★★</div>
                <h1 class="text-3xl md:text-4xl font-bold text-brand-black mb-4 leading-tight">{{ product.name }}</h1>
                
                <div class="flex items-baseline space-x-3">
                  <span class="text-4xl font-bold text-brand-black">${{ formatPrice(product.price) }}</span>
                  <span v-if="product.original_price" class="text-lg text-gray-400 line-through">
                    ${{ formatPrice(product.original_price) }}
                  </span>
                </div>
              </div>

              <p class="text-gray-600 mb-8 leading-relaxed">{{ product.description }}</p>

              <!-- Color Selection -->
              <div v-if="product.colors && product.colors.length > 0" class="mb-8">
                <h3 class="text-sm font-bold text-brand-black uppercase mb-3">Select Color</h3>
                <div class="flex space-x-3">
                  <button 
                    v-for="color in product.colors" 
                    :key="color"
                    @click="selectedColor = color"
                    :class="[
                      'w-8 h-8 border-2 border-gray-300 focus:outline-none transition-all ring-offset-2',
                      selectedColor === color ? 'ring-2 ring-brand-black' : 'hover:ring-2 hover:ring-gray-400'
                    ]"
                    :style="{ backgroundColor: getColorCode(color) }"
                    :title="color"
                  ></button>
                </div>
              </div>

              <!-- Quantity & Add to Cart -->
              <div class="border-t border-b border-gray-100 py-6 mb-8">
                <div class="flex flex-row gap-4 h-12">
                  <div class="flex items-center border border-gray-300 h-full">
                    <button @click="quantity = Math.max(1, quantity - 1)" class="px-3 h-full text-gray-600 hover:bg-gray-100 hover:text-brand-black transition">-</button>
                    <input type="number" v-model.number="quantity" class="w-10 h-full text-center border-none focus:ring-0 font-bold bg-transparent" readonly>
                    <button @click="quantity++" class="px-3 h-full text-gray-600 hover:bg-gray-100 hover:text-brand-black transition">+</button>
                  </div>

                  <button 
                    @click="addToCart"
                    class="flex-1 bg-brand-black text-white px-4 h-full font-bold uppercase tracking-wider hover:bg-gray-800 transition-all hover:scale-105 transform duration-200 flex justify-center items-center gap-2"
                  >
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path>
                    </svg>
                    <span class="hidden sm:inline">Add to Cart</span>
                    <span class="sm:hidden">Add</span>
                  </button>
                </div>

                <button class="w-full mt-4 bg-green-500 text-white hover:bg-green-600 h-12 font-bold uppercase tracking-wider transition-all duration-200 flex justify-center items-center gap-2">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/>
                  </svg>
                  Order via WhatsApp
                </button>
                              <div class="mt-6 flex flex-wrap justify-center items-center gap-6 text-gray-400 opacity-60 grayscale hover:grayscale-0 transition-all duration-300">
                <div class="flex items-center gap-1">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
                  </svg>
                  <span class="text-[10px] font-bold uppercase tracking-thinner">COD available</span>
                </div>
                <div class="flex items-center gap-1">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path>
                  </svg>
                  <span class="text-[10px] font-bold uppercase tracking-thinner">Buyer Protection</span>
                </div>
                <div class="flex items-center gap-1">
                  <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
                  </svg>
                  <span class="text-[10px] font-bold uppercase tracking-thinner">Easy Returns</span>
                </div>
              </div>
              </div>

              <!-- Features -->
              <div class="grid grid-cols-2 gap-4">
                <div class="flex items-center space-x-3 p-3 bg-gray-50">
                  <svg class="w-6 h-6 text-brand-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                  </svg>
                  <div>
                    <p class="text-xs font-bold text-brand-black uppercase">Fast Delivery</p>
                    <p class="text-xs text-gray-500">In 24-48 Hours</p>
                  </div>
                </div>
                <div class="flex items-center space-x-3 p-3 bg-gray-50">
                  <svg class="w-6 h-6 text-brand-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
                  </svg>
                  <div>
                    <p class="text-xs font-bold text-brand-black uppercase">Warranty</p>
                    <p class="text-xs text-gray-500">2 Year Official</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Specifications -->
      <section v-if="product.specs" class="py-10 bg-gray-50 border-t border-gray-200" v-animate-on-scroll>
        <div class="max-w-4xl mx-auto px-4">
          <h3 class="text-lg font-bold mb-6 text-center uppercase tracking-wide">Technical Specifications</h3>
          <div class="bg-white p-6 md:p-8 border border-gray-100">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm">
              <div class="space-y-4">
                <div 
                  v-for="(value, key, index) in leftSpecs" 
                  :key="key"
                  class="flex justify-between border-b border-gray-100 pb-2"
                >
                  <span class="text-gray-500">{{ key }}</span>
                  <span class="font-semibold">{{ value }}</span>
                </div>
              </div>
              <div class="space-y-4">
                <div 
                  v-for="(value, key, index) in rightSpecs" 
                  :key="key"
                  class="flex justify-between border-b border-gray-100 pb-2"
                >
                  <span class="text-gray-500">{{ key }}</span>
                  <span class="font-semibold">{{ value }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
          <section id="shop" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-12 pt-8">
        <div class="flex justify-between items-end mb-8" v-animate-on-scroll>
          <div>
            <h2 class="text-2xl md:text-3xl font-bold mb-2">Trending Now</h2>
            <p class="text-xs md:text-sm text-gray-500">Highest rated Phone this week.</p>
          </div>
          <router-link to="/products" class="inline-flex items-center text-xs md:text-sm font-semibold border-b border-brand-black pb-0.5 hover:text-brand-accent hover:border-brand-accent transition-colors group">
            View All 
            <svg class="w-4 h-4 ml-1 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
            </svg>
          </router-link>
        </div>

        <div v-if="trendingLoading" class="text-center py-12 text-gray-500">Loading products...</div>
        
        <div v-else class="grid grid-cols-2 md:grid-cols-4 gap-3 md:gap-6">
          <ProductCard 
            v-for="(product, index) in products" 
            :key="product.id" 
            :product="product"
            v-animate-on-scroll="{ delay: index * 100 }"
          />
        </div>
        
        <div class="mt-8 text-center" v-animate-on-scroll>
          <router-link to="/products" class="inline-block bg-gray-100 text-brand-black px-8 py-3 text-sm font-semibold hover:bg-gray-200 transition-colors rounded-sm hover:shadow-md">
            View All Products
          </router-link>
        </div>
      </section>
    </template>
  </template>

  <script setup>
  import { ref, computed, onMounted, watch } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { useCartStore } from '@/stores/cart'
  import { getProduct, getHomeProducts } from '@/services/api'
  import ProductCard from '@/components/ProductCard.vue'

  const route = useRoute()
  const router = useRouter()
  const cartStore = useCartStore()

  const product = ref(null)
  const loading = ref(true)
  const products = ref([])
  const trendingLoading = ref(true)
  const quantity = ref(1)
  const selectedColor = ref(null)
  const mainImage = ref('')

  const thumbnails = [
    'https://images.unsplash.com/photo-1592750475338-74b7b21085ab?q=80&w=200&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?q=80&w=200&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1583394838336-acd977736f90?q=80&w=200&auto=format&fit=crop',
    'https://images.unsplash.com/photo-1484704849700-f032a568e944?q=80&w=200&auto=format&fit=crop'
  ]

  const discountPercent = computed(() => {
    if (!product.value?.original_price) return 0
    return Math.round((1 - product.value.price / product.value.original_price) * 100)
  })

  const leftSpecs = computed(() => {
    if (!product.value?.specs) return {}
    const entries = Object.entries(product.value.specs)
    const half = Math.ceil(entries.length / 2)
    return Object.fromEntries(entries.slice(0, half))
  })

  const rightSpecs = computed(() => {
    if (!product.value?.specs) return {}
    const entries = Object.entries(product.value.specs)
    const half = Math.ceil(entries.length / 2)
    return Object.fromEntries(entries.slice(half))
  })

  async function fetchTrendingProducts() {
    trendingLoading.value = true
    try {
      products.value = await getHomeProducts()
    } catch (error) {
      console.error('Failed to fetch trending products:', error)
    } finally {
      trendingLoading.value = false
    }
  }

  async function fetchProduct() {
    loading.value = true
    try {
      product.value = await getProduct(route.params.id)
      mainImage.value = product.value.image_url
      if (product.value.colors?.length > 0) {
        selectedColor.value = product.value.colors[0]
      }
    } catch (error) {
      console.error('Failed to fetch product:', error)
      product.value = null
    } finally {
      loading.value = false
    }
  }

  function formatPrice(price) {
    return price.toFixed(2)
  }

  function getColorCode(colorName) {
    const colors = {
      'Black': '#000000',
      'Gray': '#9ca3af',
      'Blue': '#1e3a8a',
      'White': '#ffffff',
      'Silver': '#c0c0c0'
    }
    return colors[colorName] || '#000000'
  }

  function addToCart() {
    cartStore.addItem(product.value, quantity.value, selectedColor.value)
    router.push('/cart')
  }

  onMounted(() => {
    fetchProduct()
    fetchTrendingProducts()
  })

  watch(() => route.params.id, fetchProduct)
  </script>
