<template>
  <button @click="toggleTheme" class="btn btn-ghost btn-circle">
    <!-- Switch to {{ isDark ? 'Light' : 'Dark' }} Mode -->
    <i :class="isDark ? 'fas fa-sun text-white' : 'fas fa-moon text-black'" class="text-2xl"></i>
  </button>
</template>

<script lang='ts' setup>

import { ref, onMounted } from 'vue';

const isDark = ref<boolean>(false);

onMounted(() => {
  const theme = localStorage.getItem('dark-theme');
  if(theme != null) {
    if (theme === 'light') {
      document.documentElement.setAttribute('data-theme', 'light')
      isDark.value = false
    }
    else {
      document.documentElement.setAttribute('data-theme', 'dark')
      isDark.value = true
    }
  }
  else {
    document.documentElement.setAttribute('data-theme', 'light')
  }
  // document.documentElement.dataset.theme = isDark.value ? 'dark' : 'light';
  // document.documentElement.setAttribute
});
const toggleTheme = () => {
  console.log("isDark", isDark.value)
  isDark.value = !isDark.value;
  // localStorage.setItem('dark-theme', isDark.value.toString());
  // document.documentElement.dataset.theme = isDark.value ? 'dark' : 'light';
  if (isDark.value)
  {
    document.documentElement.setAttribute('data-theme', 'dark')
    localStorage.setItem('dark-theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', 'light')
    localStorage.setItem('dark-theme', 'light');
  }
}

</script>
