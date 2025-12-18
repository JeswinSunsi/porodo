<template>
</template>

<script setup>
import { ref } from 'vue'

const email = ref('')

function subscribe() {
  console.log('Subscribing:', email.value)
  alert(`Thanks for subscribing with ${email.value}!`)
  email.value = ''
}
</script>
