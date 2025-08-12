<template>
    <section class="bg-black text-white px-[15%] py-20 grid grid-cols-1 md:grid-cols-2 gap-14">
      <!-- Experience Section -->
      <div>
        <h2 class="text-4xl font-bold mb-10 relative">
          Experience
          <span class="block w-6 h-1 bg-white mt-2 animate-pulse"></span>
        </h2>
        <div class="bg-[#121212] p-8 rounded-2xl border border-gray-800">
          <div
            v-for="(exp, i) in experience"
            :key="i"
            class="relative pl-8 mb-12 group"
            @mouseenter="animateLineGrow(i, 'exp')"
            @mouseleave="animateLineShrink(i, 'exp')"
          >
            <div
              class="absolute left-0 top-0 flex flex-col items-center"
              :ref="el => expLineRefs[i] = el"
            >
              <div class="w-3 h-3 bg-gray-400 rounded-full z-10 mt-2"></div>
              <div class="w-[2px] bg-gray-600 mt-1" style="height: 40px;"></div>
            </div>
            <img :src="exp.logo" alt="Company Logo" class="w-10 h-10 rounded-full object-cover border border-white shadow mb-4" v-if="exp.logo" />
            <p class="text-sm text-gray-400">{{ exp.date }}</p>
            <h3 class="text-xl font-semibold group-hover:ml-2 transition-all duration-300 flex items-center gap-2">
              {{ exp.title }}
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 transform group-hover:translate-y-1 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </h3>
            <p class="text-sm text-gray-400">{{ exp.description }}</p>
          </div>
        </div>
      </div>
  
      <!-- Education Section -->
      <div>
        <h2 class="text-4xl font-bold mb-10 relative">
          Education
          <span class="block w-6 h-1 bg-white mt-2 animate-pulse"></span>
        </h2>
        <div class="bg-[#121212] p-8 rounded-2xl border border-gray-800">
          <div
            v-for="(edu, i) in education"
            :key="i"
            class="relative pl-8 mb-12 group"
            @mouseenter="animateLineGrow(i, 'edu')"
            @mouseleave="animateLineShrink(i, 'edu')"
          >
            <div
              class="absolute left-0 top-0 flex flex-col items-center"
              :ref="el => eduLineRefs[i] = el"
            >
              <div class="w-3 h-3 bg-gray-400 rounded-full z-10 mt-2"></div>
              <div class="w-[2px] bg-gray-600 mt-1" style="height: 40px;"></div>
            </div>
            <img :src="edu.logo" alt="School Logo" class="w-10 h-10 rounded-full object-cover border border-white shadow mb-4" v-if="edu.logo" />
            <p class="text-sm text-gray-400">{{ edu.date }}</p>
            <h3 class="text-xl font-semibold group-hover:ml-2 transition-all duration-300 flex items-center gap-2">
              {{ edu.title }}
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 transform group-hover:translate-y-1 transition-transform duration-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </h3>
            <p class="text-sm text-gray-400">{{ edu.description }}</p>
          </div>
        </div>
      </div>
    </section>
  
    <!-- The Numbers Section -->
    <section class="bg-black text-white px-[15%] pb-24">
      <h2 class="text-4xl font-bold mb-10 relative">
        The Numbers
        <span class="block w-6 h-1 bg-white mt-2 animate-pulse"></span>
      </h2>
      <div class="bg-[#121212] rounded-2xl border border-gray-800 flex flex-wrap justify-between items-center px-10 py-12">
        <div class="text-center w-1/2 md:w-1/4 mb-8 md:mb-0">
          <p class="text-5xl font-bold">7+</p>
          <p class="text-gray-400 mt-2">Years of experience</p>
        </div>
        <div class="text-center w-1/2 md:w-1/4 mb-8 md:mb-0">
          <p class="text-5xl font-bold">10+</p>
          <p class="text-gray-400 mt-2">Social Media Accounts Managed</p>
        </div>
        <div class="text-center w-1/2 md:w-1/4 mb-8 md:mb-0">
          <p class="text-5xl font-bold">30+</p>
          <p class="text-gray-400 mt-2">Projects completed</p>
        </div>
        <div class="text-center w-1/2 md:w-1/4">
          <p class="text-5xl font-bold">40+</p>
          <p class="text-gray-400 mt-2">Happy clients</p>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { onMounted, nextTick, ref } from 'vue'
  import { gsap } from 'gsap'
  
  const experience = [
    {
      logo: 'https://tse4.mm.bing.net/th/id/OIP.-w8BCTEklWUAkWN3Szu8ugHaHa?r=0&rs=1&pid=ImgDetMain&o=7&rm=3',
      date: 'Dec 2024 – Present',
      title: 'Social Media Manager, Refresh Xpress',
      description: 'Created and managed campaigns that increased visibility and revenue, analyzed metrics, and developed tailored strategies.'
    },
    {
      logo: require('@/assets/logo.png'),
      date: '2024 – Present',
      title: 'Founder & Lead Developer, PhanTech',
      description: 'Founded a tech brand focused on WordPress, SEO, Django, and social strategies for digital transformation.'
    },
    {
    logo: 'https://tse2.mm.bing.net/th/id/OIP.fK3BMabmBELOKAqQ24KLLQAAAA?r=0&rs=1&pid=ImgDetMain&o=7&rm=3',
    date: '2023 – Present',
    title: 'Media Executive, International Humanity Foundation (IHF)',
    description: 'Created visual assets, edited video campaigns, and wrote compelling content to support global donor communication and storytelling.'
  },
    {
      logo: 'https://media-exp1.licdn.com/dms/image/C560BAQGx-blnFnLYpQ/company-logo_200_200/0/1558050446154?e=2159024400&v=beta&t=wuLEURufatsYGMHOW3aTXJAmTsa3GRgeRzwPfSrlVVU',
      date: 'Feb 2023 – Apr 2024',
      title: 'Junior Front-End Engineer, Mogedy Technologies',
      description: 'Collaborated across teams in 3 countries, delivered responsive UI using React, and led project features increasing productivity 40%.'
    }
  ]
  
  const education = [
    {
      logo: 'https://universitycompass.com/universities/assets/images/Godfrey-Okoye-University.JPG',
      date: '2019 – 2023',
      title: 'BSc. Computer Science, Godfrey Okoye University',
      description: 'Earned foundational and advanced knowledge in software engineering, databases, and system design.'
    }
  ]
  
  const expLineRefs = ref([])
  const eduLineRefs = ref([])
  
  const animateLineGrow = (index, type) => {
    const refArr = type === 'exp' ? expLineRefs.value : eduLineRefs.value
    const el = refArr[index]?.children?.[1]
    if (el) {
      gsap.to(el, {
        height: '100px',
        duration: 0.4,
        ease: 'power2.out'
      })
    }
  }
  
  const animateLineShrink = (index, type) => {
    const refArr = type === 'exp' ? expLineRefs.value : eduLineRefs.value
    const el = refArr[index]?.children?.[1]
    if (el) {
      gsap.to(el, {
        height: '40px',
        duration: 0.3,
        ease: 'power2.in'
      })
    }
  }
  
  onMounted(() => {
    nextTick(() => {
      gsap.from('.group', {
        opacity: 0,
        y: 30,
        duration: 0.6,
        stagger: 0.2,
        ease: 'power2.out'
      })
    })
  })
  </script>
  