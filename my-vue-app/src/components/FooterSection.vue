<template>
  <footer class="bg-black text-white border-t border-gray-800 px-6 md:px-[10%] py-12 relative">
    <div class="flex flex-col md:flex-row justify-between gap-12 text-center md:text-left">
      <!-- Left: Logo and copyright -->
      <div class="flex-1">
        <img src="/logo-white.svg" alt="Logo" class="w-10 h-10 mx-auto md:mx-0 mb-4" />
        <p class="text-sm text-gray-400 mb-1">© 2025. Mellow</p>
        <p class="text-sm text-gray-400">
          <a href="#" class="hover:underline">WordPress Theme by Tansh</a>
        </p>
      </div>

      <!-- Center: Navigation -->
      <div class="flex-1">
        <h4 class="text-sm font-bold uppercase mb-4">Navigation</h4>
        <ul class="space-y-2 text-sm text-gray-300">
          <li><a href="#services" class="hover:text-white">Services</a></li>
          <li><a href="#works" class="hover:text-white">Works</a></li>
          <li><a href="#about" class="hover:text-white">About Me</a></li>
          <li><a href="#articles" class="hover:text-white">Articles</a></li>
          <li><a href="#contact" class="hover:text-white">Contact</a></li>
        </ul>
      </div>

      <!-- Right: Connect -->
      <div class="flex-1">
        <h4 class="text-sm font-bold uppercase mb-4">Connect</h4>
        <div class="space-y-3 flex flex-col items-center md:items-start">
          <a
            href="https://twitter.com/yourusername"
            target="_blank"
            class="flex items-center gap-3 border border-gray-700 rounded-full px-4 py-2 hover:bg-white hover:text-black transition"
          >
            <Icon icon="ri:twitter-x-fill" class="w-5 h-5" />
            <span class="text-sm">Twitter / X</span>
          </a>
          <a
            href="https://wa.me/2349071641796"
            target="_blank"
            class="flex items-center gap-3 border border-gray-700 rounded-full px-4 py-2 hover:bg-white hover:text-black transition"
          >
            <Icon icon="ic:baseline-whatsapp" class="w-5 h-5" />
            <span class="text-sm">WhatsApp</span>
          </a>
        </div>
      </div>
    </div>

    <!-- Scroll to top -->
    <button
      @click="scrollToTop"
      class="absolute right-4 bottom-4 md:right-8 md:bottom-6 p-2 bg-white text-black rounded hover:bg-gray-300 transition"
      aria-label="Scroll to top"
    >
      <Icon icon="mdi:chevron-up" class="w-5 h-5" />
    </button>
  </footer>
</template>

<script setup>
import { Icon } from '@iconify/vue'

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
</script> 