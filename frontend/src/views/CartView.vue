<template>
  <main class="py-8 bg-gray-50 min-h-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold text-brand-black mb-4 tracking-tight">Shopping Cart</h1>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <!-- Cart Items -->
        <div class="lg:col-span-8 space-y-4">
          
          <!-- Header -->
          <div class="hidden sm:grid grid-cols-12 text-xs font-bold text-gray-400 uppercase tracking-wider border-b border-gray-200 pb-2">
            <div class="col-span-6">Product</div>
            <div class="col-span-3 text-center">Quantity</div>
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
            v-for="item in cartStore.items" 
            :key="item.product_id"
            class="group bg-white p-3 border border-gray-100 hover:border-gray-200 transition-all duration-200"
          >
            <div class="grid grid-cols-1 sm:grid-cols-12 gap-4 items-center">
              <div class="col-span-6 flex items-center space-x-4">
                <div class="bg-gray-50 w-16 h-16 flex-shrink-0 flex items-center justify-center border border-gray-100">
                  <img :src="item.image_url" :alt="item.name" class="w-12 h-12 object-contain mix-blend-multiply">
                </div>
                <div>
                  <h3 class="font-bold text-brand-black text-sm sm:text-base">{{ item.name }}</h3>
                  <p class="text-xs text-gray-500 mb-1">Color: {{ item.selected_color || 'Default' }}</p>
                  <p class="text-sm font-medium text-brand-black sm:hidden">${{ formatPrice(item.price) }}</p>
                  <button @click="removeItem(item.product_id)" class="text-xs text-red-500 hover:text-red-600 font-medium underline mt-1">
                    Remove
                  </button>
                </div>
              </div>

              <div class="col-span-3 flex justify-center">
                <div class="flex items-center border border-gray-300 h-8 w-24">
                  <button @click="updateQuantity(item.product_id, -1)" class="w-8 h-full text-gray-600 hover:bg-gray-100 transition">-</button>
                  <input type="number" :value="item.quantity" class="w-8 h-full text-center border-none focus:ring-0 font-bold text-sm bg-transparent p-0" readonly>
                  <button @click="updateQuantity(item.product_id, 1)" class="w-8 h-full text-gray-600 hover:bg-gray-100 transition">+</button>
                </div>
              </div>

              <div class="hidden sm:block col-span-3 text-right">
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
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
                </svg>
              </div>
              <div>
                <h4 class="font-bold text-xs uppercase text-brand-black">Secure Checkout</h4>
                <p class="text-[11px]">256-bit SSL Encryption</p>
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

            <div class="mt-4 flex justify-center space-x-3 text-gray-400">
              <svg class="w-8 h-auto" viewBox="0 0 38 24" fill="currentColor"><path d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.3 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.3-3-3-3z" fill="#000"/><path d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32" fill="#fff"/><path d="M28.3 10.1H28c-.4 1-.7 1.5-1 3h1.9c-.3-1.5-.3-2.2-.6-3zm2.9 5.9h-1.7c-.1 0-.1 0-.2-.1l-.2-.9-.1-.2h-2.4c-.1 0-.2 0-.2.2l-.3.9c0 .1-.1.1-.1.1h-2.1l.2-.5L27 8.7c0-.5.3-.7.8-.7h1.5c.1 0 .2 0 .2.2l1.4 6.5c.1.4.2.7.2 1.1.1.1.1.1.1.2zm-13.4-.3l.4-1.8c.1 0 .2.1.2.1.7.3 1.4.5 2.1.4.2 0 .5-.1.7-.2.5-.2.5-.7.1-1.1-.2-.2-.5-.3-.8-.5-.4-.2-.8-.4-1.1-.7-1.2-1-.8-2.4-.1-3.1.6-.4.9-.8 1.7-.8 1.2 0 2.5 0 3.1.2h.1c-.1.6-.2 1.1-.4 1.7-.5-.2-1-.4-1.5-.4-.3 0-.6 0-.9.1-.2 0-.3.1-.4.2-.2.2-.2.5 0 .7l.5.4c.4.2.8.4 1.1.6.5.3 1 .8 1.1 1.4.2.9-.1 1.7-.9 2.3-.5.4-.7.6-1.4.6-1.4 0-2.5.1-3.4-.2-.1.2-.1.2-.2.1zm-3.5.3c.1-.7.1-.7.2-1 .5-2.2 1-4.5 1.4-6.7.1-.2.1-.3.3-.3H18c-.2 1.2-.4 2.1-.7 3.2-.3 1.5-.6 3-1 4.5 0 .2-.1.2-.3.2M5 8.2c0-.1.2-.2.3-.2h3.4c.5 0 .9.3 1 .8l.9 4.4c0 .1 0 .1.1.2 0-.1.1-.1.1-.1l2.1-5.1c-.1-.1 0-.2.1-.2h2.1c0 .1 0 .1-.1.2l-3.1 7.3c-.1.2-.1.3-.2.4-.1.1-.3 0-.5 0H9.7c-.1 0-.2 0-.2-.2L7.9 9.5c-.2-.2-.5-.5-.9-.6-.6-.3-1.7-.5-1.9-.5L5 8.2z" fill="#142688"/></svg>
              <svg class="w-8 h-auto" viewBox="0 0 38 24" fill="currentColor"><path d="M35 0H3C1.3 0 0 1.3 0 3v18c0 1.7 1.3 3 3 3h32c1.7 0 3-1.3 3-3V3c0-1.7-1.3-3-3-3z" fill="#000"/><path d="M35 1c1.1 0 2 .9 2 2v18c0 1.1-.9 2-2 2H3c-1.1 0-2-.9-2-2V3c0-1.1.9-2 2-2h32" fill="#fff"/><circle cx="15" cy="12" r="7" fill="#EB001B"/><circle cx="23" cy="12" r="7" fill="#F79E1B"/><path d="M22 12c0-2.4-1.2-4.5-3-5.7-1.8 1.3-3 3.4-3 5.7s1.2 4.5 3 5.7c1.8-1.2 3-3.3 3-5.7z" fill="#FF5F00"/></svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import { useCartStore } from '@/stores/cart'

const cartStore = useCartStore()
const discountCode = ref('')

function formatPrice(price) {
  return price.toFixed(2)
}

function updateQuantity(productId, change) {
  cartStore.updateQuantity(productId, change)
}

function removeItem(productId) {
  cartStore.removeItem(productId)
}

function applyDiscount() {
  if (discountCode.value) {
    alert(`Discount code "${discountCode.value}" applied!`)
    discountCode.value = ''
  }
}
</script>
