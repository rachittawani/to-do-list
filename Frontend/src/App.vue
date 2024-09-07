<template>
  <div class="h-full w-full">
    <div class="absolute right-5 top-2">
      <Theme />
    </div>
    <div class="pt-10 h-full w-full">
    <router-view></router-view>
    </div>
  </div>
</template>

<script setup lang="ts">
import Theme from './components/Theme/Theme.vue'
</script>

<!-- <style scoped>
:root[data-theme='light'] {
  --background-color: white;
  --text-color: black;
}

:root[data-theme='dark'] {
  --background-color: black;
  --text-color: white;
}

body {
  background-color: var(--background-color);
  color: var(--text-color);
}
</style> -->