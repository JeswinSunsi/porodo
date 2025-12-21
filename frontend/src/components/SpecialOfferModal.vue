<template>
  <transition
    enter-active-class="ease-out duration-300"
    enter-from-class="opacity-0 scale-95"
    enter-to-class="opacity-100 scale-100"
    leave-active-class="ease-in duration-200"
    leave-from-class="opacity-100 scale-100"
    leave-to-class="opacity-0 scale-95"
  >
    <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-brand-black/60 backdrop-blur-sm">
      <div class="bg-white rounded-lg shadow-2xl max-w-sm w-full overflow-hidden relative animate-pop-in">
        
        <!-- Close Button -->
        <button @click="close" class="absolute top-3 right-3 z-10 p-2 text-gray-400 hover:text-gray-600 hover:bg-gray-100 rounded-full transition-all">
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>

        <!-- Header Image / Icon Area -->
        <div class="bg-gradient-to-br from-brand-accent/10 to-brand-accent/5 p-8 text-center relative overflow-hidden">
            <!-- Decorative circles -->
            <div class="absolute top-0 left-0 w-32 h-32 bg-brand-accent/10 rounded-full -translate-x-1/2 -translate-y-1/2 blur-2xl"></div>
            <div class="absolute bottom-0 right-0 w-32 h-32 bg-brand-accent/10 rounded-full translate-x-1/2 translate-y-1/2 blur-2xl"></div>

            <div class="relative inline-block">
                <div class="h-20 w-20 bg-white rounded-full flex items-center justify-center shadow-lg shadow-brand-accent/20 mb-2 mx-auto ring-4 ring-white">
                    <span class="text-2xl font-black text-brand-accent">-15%</span>
                </div>
                <div class="absolute -top-2 -right-2 bg-brand-danger text-white text-[10px] font-bold px-2 py-0.5 rounded shadow-sm animate-bounce">
                    LIMITED
                </div>
            </div>
            <h3 class="text-xl font-black text-brand-black mt-4 uppercase tracking-tight">Special Offer Unlocked!</h3>
        </div>

        <div class="p-6 pt-5">
          <p class="text-center text-gray-600 text-sm mb-5">
            Don't miss out! Buy <span class="font-bold text-brand-black">2 products</span> together and get <span class="font-bold text-brand-accent">15% OFF</span> your entire order.
          </p>

          <!-- Progress Bar -->
          <div class="bg-gray-50 rounded-md p-4 mb-3 border border-gray-100">
            <div class="flex justify-between text-xs font-bold uppercase tracking-wider text-gray-500 mb-2">
              <span>Progress</span>
              <span class="text-brand-accent">Almost there!</span>
            </div>
            <div class="h-3 w-full bg-gray-200 rounded-sm overflow-hidden">
              <div class="h-full bg-brand-accent w-1/2 relative rounded-sm">
                <div class="absolute inset-0 bg-white/30 animate-pulse"></div>
              </div>
            </div>
            <p class="text-[10px] text-center text-gray-400 mt-2 font-medium">Add 1 more item to unlock savings</p>
          </div>

          <!-- Action Buttons -->
          <div class="space-y-3">
            <button @click="close" class="w-full py-3.5 bg-brand-accent hover:bg-brand-accentHover text-white font-bold text-sm rounded-md shadow-lg shadow-brand-accent/30 hover:shadow-brand-accent/40 hover:-translate-y-0.5 transition-all flex items-center justify-center gap-2">
              <span>Let's go</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path></svg>
            </button>
          </div>
          
          <!-- Timer -->
          <div class="mt-4 flex items-center justify-center gap-1.5 text-brand-danger/80">
             <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
             <p class="text-[10px] font-bold uppercase tracking-widest">
               Offer expires in {{ formattedTime }}
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
const timeLeft = ref(180) // 3 minutes in seconds
let timerInterval

const formattedTime = computed(() => {
  const minutes = Math.floor(timeLeft.value / 60)
  const seconds = timeLeft.value % 60
  return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`
})

function startTimer() {
  clearInterval(timerInterval)
  timeLeft.value = 180
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
/* No custom styles needed, using Tailwind utility classes */
</style>
