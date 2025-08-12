
<template>
  <div class="bg-[#151515] pt-28 md:pt-24">
    <MyNavbar />
    <HeroSECTION />
    <ServicePage />
    <ProjectsSection />
    <WorkPageComponent />
    <AboutMesection />
    <CVandExperience />
    <ToolsSection />
    <ProjectProgress />
    <ContactSection />
    <FooterSection />
  </div>
</template>

<script>
/* eslint-disable */
import MyNavbar from './components/MyNavbar.vue'
import HeroSECTION from './components/HeroSECTION.vue'
import ServicePage from './components/ServicePage.vue'
import ProjectsSection from './components/ProjectsSection.vue'
import WorkPageComponent from './components/WorkPageComponent.vue'
import AboutMesection from './components/AboutMesection.vue'
import CVandExperience from './components/CVandExperience.vue'
import ToolsSection from './components/ToolsSection.vue'
import ProjectProgress from './components/ProjectProgress.vue'
import ContactSection from './components/ContactSection.vue'
import FooterSection from './components/FooterSection.vue'

export default {
  components: {
    MyNavbar,
    HeroSECTION,
    ServicePage,
    ProjectsSection, 
    WorkPageComponent,
    AboutMesection,
    CVandExperience,
    ToolsSection,
    ProjectProgress,
    ContactSection,
    FooterSection
  }
}
// Detect if a link's href goes to the current page
function getSamePageAnchor (link) {
  if (
    link.protocol !== window.location.protocol ||
    link.host !== window.location.host ||
    link.pathname !== window.location.pathname ||
    link.search !== window.location.search
  ) {
    return false;
  }

  return link.hash;
}

// Scroll to a given hash, preventing the event given if there is one
function scrollToHash(hash, e) {
  const elem = hash ? document.querySelector(hash) : false;
  if(elem) {
    if(e) e.preventDefault();
    gsap.to(window, {scrollTo: elem});
  }
}

// If a link's href is within the current page, scroll to it instead
document.querySelectorAll('a[href]').forEach(a => {
  a.addEventListener('click', e => {
    scrollToHash(getSamePageAnchor(a), e);
  });
});

// Scroll to the element in the URL's hash on load
scrollToHash(window.location.hash);
</script>

<style>

</style>
