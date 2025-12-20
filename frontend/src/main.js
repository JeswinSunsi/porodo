import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import './style.css'

const app = createApp(App)

app.directive('animate-on-scroll', {
  mounted(el, binding) {
    el.classList.add('scroll-enter-from')
    
    const delay = binding.value?.delay || 0
    if (delay) {
      el.style.transitionDelay = `${delay}ms`
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          el.classList.add('scroll-enter-to')
          observer.unobserve(el)
        }
      })
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    })

    observer.observe(el)
  }
})

app.use(createPinia())
app.use(router)
app.mount('#app')
