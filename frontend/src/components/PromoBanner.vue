<template>
  <div class="bg-brand-black text-white text-xs font-medium py-2 text-center tracking-wide relative z-50">
    {{ promotion.title }}: {{ promotion.description }}
    <span v-if="promotion.code" class="ml-1">
      Use code: <span class="border-b border-yellow-400 text-yellow-400">{{ promotion.code }}</span>
    </span>
  </div>
</template>

<script setup>
defineProps({
  promotion: {
    type: Object,
    required: true
  }
})
</script>
