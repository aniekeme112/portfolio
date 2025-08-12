<template>
  <section class="bg-black text-white px-[15%] py-20">
    <div class="text-center mb-12">
      <p class="text-gray-400 text-sm mb-2">How I work</p>
      <h2 class="text-4xl font-extrabold mb-4 leading-tight">
        PRODUCT DESIGN PROCESS
      </h2>
      <p class="text-gray-400 max-w-3xl mx-auto">
        Structured series of steps that guide the development of a new product—from identifying a problem or opportunity, to delivering a final, market-ready solution.
      </p>
    </div>

    <!-- Timeline Line -->
    <div class="relative w-full h-8 flex justify-between items-center max-w-5xl mx-auto mb-12">
      <div v-for="i in 3" :key="i" class="relative">
        <div class="w-4 h-4 rounded-full bg-black border-4 border-white z-10 relative animate-pulse"></div>
        <div
          v-if="i !== 3"
          class="absolute top-1/2 left-full w-[calc(100%-1rem)] h-[2px] bg-white transform -translate-y-1/2"
        ></div>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-12 mb-20">
      <!-- Discover -->
      <div class="transition-all duration-500 transform hover:scale-105">
        <h3 class="text-xl font-semibold mb-2">1. Discover</h3>
        <p class="text-gray-400 mb-4">
          The goal is to define clear objectives and requirements for the product and gathering insights.
        </p>
        <div class="flex flex-col gap-2">
          <span v-for="(item, i) in discover" :key="i" class="px-4 py-2 border border-gray-600 rounded-full text-sm text-white bg-[#121212] hover:bg-white hover:text-black transition-colors duration-300">
            {{ item }}
          </span>
        </div>
      </div>

      <!-- Design -->
      <div class="transition-all duration-500 transform hover:scale-105">
        <h3 class="text-xl font-semibold mb-2">2. Design</h3>
        <p class="text-gray-400 mb-4">
          In this stage, ideas are translated into tangible concepts to align product with business goals.
        </p>
        <div class="flex flex-col gap-2">
          <span v-for="(item, i) in design" :key="i" class="px-4 py-2 border border-gray-600 rounded-full text-sm text-white bg-[#121212] hover:bg-white hover:text-black transition-colors duration-300">
            {{ item }}
          </span>
        </div>
      </div>

      <!-- Deliver -->
      <div class="transition-all duration-500 transform hover:scale-105">
        <h3 class="text-xl font-semibold mb-2">3. Deliver</h3>
        <p class="text-gray-400 mb-4">
          The final phase involves collaborating with developers to build and launch the product.
        </p>
        <div class="flex flex-col gap-2">
          <span v-for="(item, i) in deliver" :key="i" class="px-4 py-2 border border-gray-600 rounded-full text-sm text-white bg-[#121212] hover:bg-white hover:text-black transition-colors duration-300">
            {{ item }}
          </span>
        </div>
      </div>
    </div>

    <!-- Testimonials Section -->
    <div class="text-center">
      <p class="text-gray-400 text-sm mb-2">Testimonials</p>
      <h2 class="text-4xl font-extrabold mb-12">WHAT CLIENTS SAY</h2>

      <div class="relative h-[200px] md:h-[180px] flex items-center justify-center">
        <transition-group name="fade" tag="div" class="w-full relative">
          <div
            v-for="testimonial in visibleTestimonials"
            :key="testimonial.id"
            class="absolute inset-0 flex flex-col items-center justify-center transition-opacity duration-500 ease-in-out"
          >
            <img :src="testimonial.image" class="w-14 h-14 rounded-full mb-4" />
            <p class="max-w-3xl text-lg font-light leading-relaxed text-gray-300 px-4">
              "{{ testimonial.text }}"
            </p>
            <div class="mt-4 text-sm text-gray-400">
              <p class="font-semibold">{{ testimonial.name }}</p>
              <p class="text-xs">{{ testimonial.role }}</p>
            </div>
          </div>
        </transition-group>
      </div>

      <div class="flex justify-center gap-4 mt-12">
        <button @click="prevTestimonial" class="w-10 h-10 rounded-full border border-white flex items-center justify-center hover:bg-white hover:text-black transition duration-300">
          <Icon icon="ph:arrow-left-light" class="w-5 h-5" />
        </button>
        <button @click="nextTestimonial" class="w-10 h-10 rounded-full border border-white flex items-center justify-center hover:bg-white hover:text-black transition duration-300">
          <Icon icon="ph:arrow-right-light" class="w-5 h-5" />
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
  import { onMounted, nextTick, ref, computed } from 'vue'
  import { gsap } from 'gsap'
  import { Icon } from '@iconify/vue'
  
  const discover = [
    'STAKEHOLDER INTERVIEW',
    'PROBLEM FINDING',
    'MARKET RESEARCH',
    'PRODUCT POSITIONING',
    'UX RESEARCH'
  ]
  
  const design = [
    'WIREFRAME',
    'VISUAL DESIGN',
    'USER TESTING',
    'VALIDATION'
  ]
  
  const deliver = [
    'PROJECT HANDOVER',
    'DEVELOPER COLLABORATION',
    'LONG TIME SUPPORT'
  ]
  
  const testimonials = [
    {
      id: 1,
      name: 'Etimuk Udoekong',
      role: 'CEO, Mogedy.ng',
      image: 'https://tse2.mm.bing.net/th/id/OIP.KSKjHZjKGErPSUglZkaAhwAAAA?r=0&rs=1&pid=ImgDetMain&o=7&rm=3',
      text: 'Extremely professional, unique and enjoyable. The effort taken to ensure sed quia non numquam eius modi tempora incidunt ut labore voluptatem.'
    },
    {
      id: 2,
      name: 'Carol Sasaki',
      role: 'CEO Of IHF',
      image: 'https://i.pinimg.com/280x280_RS/55/5e/2c/555e2c2921a1ed95b030bdf3dde985c8.jpg',
      text: 'Extremely professional, unique and enjoyable. The effort taken to ensure sed quia non numquam eius modi tempora incidunt ut labore voluptatem.'
    },
    {
      id: 3,
      name: 'Engr Akpan',
      role: 'CEO OF BSA MANAGEMENT and HOPE FOUNDATION',
      image: require('@/assets/bsa.jpg'),
      text: 'Extremely professional, unique and enjoyable. The effort taken to ensure sed quia non numquam eius modi tempora incidunt ut labore voluptatem.'
    }
  ]
  
  const currentIndex = ref(0)
  const visibleTestimonials = computed(() => [testimonials[currentIndex.value]])
  const nextTestimonial = () => {
    currentIndex.value = (currentIndex.value + 1) % testimonials.length
  }
  const prevTestimonial = () => {
    currentIndex.value = (currentIndex.value - 1 + testimonials.length) % testimonials.length
  }
  
  onMounted(() => {
    nextTick(() => {
      gsap.from("section > div", {
        opacity: 0,
        y: 30,
        duration: 0.6,
        stagger: 0.3,
        ease: "power2.out"
      });
    })
  })
  </script>
  
  <style scoped>
  section span {
    display: inline-block;
    cursor: default;
  }
  .fade-enter-active,
  .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter-from,
  .fade-leave-to {
    opacity: 0;
  }
  </style>
  