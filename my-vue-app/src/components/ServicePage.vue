<template>
  <div id="skills" ref="root" class="bg-black">
    <!-- Section Heading -->
    <div class="grid grid-cols-1 md:grid-cols-1 lg:grid-cols-2 gap-4 text-white pb-[5%] px-[13%] pt-[5%]">
      <div>
        <h3 class="text-2xl semibold font-serif bg-gradient-to-r from-white to-gray-300 text-transparent bg-clip-text">
          What I do
        </h3>
      </div>
      <div>
        <h1 class="text-4xl bold font-serif bg-gradient-to-r from-white to-gray-300 text-transparent bg-clip-text font-black">
          Digital Product Design Services I Offer
        </h1>
      </div>
    </div>

    <!-- Cards Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-4 text-white px-[13%] pb-[5%]">
      <div
        v-for="(service, index) in services"
        :key="index"
        class="group grid divBorder grid-cols-1 md:grid-cols-2 gap-4 text-white p-6 rounded-lg border border-white/10"
      >
        <!-- Icon and Title -->
        <div class="flex items-start gap-4">
          <Icon :icon="service.icon" class="text-white" width="32" height="32" />
          <div class="text-white text-2xl font-semibold">{{ service.title }}</div>
        </div>

        <!-- Arrow Icon -->
        <div
          class="flex ml-auto items-center justify-center w-12 h-12 rounded-full border border-white transition-all duration-300 group-hover:bg-white transform rotate-[-45deg] group-hover:rotate-0"
        >
          <Icon
            :icon="service.arrowIcon"
            width="24"
            height="24"
            class="text-white transition-colors duration-300 group-hover:text-black"
          />
        </div>

        <!-- Description -->
        <div class="col-span-full text-white/80 text-base leading-relaxed">
          {{ service.description }}
        </div>

        <!-- Pills -->
        <div class="col-span-full flex flex-wrap gap-3">
          <span
            v-for="(pill, i) in service.pills"
            :key="i"
  class="px-4 border-button py-2 rounded-full text-sm text-white bg-gradient-to-br from-grey-500 to-black-900 bg-opacity-30 border border-white/10 backdrop-blur-sm shadow-inner"
          >
            {{ pill }}
          </span>
        </div>
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

const root = ref(null)

const services = [
  {
    title: 'Full Stack Development',
    icon: 'arcticons:star-tv',
    arrowIcon: 'qlementine-icons:arrow-right-24',
description: `Building dynamic, scalable, and efficient digital solutions using both frontend and backend technologies, ensuring seamless integration and optimal performance across platforms`,
    pills: ['Frontend & Backend Development', 'Performance Optimization', 'API Integration', 'Database Management']


  },
  {
    title: 'Social Media Management',
    icon: 'tabler:social',
    arrowIcon: 'qlementine-icons:arrow-right-24',
    description:
      'Crafting and executing strategies to build community, grow audiences, and drive engagement across platforms through consistent and authentic brand messaging.',
    pills: ['Platform Strategy', 'Analytics & Reporting', 'Analytics & Reporting', 'Audience Engagement']
  },
  {
    title: 'Content Creation',
    icon: 'hugeicons:creative-market',
    arrowIcon: 'qlementine-icons:arrow-right-24',
    description:
      'Developing creative content that communicates value, tells stories, and connects with the target audience through visuals, text, and media across digital platforms.',
    pills: ['Copywriting\u2002', 'Visual Content', 'Storytelling\u2002', 'Campaign Design']
  },
  {
    title: 'Tech Consulting & Project Leadership',
    icon: 'fluent-emoji-high-contrast:package',
    arrowIcon: 'qlementine-icons:arrow-right-24',
    description:
      'Providing tailored technical solutions and overseeing project lifecycles\u2014from concept to deployment\u2014while aligning business goals with efficient, scalable systems and collaborative workflows.',
    pills: [
  "Technical Strategy",
  "Project Management",
  "Volunteer Coordination",
  "Digital Transformation",
  "Remote Team Leadership"
]
  }
]

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
.divBorder {
  border: 1px solid #ffffff;
  padding: 20px;
  border-radius: 10px;
  transition: transform 0.3s ease;
}
.divBorder:hover {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  background-color: rgba(43, 38, 38, 0.725);
}
.icon-wrapper {
  transition: transform 0.3s ease, color 0.3s ease;
  transform: rotate(-45deg);
}
.icon-wrapper:hover {
  transform: rotate(0deg);
}
.border-button {
  border: 2px solid #232121;
  cursor: pointer;
}
</style>
