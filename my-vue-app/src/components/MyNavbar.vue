<template>
  <div class="fixed top-0 left-0 z-50 bg-[#0a0a0a] text-white w-full text-l p-7">
    <div class="flex items-center justify-between">
      <!-- Logo -->
      <div class="font-bold">LOGO</div>

      <!-- Desktop Menu -->
      <ul class="hidden md:flex space-x-10  font-bold uppercase tracking-wide font-sans  transition">
        <li v-for="item in Menu" :key="item.name">
          <a :href="item.href" class="hover:text-gray-300 transition">
            {{ item.name }}
          </a>
        </li>
      </ul>

      <!-- Mobile Menu Toggle -->
      <button
      @click="toggleMenu" class="md:hidden">
<Icon 
    v-if="!isOpen"
       icon="fluent:navigation-20-regular" width="20" height="20" />
<Icon
v-else icon="proicons:cancel" width="24" height="24" />
</button>
    </div>

    <!-- Animated Mobile Dropdown -->
    <Transition name="slide-fade">
      <ul v-if="isOpen" class="md:hidden mt-4 space-y-4 font-serif">
        <li v-for="item in Menu" :key="item.name">
          <a :href="item.href" class="block px-4 py-2 hover:bg-[#1a1a1a] rounded">
            {{ item.name }}
          </a>
        </li>
      </ul>
    </Transition>
  </div>
</template>


<script setup>
import { ref } from 'vue'
import { Icon } from '@iconify/vue'

const isOpen = ref(false)
const toggleMenu = () => {
  isOpen.value = !isOpen.value
}

const Menu = ref([
  { name: 'Home', href: '/' },
  { name: 'Service', href: '#service' },
  { name: 'Skills', href: '#skills' },
  { name: 'Projects', href: '#projects' },
  { name: 'About Me', href: '#why-me' },
  { name: 'Contact', href: '#contact' },
])
</script>
<style scoped>
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.3s ease;
}
.slide-fade-enter-from,
.slide-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
