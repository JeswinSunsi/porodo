<template>
  <transition
    enter-active-class="ease-out duration-300"
    enter-from-class="opacity-0"
    enter-to-class="opacity-100"
    leave-active-class="ease-in duration-200"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
  >
    <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-brand-black/80 backdrop-blur-sm transition-all duration-300">
      <div class="bg-white shadow-2xl max-w-md w-full transform transition-all relative border-x border-b border-gray-200 border-t-4 border-t-brand-accent">
        
        <button @click="close" class="absolute top-4 right-4 text-gray-400 hover:text-brand-black transition-colors">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>

        <div class="p-8 text-center">
          <!-- Visual Icon -->
          <div class="mx-auto flex items-center justify-center h-24 w-24 bg-brand-accent/5 mb-6 border border-brand-accent/10 rounded-full ring-4 ring-brand-accent/5">
            <span class="text-4xl font-black text-brand-accent tracking-tighter">-10%</span>
          </div>
          
          <h3 class="text-2xl font-black text-brand-black mb-2 tracking-tight uppercase">Unlock Discount</h3>
          
          <p class="text-gray-600 mb-8 leading-relaxed text-sm">
            Add <span class="font-bold text-brand-black">1 more</span> of the same product to your cart and instantly save <span class="font-bold text-brand-accent">10%</span> on your order.
          </p>

          <!-- Progress Bar -->
          <div class="mb-8">
            <div class="flex justify-between text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
              <span>1 Item Added</span>
              <span class="text-brand-accent">10% OFF Unlocked</span>
            </div>
            <div class="h-2 w-full bg-gray-100">
              <div class="h-full bg-brand-accent w-1/2 relative">
                <div class="absolute inset-0 bg-white/20 animate-pulse"></div>
              </div>
            </div>
            <p class="text-xs text-gray-400 mt-2 italic">Add 1 more to complete the deal</p>
          </div>

          <!-- Action Buttons -->
          <div class="space-y-3">
            <button @click="close" class="group w-full py-4 bg-brand-black text-white font-bold text-sm uppercase tracking-wider hover:bg-gray-900 transition-all flex items-center justify-center gap-2 border border-brand-black shadow-xl shadow-brand-accent/10 hover:shadow-brand-accent/20">
              <span>Add to Cart & Save</span>
              <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
            </button>
            
            <button @click="close" class="w-full py-3 text-xs font-bold text-gray-400 uppercase tracking-wider hover:text-brand-black transition-colors border border-transparent hover:border-gray-200">
              I'll pay full price
            </button>
          </div>
          
          <!-- Subtle Urgency -->
          <div class="mt-6 pt-4 border-t border-gray-100">
             <p class="text-[10px] text-brand-danger font-bold uppercase tracking-widest">
               Offer Expires in {{ formattedTime }}
             </p>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed, watch } from 'vue'

const props = defineProps({
  isOpen: Boolean
})

const emit = defineEmits(['close'])

// Countdown Timer Logic
const timeLeft = ref(600) // 10 minutes in seconds
let timerInterval

const formattedTime = computed(() => {
  const minutes = Math.floor(timeLeft.value / 60)
  const seconds = timeLeft.value % 60
  return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`
})

function startTimer() {
  clearInterval(timerInterval)
  timeLeft.value = 600
  timerInterval = setInterval(() => {
    if (timeLeft.value > 0) {
      timeLeft.value--
    } else {
      clearInterval(timerInterval)
      // Optional: Auto close or show expired state
    }
  }, 1000)
}

// Watch for modal opening to restart timer
watch(() => props.isOpen, (newValue) => {
  if (newValue) {
    startTimer()
  } else {
    clearInterval(timerInterval)
  }
})

function close() {
  emit('close')
}

onUnmounted(() => {
  clearInterval(timerInterval)
})
</script>

<style scoped>
.animate-bounce-slow {
  animation: bounce 2s infinite;
}
@keyframes bounce {
  0%, 100% { transform: translateY(-5%); }
  50% { transform: translateY(5%); }
}
</style>
