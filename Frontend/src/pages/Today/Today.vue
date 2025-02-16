<template>
    <Tasks :nameOfHeading="value"/>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import Tasks from '../../components/Tasks/Tasks.vue'

const value = ref("To Do")

</script>
<style>
.customGrid{
    height: 100%;
}
</style>