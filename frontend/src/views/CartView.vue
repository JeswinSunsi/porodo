<template>
  <main class="py-8 bg-gray-50 min-h-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold text-brand-black mb-4 tracking-tight">Shopping Cart</h1>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">

        <!-- Cart Items Column -->
        <div class="lg:col-span-8 space-y-4">

          <!-- Header -->
          <div
            class="hidden sm:grid grid-cols-12 text-xs font-bold text-gray-400 uppercase tracking-wider border-b border-gray-200 pb-2">
            <div class="col-span-9">Product</div>
            <div class="col-span-3 text-right">Total</div>
          </div>

          <!-- Empty Cart State -->
          <div v-if="cartStore.items.length === 0" class="bg-white p-8 text-center border border-gray-100">
            <p class="text-gray-500 mb-4">Your cart is empty</p>
            <router-link to="/"
              class="inline-block bg-brand-black text-white px-6 py-3 font-semibold hover:bg-gray-800 transition-colors">
              Continue Shopping
            </router-link>
          </div>

          <!-- Cart Items List -->
          <div v-for="(item, index) in cartStore.items" :key="item.product_id"
            class="group bg-white p-4 border border-gray-100 hover:border-gray-200 transition-all duration-200 shadow-sm hover:shadow-md">
            <div class="grid grid-cols-1 sm:grid-cols-12 gap-6 items-start">
              <div class="col-span-9 flex items-start space-x-6">
                <router-link :to="`/product/${item.product_id}`"
                  class="bg-brand-gray w-24 h-24 flex-shrink-0 flex items-center justify-center border border-gray-50 hover:opacity-80 transition-opacity">
                  <img :src="item.image_url" :alt="item.name" class="w-20 h-20 object-contain mix-blend-multiply">
                </router-link>
                <div class="flex flex-col space-y-3 w-full">
                  <div class="flex justify-between items-start">
                    <router-link :to="`/product/${item.product_id}`">
                      <h3
                        class="font-black text-brand-black text-sm sm:text-base pr-2 hover:text-brand-accent transition-colors uppercase tracking-tight">
                        {{ item.name }}</h3>
                    </router-link>
                    <span v-if="item.tag"
                      class="text-[10px] font-black px-2 py-0.5 uppercase bg-brand-black text-white rounded-none tracking-widest">{{
                        item.tag }}</span>
                  </div>
                  <div class="flex gap-4">
                    <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest">Color: <span class="text-brand-black">{{ item.selected_color || 'Default' }}</span></p>
                    <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest sm:hidden">Unit: <span class="text-brand-black font-black">${{ formatPrice(item.price) }}</span></p>
                  </div>

                  <div class="flex items-center border border-gray-200 h-10 w-28 bg-brand-gray">
                    <button @click="updateQuantity(item.product_id, -1)"
                      class="w-10 h-full text-brand-black hover:bg-gray-200 transition font-bold">-</button>
                    <input type="number" :value="item.quantity"
                      class="w-8 h-full text-center border-none focus:ring-0 font-black text-xs bg-transparent p-0"
                      readonly>
                    <button @click="updateQuantity(item.product_id, 1)"
                      class="w-10 h-full text-brand-black hover:bg-gray-200 transition font-bold">+</button>
                  </div>
                </div>
              </div>

              <div class="hidden sm:block col-span-3 text-right pt-2">
                <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-1">Total</p>
                <span class="font-black text-xl text-brand-black tracking-tight">${{ formatPrice(item.price * item.quantity) }}</span>
              </div>
            </div>
          </div>

          <!-- Trust Badges -->
          <div v-if="cartStore.items.length > 0"
            class="grid grid-cols-1 md:grid-cols-3 gap-4 py-6 border-t border-b border-gray-200 mt-6">
            <div class="flex items-center space-x-3 text-gray-600">
              <div class="bg-blue-50 p-2 rounded-full text-brand-accent">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
              <div>
                <h4 class="font-bold text-xs uppercase text-brand-black">14-Day Returns</h4>
                <p class="text-[11px]">No questions asked</p>
              </div>
            </div>
            <div class="flex items-center space-x-3 text-gray-600">
              <div class="bg-blue-50 p-2 rounded-full text-brand-accent">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z">
                  </path>
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
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M19.428 15.428a2 2 0 00-1.022-.547l-2.384-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z">
                  </path>
                </svg>
              </div>
              <div>
                <h4 class="font-bold text-xs uppercase text-brand-black">1-Year Warranty</h4>
                <p class="text-[11px]">On all electronics</p>
              </div>
            </div>
          </div>

          <div class="pt-4">
            <router-link to="/"
              class="flex items-center text-sm font-medium text-gray-500 hover:text-brand-black transition-colors group w-max">
              <svg class="w-4 h-4 mr-2 transform group-hover:-translate-x-1 transition-transform" fill="none"
                stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18">
                </path>
              </svg>
              Continue Shopping
            </router-link>
          </div>
        </div>

        <!-- Order Summary Column -->
        <div class="lg:col-span-4">
          <div class="bg-white p-6 border border-gray-200 sticky top-24 shadow-sm">
            <h2 class="text-xs font-black text-brand-black uppercase tracking-[0.2em] mb-6 pb-2 border-b border-gray-100">Order Summary</h2>

            <!-- Delivery Options -->
            <div class="mb-6">
              <h3 class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-3">Delivery Method</h3>
              <div class="grid grid-cols-2 gap-2 mb-4">
                <button 
                  @click="cartStore.deliveryMethod = 'delivery'"
                  type="button"
                  :class="[
                    'py-2 px-4 text-xs font-bold uppercase tracking-wider border transition-all',
                    cartStore.deliveryMethod === 'delivery' 
                      ? 'border-brand-black bg-brand-black text-white' 
                      : 'border-gray-200 text-gray-500 hover:border-gray-300'
                  ]"
                >
                  Delivery
                </button>
                <button 
                  @click="cartStore.deliveryMethod = 'pickup'"
                  type="button"
                  :class="[
                    'py-2 px-4 text-xs font-bold uppercase tracking-wider border transition-all',
                    cartStore.deliveryMethod === 'pickup' 
                      ? 'border-brand-black bg-brand-black text-white' 
                      : 'border-gray-200 text-gray-500 hover:border-gray-300'
                  ]"
                >
                  Pick Up
                </button>
              </div>

              <!-- Store Selector -->
              <div v-if="cartStore.deliveryMethod === 'pickup'" class="animate-fade-in">
                 <select 
                   v-model="cartStore.selectedStore"
                   class="w-full bg-brand-gray border-none text-xs font-bold p-3 focus:ring-1 focus:ring-brand-black outline-none transition uppercase tracking-wide mb-2"
                 >
                   <option :value="null" disabled>Select a Store</option>
                   <option v-for="store in stores" :key="store.id" :value="store.id">
                     {{ store.name }}
                   </option>
                 </select>
                 <p v-if="cartStore.selectedStore" class="text-[10px] text-gray-500 pl-1">
                   {{ stores.find(s => s.id === cartStore.selectedStore)?.address }}
                 </p>
              </div>
            </div>

            <div class="space-y-4 text-xs font-medium text-gray-500 mb-8">
              <div class="flex justify-between items-center">
                <span class="uppercase tracking-wider">Subtotal</span>
                <span class="text-sm font-bold text-brand-black">${{ formatPrice(cartStore.subtotal) }}</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="uppercase tracking-wider">{{ cartStore.deliveryMethod === 'pickup' ? 'Store Pickup' : 'Shipping' }}</span>
                <span class="text-brand-accent font-bold uppercase">FREE</span>
              </div>
              <div class="flex justify-between items-center pb-4 border-b border-gray-50">
                <span class="uppercase tracking-wider">Estimated Tax</span>
                <span class="text-sm font-bold text-brand-black">${{ formatPrice(cartStore.tax) }}</span>
              </div>
              <div class="flex justify-between items-center pt-2">
                <span class="text-sm font-black text-brand-black uppercase tracking-widest">Total</span>
                <span class="text-xl font-black text-brand-black">${{ formatPrice(cartStore.total) }}</span>
              </div>
            </div>

            <!-- Discount Code -->
            <div class="mb-8">
              <div class="flex gap-2">
                <input v-model="discountCode" type="text" placeholder="PROMO CODE"
                  class="flex-1 bg-brand-gray border-none text-[10px] font-bold p-3 focus:ring-1 focus:ring-brand-black outline-none transition uppercase tracking-widest">
                <button @click="applyDiscount"
                  class="px-6 bg-brand-black text-white text-[10px] font-bold uppercase tracking-widest hover:bg-gray-800 transition">
                  Apply
                </button>
              </div>
            </div>

            <div class="space-y-3">
              <button @click="proceedToCheckout" :disabled="cartStore.items.length === 0"
                class="w-full bg-brand-black text-white h-14 font-bold uppercase tracking-[0.2em] text-xs hover:bg-gray-800 transition-all disabled:opacity-20 disabled:cursor-not-allowed">
                Proceed to Checkout
              </button>

              <button
                class="w-full bg-[#25D366] text-white h-14 font-bold uppercase tracking-[0.2em] text-xs hover:bg-[#128C7E] transition-all flex justify-center items-center gap-2">
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path
                    d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981z" />
                </svg>
                WhatsApp Checkout
              </button>
            </div>

            <div class="mt-8 pt-8 border-t border-gray-100">
              <p class="text-[10px] font-bold text-gray-400 uppercase tracking-[0.2em] mb-4 text-center">Accepted Payments</p>
              <div
                class="flex justify-center items-center gap-6 text-gray-400">
                <div class="flex items-center gap-1">
                   <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg>
                   <span class="text-[9px] font-bold uppercase tracking-wider">Card</span>
                </div>
                <div class="flex items-center gap-1">
                   <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"></path></svg>
                   <span class="text-[9px] font-bold uppercase tracking-wider">Cash</span>
                </div>
              </div>
            </div>

            <div class="mt-8 border-t border-gray-100 pt-6">
              <h3 class="text-[10px] font-black text-brand-black uppercase tracking-widest mb-3">Support</h3>
              <p class="text-[10px] text-gray-500 mb-1 uppercase tracking-wider">Phone: <a href="tel:+96891515555"
                  class="text-brand-black hover:underline font-bold">+968 9151 5555</a></p>
              <p class="text-[10px] text-gray-500 uppercase tracking-wider">Email: <a href="mailto:support@phonemate.com"
                  class="text-brand-black hover:underline font-bold">support@phonemate.om</a></p>
            </div>
          </div>
        </div>
      </div>
    </div>


    <Transition enter-active-class="ease-out duration-300" enter-from-class="opacity-0" enter-to-class="opacity-100"
      leave-active-class="ease-in duration-200" leave-from-class="opacity-100" leave-to-class="opacity-0">
      <div v-if="showRemoveModal"
        class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-brand-black/60 backdrop-blur-sm"
        @click.self="cancelRemove">
        <Transition enter-active-class="ease-out duration-300"
          enter-from-class="opacity-0 scale-95"
          enter-to-class="opacity-100 scale-100" leave-active-class="ease-in duration-200"
          leave-from-class="opacity-100 scale-100"
          leave-to-class="opacity-0 scale-95">
          <div class="bg-white w-full max-w-md shadow-2xl relative border border-gray-100">
            <!-- Header -->
            <div class="p-8 pb-0 flex justify-between items-start">
              <div>
                <h3 class="text-2xl font-black text-brand-black uppercase tracking-tight leading-none">Wait</h3>
                <p class="text-xs text-brand-accent font-bold uppercase mt-2 tracking-[0.2em]">Limited Offer Included</p>
              </div>
              <button @click="cancelRemove" class="text-gray-400 hover:text-brand-black transition-colors focus:outline-none">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
              </button>
            </div>

            <div class="p-8">
              <p class="text-sm text-gray-600 mb-8 leading-relaxed">
                This item is in high demand and quantities are limited. Complete your purchase now and we'll apply a
                <span class="font-bold text-brand-black text-base underline decoration-brand-accent decoration-2 underline-offset-4">10% discount</span> to your order.
              </p>

              <!-- Benefits List -->
              <div class="space-y-4 mb-8">
                <div class="flex items-center group">
                  <div class="w-10 h-10 bg-brand-gray flex items-center justify-center mr-4 group-hover:bg-brand-accent/5 transition-colors">
                    <span class="text-lg">🎁</span>
                  </div>
                  <div>
                    <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest">Added Value</p>
                    <p class="text-xs font-bold text-brand-black uppercase">Free Gift (Worth $25)</p>
                  </div>
                </div>
                <div class="flex items-center group">
                  <div class="w-10 h-10 bg-brand-gray flex items-center justify-center mr-4 group-hover:bg-brand-accent/5 transition-colors">
                    <span class="text-lg">🚚</span>
                  </div>
                  <div>
                    <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest">Speed</p>
                    <p class="text-xs font-bold text-brand-black uppercase">Free 2-Day Express Shipping</p>
                  </div>
                </div>
                <div class="flex items-center group">
                  <div class="w-10 h-10 bg-brand-gray flex items-center justify-center mr-4 group-hover:bg-brand-accent/5 transition-colors">
                    <span class="text-lg">🔒</span>
                  </div>
                  <div>
                    <p class="text-[10px] font-bold text-gray-400 uppercase tracking-widest">Security</p>
                    <p class="text-xs font-bold text-brand-black uppercase">30-Day Price Protection</p>
                  </div>
                </div>
              </div>

              <!-- Promo Ribbon -->
              <div class="border-t border-b border-gray-100 py-4 mb-8 flex items-center justify-between">
                <div class="flex items-center gap-3">
                  <div class="w-3 h-3 bg-brand-accent rounded-full animate-pulse"></div>
                  <span class="text-xs font-bold text-brand-black uppercase tracking-wider">Active Promo: KEEP10</span>
                </div>
                <span class="text-xs font-black text-brand-accent uppercase">-10% OFF</span>
              </div>

              <!-- Action Buttons -->
              <div class="flex flex-col gap-3">
                <button @click="cancelRemove"
                  class="w-full bg-brand-black text-white h-14 font-bold uppercase tracking-[0.2em] text-xs hover:bg-gray-800 transition-all flex items-center justify-center gap-3">
                  Keep Item & Save
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
                  </svg>
                </button>
                <button @click="confirmRemove"
                  class="w-full py-2 text-[10px] font-bold text-gray-400 hover:text-brand-danger transition-colors uppercase tracking-[0.1em]">
                  No thanks, I'll pass on this
                </button>
              </div>
            </div>
          </div>
        </Transition>
      </div>
    </Transition>
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

const stores = [
  { id: 1, name: 'Downtown Flagship', address: '123 Main St, Downtown' },
  { id: 2, name: 'Northside Mall', address: '456 North Ave, Northside' },
  { id: 3, name: 'West End Plaza', address: '789 West Blvd, West End' },
  { id: 4, name: 'Airport Branch', address: '101 Airport Rd, Terminal 2' }
]

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