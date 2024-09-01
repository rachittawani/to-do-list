<template>
    <div class="color-palette p-4">
        <div
            v-for="(color, index) in colors"
            :key="index"
            :style="{ backgroundColor: color.hexCode }"
            class="color-box rounded-sm cursor-pointer m-1"
            @click="clickedColor(color)"
        ></div>
    </div>
</template>
<script setup lang="ts">
import { defineEmits } from 'vue';
import { colors } from '../../utils/Colors.ts'

const emit = defineEmits(['customColor']);

const clickedColor = (color) => {
  emit('customColor', color)
}
</script>
<style>
.color-palette {
  display: flex;
  flex-wrap: wrap;
}
.color-box {
  width: 15px;
  height: 15px;
}
</style>