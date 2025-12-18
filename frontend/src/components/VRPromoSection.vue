<template>
  <section class="bg-brand-black text-white py-20 overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
      <div class="order-2 md:order-1 relative">
        <img 
          src="https://images.unsplash.com/photo-1550009158-9ebf69173e03?q=80&w=1000&auto=format&fit=crop" 
          alt="VR Headset" 
          class="rounded-sm border border-gray-700 w-full object-cover h-[400px] hover:scale-105 transition-transform duration-700"
        >
        <div class="absolute -bottom-6 -right-6 bg-brand-accent text-white p-6 w-40 text-center rounded-none hidden md:block shadow-2xl">
          <p class="text-3xl font-bold">30%</p>
          <p class="text-sm font-medium uppercase">Off VR Gear</p>
        </div>
      </div>
      <div class="order-1 md:order-2 space-y-6">
        <h2 class="text-4xl md:text-5xl font-bold leading-tight">Immersion like <br>never before.</h2>
        <p class="text-gray-400 text-lg">
          Step into the future with our next-gen VR headsets. Ultra-low latency, 4K resolution per eye, and wireless freedom.
        </p>
        <ul class="space-y-3 text-gray-300">
          <li class="flex items-center">
            <svg class="w-5 h-5 text-brand-accent mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
            2-Year Official Warranty
          </li>
          <li class="flex items-center">
            <svg class="w-5 h-5 text-brand-accent mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
            Includes Half-Life: Alyx
          </li>
        </ul>
        <button class="mt-4 bg-white text-brand-black px-10 py-4 font-bold uppercase tracking-wider hover:bg-gray-200 transition-colors hover:scale-105 transform duration-200">
          Explore VR
        </button>
      </div>
    </div>
  </section>
</template>
