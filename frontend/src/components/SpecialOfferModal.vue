<template>
  <transition
    enter-active-class="ease-out duration-300"
    enter-from-class="opacity-0"
    enter-to-class="opacity-100"
    leave-active-class="ease-in duration-200"
    leave-from-class="opacity-100"
    leave-to-class="opacity-0"
  >
    <div v-if="isOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-brand-black/60 backdrop-blur-sm transition-all duration-300">
      <div class="bg-white shadow-2xl max-w-sm w-full transform transition-all border border-gray-100 relative overflow-hidden">
        <!-- Decorative top bar -->
        <div class="h-1.5 w-full bg-brand-black"></div>
        
        <div class="p-8 text-center">
          <div class="mx-auto flex items-center justify-center h-16 w-16 rounded-full bg-gray-50 mb-6 border border-gray-100">
            <svg class="h-8 w-8 text-brand-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          
          <h3 class="text-xl font-bold text-brand-black mb-2 tracking-tight">Special Offer Unlocked!</h3>
          <p class="text-sm text-gray-500 mb-6 leading-relaxed">
            You've added your first item! Buy 2 of the same product to get <span class="font-bold text-brand-black">10% OFF</span> your entire order!
          </p>

          <div class="space-y-3">
            <button @click="close" class="w-full py-3.5 bg-brand-black text-white font-bold uppercase tracking-wider hover:bg-gray-800 transition-all shadow-lg shadow-gray-200 hover:shadow-xl">
              Got it!
            </button>
            <button @click="close" class="w-full py-2 text-xs font-bold text-gray-400 uppercase tracking-wider hover:text-gray-600 transition-colors">
              No thanks
            </button>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
defineProps({
  isOpen: Boolean
})

const emit = defineEmits(['close'])

function close() {
  emit('close')
}
</script>
