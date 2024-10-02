<template>
    <transition name="slide-out-right">
    <div v-if="isVisible" class="toast">
        <div role="alert" class="alert" :class="{
            'alert-error': toast.toastDetails.name === 'error', 
            'alert-success': toast.toastDetails.name === 'success', 
            'alert-warning': toast.toastDetails.name === 'warning'
        }">
            <div class="flex items-center gap-4">
                <i :class="{
                    'fas fa-times-circle': toast.toastDetails.name === 'error',
                    'fas fa-check-circle': toast.toastDetails.name === 'success',
                    'fas fa-exclamation-triangle': toast.toastDetails.name === 'warning'
                }"></i>
                <span>{{ toast.toastDetails.msg }}</span>
            </div>
            <div class="cursor-pointer flex flex-start relative">
                <i class="fas fa-times-circle text-xs" @click="closeToast"></i>
            </div>
        </div>
    </div>
</transition>
</template>
<script setup lang="ts">
import { ref, defineProps, defineEmits, onMounted } from 'vue';
// import Toast from '../../models/toast'

// const toast = ref<Toast>({})
const toast = defineProps(['toastDetails']);
const emit = defineEmits(['toastClose']);
const isVisible = ref(true);

onMounted(()=>{
    setTimeout(() => {
        isVisible.value = false;
        setTimeout(() => {
            emit('toastClose', false);
        }, 300);  // Slight delay for animation to complete before emitting
    }, 3000);
})

const closeToast = () => {
    isVisible.value = false;
    setTimeout(() => {
        emit('toastClose', false);
    }, 300);  // Ensure animation completes before emitting
};
</script>

<style scoped>
/* Slide out to the right animation */
.slide-out-right-enter-active, .slide-out-right-leave-active {
    transition: transform 0.3s ease, opacity 0.3s ease;
}

.slide-out-right-enter-from, .slide-out-right-leave-to {
    transform: translateX(100%);
    opacity: 0;
}

.slide-out-right-enter-to, .slide-out-right-leave-from {
    transform: translateX(0);
    opacity: 1;
}
</style>