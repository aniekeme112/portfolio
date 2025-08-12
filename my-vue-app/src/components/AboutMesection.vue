<template>
  <section id="why-me" ref="root" class="bg-black text-white py-20 px-10 md:px-20 grid grid-cols-1 md:grid-cols-12 gap-10 items-center">
    <!-- Side Label -->
    <div class="md:col-span-2 text-left md:text-right">
      <p class="text-lg font-light text-gray-300">About Me</p>
    </div>

    <!-- Main Content -->
    <div class="md:col-span-7">
      <h1 class="text-3xl md:text-5xl font-extrabold leading-tight uppercase">
        A Social Media Writer, 
  Website Developer,
  Content Creator, 
  and Tech Enthusiast.
      </h1>
    </div>

    <!-- Right Text -->
    <div class="md:col-span-3 space-y-6">
      <p class="text-sm text-gray-400 leading-relaxed">
        I specialize in crafting compelling content, building engaging websites, and growing brands through digital storytelling. I believe that powerful work begins with shared values, honest communication, technical skill, and a deep understanding of your audience.
      </p>

      <!-- Contact Glass Card -->
      <a
        href="mailto:aniekemeudoeong@gmail.com"
        class="flex items-center backdrop-blur-md bg-white/10 border border-white/20 rounded-full px-4 py-2 w-fit hover:bg-white hover:text-black transition"
      >
        <img
          src="@/assets/Headerrr.jpg"
          alt="profile"
          class="w-10 h-10 rounded-full object-cover mr-3 border border-white/30"
        />
        <div>
          <p class="text-xs uppercase font-semibold">Get in Touch</p>
          <p class="text-sm font-light">aniekemeudoeong@gmail.com</p>
        </div>
      </a>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const root = ref(null)

onMounted(() => {
  gsap.utils.toArray('p, h1, a', root.value).forEach((el, i) => {
    gsap.from(el, {
      scrollTrigger: {
        trigger: el,
        start: 'top 90%',
        toggleActions: 'play none none none',
      },
      y: 30,
      opacity: 0,
      duration: 0.8,
      delay: i * 0.1,
      ease: 'power3.out',
    })
  })
})
</script>

<style scoped>
/* Optional extra glassy effect if you want shadow */
a:hover img {
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
}
</style>
