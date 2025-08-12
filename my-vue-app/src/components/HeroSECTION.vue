<template>
<div id="service" ref="root" class="grid sm:mt-[10%] md:mt-0 grid-cols-1 md:grid-cols-1 lg:grid-cols-2 gap-4 pt-[10%] pb-[10%] px-[10%]">
  <!-- Left Column -->
    <div class="flex items-start gap-4">
      <!-- Profile Image -->
      <img
        :src="image"
        alt="Header Image"
        class="w-20 h-20 md:w-24 md:h-24 rounded-full object-cover transform hover:-translate-x-5 hover:scale-110 border-2 border-white shadow-lg"
      />

      <!-- Arrow and Text Stack -->
      <div class="flex flex-col font-serif capitalize font-black">
        <!-- Arrow + First Line -->
        <div class="flex items-center space-x-2">
          <Icon icon="guidance:left-arrow" class="text-white animate-bounce" width="40" height="40" />
          <h1 class="text-white text-3xl md:text-5xl font-extrabold">Hi I am</h1>
        </div>

        <!-- Name Lines -->
        <h1 class="text-white text-10xl md:text-5xl font-extrabold">Aniekeme</h1>
        <h1 class="text-white text-3xl md:text-5xl font-extrabold flex items-center gap-2">
          Udoekong
          <span class="text-2xl md:text-4xl animate-wave origin-[70%_70%] inline-block">👋🏽</span>
        </h1>
      </div>
    </div>

    <!-- Right Column -->
    <div>
        <h5 class="font-serif capitalize  text-white text-xl semibold ">
            I’m a web developer, social media manager, and content creator, specializing in creating magical visual identities for digital products that connect, convert, and captivate
        </h5>
    <!-- button area the resume -->
        <div class="text-white mt-[5%] ">
            <button class="porfolio-button mr-[5%]">VIEW PORTFOLIO </button>
            <button class="border-white-500 download">DOWNLOAD RESUME</button>
        </div>
    </div>
  </div>
</template>

<script setup>
import { Icon } from '@iconify/vue'
import { ref, onMounted } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const image = require('@/assets/Headerrr.jpg')
const root = ref(null)

onMounted(() => {
  gsap.utils.toArray('h1, h3, h5, p, .text-2xl, .text-3xl, .text-4xl, .text-xl', root.value).forEach(el => {
    gsap.from(el, {
      scrollTrigger: {
        trigger: el,
        start: 'top 80%',
        toggleActions: 'play none none none'
      },
      y: 50,
      opacity: 0,
      duration: 1,
      ease: 'power3.out'
    })
  })
})
</script>

<style scoped>
@keyframes wave {
  0% { transform: rotate(0deg); }
  10% { transform: rotate(14deg); }
  20% { transform: rotate(-8deg); }
  30% { transform: rotate(14deg); }
  40% { transform: rotate(-4deg); }
  50% { transform: rotate(10deg); }
  60%, 100% { transform: rotate(0deg); }
}

.animate-wave {
  animation: wave 1.8s infinite;
}
/* button area styling*/
.download {
  background-color: transparent;
  color: white;
  border: 2px solid white;
  padding: 10px 20px;
  border-radius: 50px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}
.download:hover {
  background-color: rgb(163, 156, 156);
  color: black;
}
.porfolio-button {
  background-color: white;
  color: black;
  padding: 10px 20px;
  border-radius: 50px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}
.porfolio-button:hover {
  background-color: rgb(163, 156, 156);
  color: black;
}

</style>
