<template>
  <main class="py-8 bg-gray-50 min-h-screen">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold text-brand-black mb-4 tracking-tight">Checkout</h1>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <!-- Checkout Forms -->
        <div class="lg:col-span-8 space-y-8">
          
          <!-- Delivery Information -->
          <div class="bg-white p-6 border border-gray-100">
            <h2 class="text-xl font-bold text-brand-black mb-6">Delivery Information</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
                <input v-model="form.name" type="text" class="w-full bg-gray-50 border border-gray-200 p-3 focus:ring-1 focus:ring-brand-black focus:border-brand-black outline-none transition">
              </div>
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-1">Address</label>
                <input v-model="form.address" type="text" class="w-full bg-gray-50 border border-gray-200 p-3 focus:ring-1 focus:ring-brand-black focus:border-brand-black outline-none transition">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">City</label>
                <input v-model="form.city" type="text" class="w-full bg-gray-50 border border-gray-200 p-3 focus:ring-1 focus:ring-brand-black focus:border-brand-black outline-none transition">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">House Number</label>
                <input v-model="form.houseNumber" type="text" class="w-full bg-gray-50 border border-gray-200 p-3 focus:ring-1 focus:ring-brand-black focus:border-brand-black outline-none transition">
              </div>
              <div class="md:col-span-2">
                <label class="block text-sm font-medium text-gray-700 mb-1">Governorate</label>
                <select v-model="form.governorate" class="w-full bg-gray-50 border border-gray-200 p-3 focus:ring-1 focus:ring-brand-black focus:border-brand-black outline-none transition">
                  <option value="Muscat">Muscat</option>
                  <option value="Dhofar">Dhofar</option>
                  <option value="Musandam">Musandam</option>
                  <option value="Al Buraimi">Al Buraimi</option>
                  <option value="Al Dakhiliyah">Al Dakhiliyah</option>
                  <option value="Al Batinah North">Al Batinah North</option>
                  <option value="Al Batinah South">Al Batinah South</option>
                  <option value="Al Zahirah">Al Zahirah</option>
                  <option value="Al Sharqiyah North">Al Sharqiyah North</option>
                  <option value="Al Sharqiyah South">Al Sharqiyah South</option>
                  <option value="Al Wusta">Al Wusta</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Payment Information -->
          <div class="bg-white p-6 border border-gray-100">
            <h2 class="text-xl font-bold text-brand-black mb-6">Payment Details</h2>
            <div class="bg-gray-50 p-4 border border-gray-200 rounded text-center">
              <p class="text-brand-black font-medium">Pay with Cash or Card on Delivery.</p>
              <p class="text-sm text-gray-500 mt-1">You can pay using cash or card when your order arrives.</p>
              
              <div class="mt-4 pt-4 border-t border-gray-200 flex items-center justify-center gap-2 text-green-700">
                 <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5">
                   <path fill-rule="evenodd" d="M8.603 3.799A4.49 4.49 0 0112 2.25c1.357 0 2.573.6 3.397 1.549a4.49 4.49 0 013.498 1.307 4.491 4.491 0 011.307 3.497A4.49 4.49 0 0121.75 12a4.49 4.49 0 01-1.549 3.397 4.491 4.491 0 01-1.307 3.497 4.491 4.491 0 01-3.497 1.307A4.49 4.49 0 0112 21.75a4.49 4.49 0 01-3.397-1.549 4.49 4.49 0 01-3.498-1.306 4.491 4.491 0 01-1.307-3.498A4.49 4.49 0 012.25 12c0-1.357.6-2.573 1.549-3.397a4.49 4.49 0 011.307-3.497 4.49 4.49 0 013.497-1.307zm4.45 6.45l-4.25 4.25a.75.75 0 01-1.06 0l-1.75-1.75a.75.75 0 011.06-1.06l1.22 1.22 3.72-3.72a.75.75 0 011.06 1.06z" clip-rule="evenodd" />
                 </svg>
                 <span class="text-sm font-semibold">100% Original &amp; Assured</span>
              </div>
            </div>
          </div>

        </div>

        <!-- Order Summary -->
        <div class="lg:col-span-4">
          <div class="bg-white p-4 border border-gray-100 sticky top-24">
            <h2 class="text-lg font-bold text-brand-black uppercase tracking-wide mb-4">Order Summary</h2>
            
            <!-- Mini Cart Items -->
            <div class="max-h-60 overflow-y-auto mb-4 space-y-3 border-b border-gray-200 pb-4">
              <div v-for="item in cartStore.items" :key="item.product_id" class="flex gap-3">
                <div class="w-12 h-12 bg-gray-50 border border-gray-100 flex items-center justify-center flex-shrink-0">
                  <img :src="item.image_url" :alt="item.name" class="w-8 h-8 object-contain mix-blend-multiply">
                </div>
                <div class="flex-1 min-w-0">
                  <p class="text-sm font-medium text-brand-black truncate">{{ item.name }}</p>
                  <p class="text-xs text-gray-500">Qty: {{ item.quantity }}</p>
                </div>
                <div class="text-sm font-medium text-brand-black">
                  ${{ formatPrice(item.price * item.quantity) }}
                </div>
              </div>
            </div>

            <!-- Promo Code -->
            <div class="mb-4 border-b border-gray-200 pb-4">
               <label class="block text-xs font-medium text-gray-700 mb-1">Promo Code</label>
               <input v-model="form.promoCode" type="text" class="w-full bg-gray-50 border border-gray-200 p-2 text-sm focus:ring-1 focus:ring-brand-black focus:border-brand-black outline-none transition" placeholder="Enter code">
            </div>

            <div class="space-y-2 text-sm text-gray-600 mb-4">
              <div class="flex justify-between">
                <span>Subtotal</span>
                <span class="font-medium text-brand-black">${{ formatPrice(cartStore.subtotal) }}</span>
              </div>
              <div class="flex justify-between">
                <span>Shipping</span>
                <span class="text-brand-accent font-medium">Free</span>
              </div>
              <div class="flex justify-between">
                <span>Tax</span>
                <span class="font-medium text-brand-black">${{ formatPrice(cartStore.tax) }}</span>
              </div>
            </div>

            <div class="border-t border-gray-200 pt-4 mb-6">
              <div class="flex justify-between text-lg font-bold text-brand-black">
                <span>Order Total</span>
                <span>${{ formatPrice(cartStore.total) }}</span>
              </div>
            </div>

            <button 
              @click="placeOrder"
              :disabled="processing || cartStore.items.length === 0"
              class="w-full bg-brand-black text-white h-12 font-bold uppercase tracking-wider hover:bg-gray-800 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center"
            >
              <span v-if="!processing">Place Order</span>
              <span v-else>Processing...</span>
            </button>
            
            <div class="mt-4 text-center">
               <router-link to="/cart" class="text-sm text-gray-500 hover:text-brand-black underline">Return to Cart</router-link>
            </div>

          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useCartStore } from '@/stores/cart'
import { useRouter } from 'vue-router'

const cartStore = useCartStore()
const router = useRouter()
const processing = ref(false)

const form = reactive({
  name: '',
  address: '',
  city: '',
  houseNumber: '',
  governorate: 'Muscat',
  promoCode: ''
})

function formatPrice(price) {
  return price.toFixed(2)
}

async function placeOrder() {
  if (cartStore.items.length === 0) return
  
  // Basic validation
  if (!form.name || !form.address || !form.city || !form.houseNumber || !form.governorate) {
    alert('Please fill in all fields')
    return
  }

  processing.value = true
  
  try {
    const orderData = {
      name: form.name,
      address: form.address,
      city: form.city,
      houseNumber: form.houseNumber,
      governorate: form.governorate,
      promo_code: form.promoCode,
      items: cartStore.items.map(item => ({
        product_id: item.product_id,
        quantity: item.quantity,
        selected_color: item.selected_color
      })),
      total: cartStore.total
    }

    const response = await fetch('http://localhost:8000/api/orders', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(orderData),
    })

    if (!response.ok) {
      throw new Error('Failed to place order')
    }
    
    alert('Order placed successfully! Payment will be collected on delivery.')
    cartStore.clearCart()
    router.push('/')
  } catch (error) {
    console.error('Error placing order:', error)
    alert('Failed to place order. Please try again.')
  } finally {
    processing.value = false
  }
}
</script>
