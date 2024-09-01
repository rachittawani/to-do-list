<template>
    <div class="customGrid flex flex-row p-5 gap-4">
        <SidePanel @toggleSidePanel="toggleClosed"/>
        <div class="rounded-lg" :class="toggle === false ? 'w-4/5' : 'w-full'">
            <router-view></router-view>
        </div>
    </div>
</template>
<script setup lang="ts">
import SidePanel from '../../components/SidePanel/SidePanel.vue'
import { ref } from 'vue';

const toggle = ref<boolen>(false)

const toggleClosed = (listOpen: boolean) => {
    toggle.value = !listOpen
}
</script>
<style>
.customGrid{
    height: 100%;
}
</style>
