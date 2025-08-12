<template>
    <section  class="bg-black text-white px-[5%] md:px-[15%] py-24" id="contact">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-start" v-motion-fade-visible>
        <!-- Left Info -->
        <div>
          <p class="text-gray-400 text-sm mb-2">Contact Me</p>
          <h2 class="text-4xl font-extrabold mb-6 leading-tight">
            LET'S TALK ABOUT<br />YOUR PROJECT
          </h2>
          <p class="text-gray-400 mb-6">
            Let's embark on a creative journey together by shaping a visual narrative of your brand in the crowded digital space.
          </p>
  
          <!-- Call -->
          <div class="flex items-center gap-4 bg-[#111] p-4 rounded-lg border border-gray-700 mb-4 hover:bg-white hover:text-black transition duration-300">
            <img :src="Headerimage" class="w-10 h-10 rounded-full" />
            <div>
              <p class="text-sm font-semibold">BOOK A CALL</p>
<a href="tel:+2349071641796" class="text-sm text-gray-400 hover:underline">
  +234 9071641796
</a>
            </div>
          </div>
  
          <!-- Email -->
          <div class="flex items-center gap-4 bg-[#111] p-4 rounded-lg border border-gray-700 hover:bg-white hover:text-black transition duration-300">
            <Icon icon="mdi:email-outline" class="w-6 h-6" />
            <div>
              <p class="text-sm font-semibold">PREFER EMAIL COMMUNICATION</p>
<a href="mailto:aniekemeudoeong@gmail.com" class="text-sm text-gray-400 hover:underline">
  aniekemeudoeong@gmail.com
</a>            </div>
          </div>
        </div>
  
        <!-- Right Form -->
        <form @submit.prevent="sendMessage" class="space-y-6 bg-[#111] p-6 rounded-lg border border-gray-700">
          <input v-model="form.name" type="text" placeholder="John Doe" required class="w-full px-4 py-3 bg-black text-white border border-gray-600 rounded-lg focus:outline-none focus:border-white" />
          <input v-model="form.email" type="email" placeholder="hello@example.com" required class="w-full px-4 py-3 bg-black text-white border border-gray-600 rounded-lg focus:outline-none focus:border-white" />
          <input v-model="form.subject" type="text" placeholder="Subject" required class="w-full px-4 py-3 bg-black text-white border border-gray-600 rounded-lg focus:outline-none focus:border-white" />
          <textarea v-model="form.message" rows="5" placeholder="Message in brief..." required class="w-full px-4 py-3 bg-black text-white border border-gray-600 rounded-lg focus:outline-none focus:border-white"></textarea>
          <button type="submit" class="w-full py-3 bg-white text-black rounded-lg font-bold hover:bg-gray-300 transition">
            SEND MESSAGE
          </button>
        </form>
      </div>
    </section>
  </template>
  
  <script setup>
 import { Icon } from '@iconify/vue'
import emailjs from '@emailjs/browser'
import { ref } from 'vue'
import Headerimage from '../assets/Headerrr.jpg'

const form = ref({
  name: '',
  email: '',
  subject: '',
  message: ''
})

const sendMessage = () => {
  emailjs.send(
    "service_9qhxn8c",          //  Your Service ID
    "template_xfkhold",         //  Your Template ID
    {
      from_name: form.value.name,
      from_email: form.value.email,
      subject: form.value.subject,
      message: form.value.message
    },
    "kIDaGdDDHkLkNV61u"         //  Your User ID
  )
  .then(() => {
    alert("Message sent successfully!")
    form.value = { name: '', email: '', subject: '', message: '' }
  })
  .catch((err) => {
    console.error(err)
    alert("Failed to send message. Please try again.")
  })
}

  </script>
  
  <style scoped>
  input,
  textarea {
    transition: all 0.3s ease;
  }
  </style>
  