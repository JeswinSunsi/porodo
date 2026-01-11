<template>
  <main class="py-8 bg-gray-50 min-h-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold text-brand-black mb-4 tracking-tight">Shopping Cart</h1>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <!-- Cart Items -->
        <div class="lg:col-span-8 space-y-4">
          
          <!-- Header -->
          <div class="hidden sm:grid grid-cols-12 text-xs font-bold text-gray-400 uppercase tracking-wider border-b border-gray-200 pb-2">
            <div class="col-span-9">Product</div>
            <div class="col-span-3 text-right">Total</div>
          </div>

          <!-- Empty Cart -->
          <div v-if="cartStore.items.length === 0" class="bg-white p-8 text-center border border-gray-100">
            <p class="text-gray-500 mb-4">Your cart is empty</p>
            <router-link to="/" class="inline-block bg-brand-black text-white px-6 py-3 font-semibold hover:bg-gray-800 transition-colors">
              Continue Shopping
            </router-link>
          </div>

          <!-- Cart Items -->
          <div 
            v-for="(item, index) in cartStore.items" 
            :key="item.product_id"
            class="group bg-white p-3 border border-gray-100 hover:border-gray-200 transition-all duration-200"
            v-animate-on-scroll="{ delay: index * 100 }"
          >
            <div class="grid grid-cols-1 sm:grid-cols-12 gap-4 items-start">
              <div class="col-span-9 flex items-start space-x-4">
                <div class="bg-gray-50 w-24 h-24 flex-shrink-0 flex items-center justify-center border border-gray-100">
                  <img :src="item.image_url" :alt="item.name" class="w-20 h-20 object-contain mix-blend-multiply">
                </div>
                <div class="flex flex-col space-y-2 w-full">
                  <div class="flex justify-between items-start">
                    <h3 class="font-bold text-brand-black text-sm sm:text-base pr-2">{{ item.name }}</h3>
                    <span v-if="item.tag" class="text-[10px] font-bold px-1.5 py-0.5 uppercase bg-orange-100 text-orange-600 rounded whitespace-nowrap">{{ item.tag }}</span>
                  </div>
                  <p class="text-xs text-gray-500">Color: {{ item.selected_color || 'Default' }}</p>
                  <p class="text-sm font-medium text-brand-black sm:hidden">${{ formatPrice(item.price) }}</p>
                  
                  <div class="flex items-center border border-gray-300 h-8 w-24">
                    <button @click="updateQuantity(item.product_id, -1)" class="w-8 h-full text-gray-600 hover:bg-gray-100 transition">-</button>
                    <input type="number" :value="item.quantity" class="w-8 h-full text-center border-none focus:ring-0 font-bold text-sm bg-transparent p-0" readonly>
                    <button @click="updateQuantity(item.product_id, 1)" class="w-8 h-full text-gray-600 hover:bg-gray-100 transition">+</button>
                  </div>
                </div>
              </div>

              <div class="hidden sm:block col-span-3 text-right pt-2">
                <span class="font-bold text-lg">${{ formatPrice(item.price * item.quantity) }}</span>
              </div>
            </div>
          </div>

          <!-- Trust Badges -->
          <div v-if="cartStore.items.length > 0" class="grid grid-cols-1 md:grid-cols-3 gap-4 py-6 border-t border-b border-gray-200 mt-6">
            <div class="flex items-center space-x-3 text-gray-600">
              <div class="bg-blue-50 p-2 rounded-full text-brand-accent">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
              <div>
                <h4 class="font-bold text-xs uppercase text-brand-black">30-Day Returns</h4>
                <p class="text-[11px]">No questions asked</p>
              </div>
            </div>
            <div class="flex items-center space-x-3 text-gray-600">
              <div class="bg-blue-50 p-2 rounded-full text-brand-accent">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"></path>
                </svg>
              </div>
              <div>
                <h4 class="font-bold text-xs uppercase text-brand-black">Payment Options</h4>
                <p class="text-[11px]">Cash/Card on Delivery</p>
              </div>
            </div>
            <div class="flex items-center space-x-3 text-gray-600">
              <div class="bg-blue-50 p-2 rounded-full text-brand-accent">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.384-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path>
                </svg>
              </div>
              <div>
                <h4 class="font-bold text-xs uppercase text-brand-black">2-Year Warranty</h4>
                <p class="text-[11px]">On all electronics</p>
              </div>
            </div>
          </div>

          <div class="pt-4">
            <router-link to="/" class="flex items-center text-sm font-medium text-gray-500 hover:text-brand-black transition-colors group w-max">
              <svg class="w-4 h-4 mr-2 transform group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
              </svg>
              Continue Shopping
            </router-link>
          </div>
        </div>

        <!-- Order Summary -->
        <div class="lg:col-span-4">
          <div class="bg-white p-4 border border-gray-100 sticky top-24">
            <h2 class="text-lg font-bold text-brand-black uppercase tracking-wide mb-4">Order Summary</h2>
            
            <div class="space-y-2 text-sm text-gray-600 mb-4">
              <div class="flex justify-between">
                <span>Subtotal</span>
                <span class="font-medium text-brand-black">${{ formatPrice(cartStore.subtotal) }}</span>
              </div>
              <div class="flex justify-between">
                <span>Shipping estimate</span>
                <span class="text-brand-accent font-medium">Free</span>
              </div>
              <div class="flex justify-between">
                <span>Tax estimate</span>
                <span class="font-medium text-brand-black">${{ formatPrice(cartStore.tax) }}</span>
              </div>
            </div>

            <!-- Discount Code -->
            <div class="mb-4">
              <label class="block text-xs font-bold text-gray-500 uppercase mb-2">Discount Code</label>
              <div class="flex space-x-2">
                <input 
                  v-model="discountCode"
                  type="text" 
                  placeholder="Enter code" 
                  class="flex-1 bg-gray-50 border border-gray-200 text-sm p-2 focus:ring-1 focus:ring-brand-black focus:border-brand-black outline-none transition"
                >
                <button @click="applyDiscount" class="px-4 py-2 bg-gray-200 text-brand-black text-xs font-bold uppercase hover:bg-gray-300 transition">
                  Apply
                </button>
              </div>
            </div>

            <div class="border-t border-gray-200 pt-4 mb-6">
              <div class="flex justify-between text-lg font-bold text-brand-black">
                <span>Order Total</span>
                <span>${{ formatPrice(cartStore.total) }}</span>
              </div>
            </div>

            <button 
              @click="proceedToCheckout"
              :disabled="cartStore.items.length === 0"
              class="w-full bg-brand-black text-white h-12 font-bold uppercase tracking-wider hover:bg-gray-800 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Proceed to Checkout
            </button>

            <button class="w-full mt-3 bg-green-500 text-white hover:bg-green-600 h-12 font-bold uppercase tracking-wider transition-all duration-200 flex justify-center items-center gap-2">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z"/>
              </svg>
              Checkout via WhatsApp
            </button>

            <div class="mt-6">
              <p class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3 text-center">Payment Methods</p>
              <div class="flex justify-center items-center space-x-2 text-gray-500 bg-gray-50 py-3 rounded border border-gray-100">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"></path>
                </svg>
                <span class="text-xs font-bold uppercase">Cash / Card on Delivery</span>
              </div>
            </div>

            <div class="mt-6 border-t border-gray-200 pt-6">
              <h3 class="text-sm font-bold text-brand-black mb-2">Need Help?</h3>
              <p class="text-xs text-gray-500 mb-1">Call us: <a href="tel:+1234567890" class="text-brand-black hover:underline">+1 (234) 567-890</a></p>
              <p class="text-xs text-gray-500">Email: <a href="mailto:support@phonemate.com" class="text-brand-black hover:underline">support@phonemate.com</a></p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Removal Confirmation Modal -->
    <div v-if="showRemoveModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-brand-black/60 backdrop-blur-sm transition-all duration-300">
      <div class="bg-white rounded-lg shadow-2xl max-w-sm w-full transform transition-all border border-gray-100 relative overflow-hidden">
        <!-- Decorative top bar -->
        <div class="h-1.5 w-full bg-brand-accent"></div>
        
        <div class="p-8 text-center">
          <div class="mx-auto flex items-center justify-center h-16 w-16 rounded-full bg-brand-accent/10 mb-6 border border-brand-accent/10">
            <svg class="h-8 w-8 text-brand-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
          </div>
          
          <h3 class="text-xl font-bold text-brand-black mb-2 tracking-tight">Remove Item?</h3>
          <p class="text-sm text-gray-500 mb-6 leading-relaxed">
            Are you sure you want to remove this item from your cart?
          </p>

          <!-- Promo Box -->
          <div class="bg-gray-50 border border-dashed border-gray-300 p-5 mb-8 relative">
            <div class="absolute -top-3 left-1/2 transform -translate-x-1/2 bg-white px-3 text-[10px] font-bold text-brand-black uppercase tracking-widest border border-gray-100 shadow-sm">
              Special Offer
            </div>
            <p class="text-sm text-gray-600 leading-relaxed pt-1">
              <span class="font-bold text-brand-black">Wait!</span> Use code <span class="font-mono font-bold text-blue-500 bg-white border border-gray-200 px-2 py-1 mx-1 select-all shadow-sm">SAVE5</span> for 5% off if you complete your purchase now!
            </p>
          </div>

          <div class="space-y-3">
            <button @click="cancelRemove" class="w-full py-3.5 bg-brand-accent text-white font-bold uppercase tracking-wider hover:bg-brand-accentHover transition-all shadow-lg shadow-brand-accent/20 hover:shadow-xl rounded-md">
              Keep Item
            </button>
            <button @click="confirmRemove" class="w-full py-2 text-xs font-bold text-gray-400 uppercase tracking-wider hover:text-red-600 transition-colors rounded-md">
              Remove Item
            </button>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import { useCartStore } from '@/stores/cart'
import { useRouter } from 'vue-router'

const cartStore = useCartStore()
const router = useRouter()
const discountCode = ref('')
const showRemoveModal = ref(false)
const itemToRemoveId = ref(null)

function formatPrice(price) {
  return price.toFixed(2)
}

function updateQuantity(productId, change) {
  const item = cartStore.items.find(i => i.product_id === productId)
  if (!item) return

  if (item.quantity === 1 && change === -1) {
    itemToRemoveId.value = productId
    showRemoveModal.value = true
  } else {
    cartStore.updateQuantity(productId, change)
  }
}

function confirmRemove() {
  if (itemToRemoveId.value) {
    cartStore.removeItem(itemToRemoveId.value)
    showRemoveModal.value = false
    itemToRemoveId.value = null
  }
}

function cancelRemove() {
  showRemoveModal.value = false
  itemToRemoveId.value = null
}

function applyDiscount() {
  if (discountCode.value) {
    alert(`Discount code "${discountCode.value}" applied!`)
    discountCode.value = ''
  }
}

function proceedToCheckout() {
  router.push('/checkout')
}
</script>
