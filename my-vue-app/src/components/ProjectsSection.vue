<template>
    <section  ref="triggerSection" class="relative w-full h-[400vh] bg-black">
      <!-- Title -->
      <h1 class="text-white text-4xl font-bold text-center mt-8">Projects</h1>
  
    
  
      <!-- Pinned container -->
      <div ref="projectPin" class="sticky top-0 h-screen flex items-center justify-center overflow-hidden">
        <div class="w-full ml-[5%] mr-[5%] relative h-[70vh]">
          <div
            v-for="(slide, index) in slides"
            :key="index"
            :ref="el => projectCards[index] = el"
            class="project-card absolute top-0 left-0 w-full h-full bg-white rounded-xl shadow-lg p-6 text-black flex flex-col justify-start items-start"
            :style="{ opacity: index === 0 ? 1 : 0, zIndex: index === 0 ? 2 : 0 }"
          >
            <h3 class="text-2xl font-bold mb-2">{{ slide.title }}</h3>
            <p class="text-sm mb-4">{{ slide.description }}</p>
  
            <div class="w-full flex-1 rounded-md overflow-hidden border">
              <iframe
                :src="slide.link"
                frameborder="0"
                class="w-full h-full"
                allowfullscreen
                loading="lazy"
              ></iframe>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  import gsap from 'gsap'
  import { ScrollTrigger } from 'gsap/ScrollTrigger'
  
  gsap.registerPlugin(ScrollTrigger)
  
  export default {
    name: 'ProjectsSection',
    data() {
      return {
        slides: [
          {
            title: 'Kaklin Website',
            description: 'Corporate business site with clean design and booking system.',
            link: 'https://kaklin.com/'
          },
          {
            title: 'IHF Online',
            description: 'International NGO site for education, health, and volunteering.',
            link: 'https://ihfonline.org/'
          },
          {
            title: 'Hope Blessing Foundation',
            description: 'Non-profit organization focused on hope and community outreach.',
            link: 'https://hopeblessingfoundation.com/'
          },
          {
            title: 'BSA Management System',
            description: 'Internal business tool for asset and staff management.',
            link: 'https://dev.bsamanagementsystem.com/'
          }
        ],
        projectCards: []
      }
    },
    mounted() {
      this.$nextTick(() => {
        this.setupScrollAnimations()
        this.setupProgressIndicator()
      })
    },
    methods: {
      setupScrollAnimations() {
        this.projectCards.forEach((card, index) => {
          if (index !== 0) {
            gsap.set(card, { opacity: 0, zIndex: 0 })
          }
  
          ScrollTrigger.create({
            trigger: this.$refs.triggerSection,
            start: `${index * 100}vh top`,
            end: `${(index + 1) * 100}vh top`,
            scrub: true,
            onEnter: () => {
              gsap.to(card, {
                opacity: 1,
                zIndex: 2,
                duration: 1
              })
            },
            onLeave: () => {
              gsap.to(card, {
                opacity: 0,
                zIndex: 0,
                duration: 0.8
              })
            },
            onEnterBack: () => {
              gsap.to(card, {
                opacity: 1,
                zIndex: 2,
                duration: 1
              })
            },
            onLeaveBack: () => {
              gsap.to(card, {
                opacity: 0,
                zIndex: 0,
                duration: 0.8
              })
            }
          })
        })
      },
      setupProgressIndicator() {
        ScrollTrigger.create({
          trigger: this.$refs.triggerSection,
          start: 'top top',
          end: 'bottom bottom',
          scrub: true,
          onUpdate: (self) => {
            if (this.$refs.progressBar) {
              this.$refs.progressBar.style.width = `${(self.progress * 100).toFixed(1)}%`
            }
          }
        })
      }
    }
  }
  </script>
  
  <style scoped>
  .project-card {
    transition: all 0.5s ease;
  }
  iframe {
    height: 100%;
  }
  </style>
  