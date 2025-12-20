<template>
  <div class="min-h-screen flex flex-col">
    <PromoBanner v-if="activePromotion" :promotion="activePromotion" />
    <NavBar :cartCount="cartStore.itemCount" />
    <main class="flex-grow">
      <router-view />
    </main>
    <FooterSection />
    <ToastNotification />
    <SpecialOfferModal :isOpen="showSpecialOffer" @close="closeSpecialOffer" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCartStore } from '@/stores/cart'
import NavBar from '@/components/NavBar.vue'
import FooterSection from '@/components/FooterSection.vue'
import PromoBanner from '@/components/PromoBanner.vue'
import ToastNotification from '@/components/ToastNotification.vue'
import SpecialOfferModal from '@/components/SpecialOfferModal.vue'
import { getPromotions } from '@/services/api'

const cartStore = useCartStore()
const activePromotion = ref(null)
const showSpecialOffer = ref(false)
const offerShown = ref(false)

// Watch for cart changes to trigger the modal
import { watch } from 'vue'
watch(() => cartStore.itemCount, (newCount, oldCount) => {
  if (newCount > 0 && !offerShown.value && !cartStore.hasDiscount) {
    // Only show if it's the first time adding items (or going from 0 to >0)
    // But the requirement says "after the first product is added".
    // If the user refreshes, we might not want to show it again if they already saw it.
    // For now, let's just show it once per session/load.
    showSpecialOffer.value = true
    offerShown.value = true
  }
})

function closeSpecialOffer() {
  showSpecialOffer.value = false
}

onMounted(async () => {
  await cartStore.fetchCart()
  try {
    const promotions = await getPromotions()
    if (promotions.length > 0) {
      activePromotion.value = promotions[0]
    }
  } catch (error) {
    console.error('Failed to fetch promotions:', error)
  }
})
</script>
