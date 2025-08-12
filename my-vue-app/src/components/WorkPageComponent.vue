<template>
  <section id="projects" class="bg-black text-white py-16 text-center">
    <!-- Subheading -->
    <p class="text-xl mb-2 text-gray-300">Works</p>

    <!-- Main Heading -->
    <h2 class="text-5xl font-extrabold mb-10">FEATURED PROJECTS</h2>

    <!-- Filter Tabs -->
    <div class="flex justify-center flex-wrap gap-6 mb-10">
      <label
        v-for="filter in filters"
        :key="filter"
        class="flex items-center gap-2 cursor-pointer"
      >
        <input
          type="radio"
          name="projectFilter"
          class="accent-white w-4 h-4"
          :value="filter"
          v-model="selectedFilter"
        />
        <span
          :class="{
            'text-white font-bold': selectedFilter === filter,
            'text-gray-400': selectedFilter !== filter
          }"
        >
          {{ filter }}
        </span>
      </label>
    </div>

    <!-- Project Grid -->
    <div
      ref="projectGrid"
      class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto"
    >
      <a
        v-for="project in filteredProjects"
        :key="project.id"
        :href="project.link || '#'"
        target="_blank"
        class="relative rounded-2xl overflow-hidden shadow-md transform transition-transform duration-500 hover:scale-105 hover:shadow-xl group"
      >
        <img
          :src="project.image"
          alt="project image"
          class="w-full h-60 object-cover transition duration-300 group-hover:brightness-75 group-hover:scale-105"
        />
        <div class="p-4 bg-black text-white">
          <p class="text-sm text-gray-400">{{ project.category }}</p>
          <h3 class="text-xl font-bold group-hover:underline">{{ project.title }}</h3>
        </div>

        <!-- Hover Overlay -->
        <div
          class="absolute inset-0 flex items-end justify-start p-6 opacity-0 group-hover:opacity-100 transition duration-300 bg-black bg-opacity-60"
        >
          <span class="text-white font-semibold tracking-wide flex items-center gap-2">
            VIEW PROJECT
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-4 w-4"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M17 8l4 4m0 0l-4 4m4-4H3"
              />
            </svg>
          </span>
        </div>
      </a>
    </div>
  </section>
</template>

<script>
import gsap from 'gsap';

export default {
  name: "FeaturedProjectsSection",
  data() {
    return {
      filters: ["ALL", "WEBSITE", "SOCIAL MEDIA", "MARKETING", "APP"],
      selectedFilter: "ALL",
      projects: [],
      socket: null
    };
  },
  computed: {
    filteredProjects() {
      if (this.selectedFilter === 'ALL') return this.projects;
      return this.projects.filter(p => p.category === this.selectedFilter);
    }
  },
  watch: {
    filteredProjects() {
      this.$nextTick(() => {
        gsap.fromTo(
          this.$refs.projectGrid.children,
          { opacity: 0, y: 30 },
          { opacity: 1, y: 0, duration: 0.8, stagger: 0.1 }
        );
      });
    }
  },
  created() {
    // Initial load of existing projects
    fetch('http://127.0.0.1:8000/api/projects/')
      .then(res => res.json())
      .then(data => {
        this.projects = data;
      })
      .catch(error => {
        console.error("Failed to fetch projects:", error);
      });
  },
  mounted() {
    // WebSocket connection for live updates
    this.socket = new WebSocket("ws://127.0.0.1:8000/ws/projects/");
    this.socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log("Realtime update:", data);

      // Add new project to the list
      this.projects.unshift(data.content);  // adds it to the top
    };
    this.socket.onerror = (err) => {
      console.error("WebSocket error:", err);
    };
  },
  beforeUnmount() {
    // Clean up socket
    if (this.socket) {
      this.socket.close();
    }
  }
};
</script>


<style scoped>
input[type="radio"] {
  appearance: none;
  border: 2px solid #888;
  border-radius: 50%;
  width: 16px;
  height: 16px;
  position: relative;
}

input[type="radio"]:checked::before {
  content: '';
  position: absolute;
  top: 2px;
  left: 2px;
  width: 8px;
  height: 8px;
  background: white;
  border-radius: 50%;
}
</style>
