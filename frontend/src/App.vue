<template>
  <div class="min-h-screen flex flex-col">
    <PromoBanner v-if="activePromotion" :promotion="activePromotion" />
    <NavBar :cartCount="cartStore.itemCount" />
    <main class="flex-grow">
      <router-view />
    </main>
    <FooterSection />
    <ToastNotification />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCartStore } from '@/stores/cart'
import NavBar from '@/components/NavBar.vue'
import FooterSection from '@/components/FooterSection.vue'
import PromoBanner from '@/components/PromoBanner.vue'
import ToastNotification from '@/components/ToastNotification.vue'
import { getPromotions } from '@/services/api'

const cartStore = useCartStore()
const activePromotion = ref(null)

onMounted(async () => {
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
