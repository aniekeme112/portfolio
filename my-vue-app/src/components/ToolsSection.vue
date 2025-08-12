<template>
    <section class="bg-black text-white px-[15%] py-20">
      <h2 class="text-xl text-gray-400 mb-4">Tools</h2>
      <h1 class="text-4xl font-extrabold mb-12 leading-tight">
        <span class="block">THE KEY DESIGN AND</span>
        <span class="block text-white">DEVELOPMENT TOOLS I USE</span>
      </h1>
  
      <!-- Main Tools Grid -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
        <div
          v-for="(tool, i) in tools"
          :key="i"
          class="border border-gray-700 rounded-xl p-6 flex flex-col items-center hover:scale-105 transition-transform duration-300 ease-in-out"
        >
          <Icon :icon="tool.icon" class="text-3xl mb-4" />
          <p class="text-sm text-gray-300 uppercase tracking-wide">{{ tool.name }}</p>
        </div>
      </div>
  
      <!-- Development & Motion Sections -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-10">
        <div class="border border-gray-700 rounded-xl p-6">
          <h3 class="text-sm text-gray-400 mb-4 uppercase tracking-wide">Development</h3>
          <div class="flex gap-6 justify-center">
            <Icon v-for="(icon, i) in devIcons" :key="i" :icon="icon" class="text-2xl" />
          </div>
        </div>
        <div class="border border-gray-700 rounded-xl p-6">
          <h3 class="text-sm text-gray-400 mb-4 uppercase tracking-wide">Social Media</h3>
          <div class="flex gap-6 justify-center">
            <Icon v-for="(icon, i) in socialMediaicons" :key="i" :icon="icon" class="text-2xl" />
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
import { Icon } from '@iconify/vue'

const tools = [
  { name: 'Figma', icon: 'logos:figma' },
  { name: 'Python', icon: 'logos:python' },
  { name: 'Vue', icon: 'logos:vue' },
  { name: 'HTML5', icon: 'vscode-icons:file-type-html' },
  { name: 'Instagram', icon: 'logos:instagram-icon' },
  { name: 'Facebook', icon: 'logos:facebook' },
  { name: 'Slack', icon: 'logos:slack-icon' },
  { name: 'YouTube', icon: 'logos:youtube-icon' },
  { name: 'WordPress', icon: 'logos:wordpress-icon' },
  { name: 'React', icon: 'logos:react' },
  { name: 'Tailwind', icon: 'logos:tailwindcss-icon' },
  { name: 'X (Twitter)', icon: 'logos:x-twitter' }
]

const devIcons = [
  'logos:wordpress-icon',
  'logos:vue',
  'logos:visual-studio-code',
  'logos:python'
]

const socialMediaicons = [
  'logos:instagram-icon',
  'logos:x-twitter',
  'logos:facebook',
  'logos:youtube-icon',
  'logos:tiktok-icon'
]

  </script>
  