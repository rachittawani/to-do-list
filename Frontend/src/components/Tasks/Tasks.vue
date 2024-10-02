<template>
    <div class="customGrid flex flex-row gap-2">
        <Toast :toastDetails="toastDetailsValue" v-if="toastVisible" @toastClose="closeToast"/>
        <div class="flex flex-col gap-3 px-2" :class="rightToggle == true ? 'w-2/3': 'w-full'">
            <p class="text-5xl font-bold pb-5">{{ props.nameOfHeading }}</p>
            <div class="flex">
                <button class="btn btn-wide rounded-lg border border-black cursor-pointer bg-gray-100 text-zinc-600 hover:bg-gray-300" @click="addNewTask">
                    <i class="fas fa-plus text-xs"></i>
                    <span class="text-sm">Add New Task</span>
                </button>
            </div>
            <div class="flex flex-col justify-between bg-gray-100 rounded-lg border border-black" v-if="!isLoading" v-for="(task) in tasks" @click="showTask(task)">
                <div class="flex flex-row justify-between cursor-pointer p-2 pb-4">
                    <div class="flex flex-row items-start gap-4">
                        <div class="p-2">
                            <input type="checkbox" class="flex checkbox checkbox-ms border-black hover:border-black checked:border-black">
                        </div>
                        <div class="flex flex-col gap-2">
                            <p class="text-zinc-600 text-md">{{ task.title }}</p>
                            <div class="flex flex-row gap-5">
                                <div v-if="task.due_date" class="flex flex-row gap-2 items-center">
                                    <i class="fas fa-calendar-times text-zinc-600 text-md"></i>
                                    <p class="text-zinc-600 text-sm">{{ task.due_date }}</p>
                                    <div class="verticalLine ml-3" v-if="task.list_details"></div>
                                </div>
                               
                                <div v-if="task.list_details" class="flex flex-row gap-2 items-center">
                                    <div :style="{ backgroundColor: task.list_details['hex_color'] }" class="colorBox rounded-sm cursor-pointer"></div>
                                    <p class="text-zinc-600 text-sm">{{ task.list_details['name'] }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <i class="fas fa-angle-right text-zinc-600 text-lg"></i>
                    </div>
                </div>
            </div>
            <div class="flex justify-center items-center h-full" v-else>
                <span class="loading loading-bars loading-lg"></span>
            </div>
        </div>
        <div v-if="rightToggle" class="h-full w-1/3 px-2">
            <RightPanel @taskClosed="closingPanel" :selectedTask="taskSelected"/>
        </div>
    </div>
</template>
<script setup lang="ts">
import { ref, defineProps, onMounted, computed } from 'vue';
import RightPanel from '../RightPanel/RightPanel.vue'
import { Task } from '../../models/task.ts'
import { getTodo } from '../../utils/apiService/index';
import ToastModel from '../../models/toast.ts';
import Toast from '../../components/Toast/Toast.vue'

const rightToggle = ref<boolean>(false)
const taskSelected = ref<Task>({})
const props = defineProps(['nameOfHeading']);
const tasks = ref<Array<Task>>([])
const isLoading = ref<boolean>(false)
const toastVisible = ref<boolen>(false)
const toastDetailsValue = ref<ToastModel>({})

const getTodoDataForUser = async () => {
    isLoading.value = true
    try{
        const response = await getTodo();
        const status:number = response.status;
        const payload = response.data
        console.log("todo",payload)
        if (status == 200){
            tasks.value = payload
            isLoading.value = false
            toastDetailsValue.value.name = 'success'
            toastDetailsValue.value.msg = 'Fetch all todos!!!'
            toastVisible.value = true
        } 
    } catch (error: any) {
        isLoading.value = false
        toastDetailsValue.value.name = 'error'
        toastDetailsValue.value.msg = 'Could not fetch todos!!!'
        toastVisible.value = true
    }
}

const closeToast = (closeingToast: boolean) => {
    toastVisible.value = closeingToast
    console.log("close", toastVisible.value)
}

onMounted(() => {
    getTodoDataForUser()
})
// const tasks = computed(() => store.getters['taskMod/newTask'])
const addNewTask = () => {
    rightToggle.value = true
    taskSelected.value = {
        title: '',
        description: '',
        list_details_uuid: '',
        priority: 0,
        due_date: '',
        complete: false
    }
}
const closingPanel = (closed: any) => {
    getTodoDataForUser()
    rightToggle.value = closed
}
const showTask = (task: any) => {
    taskSelected.value = task
    rightToggle.value = true
}
</script>
<style scoped>
.customGrid{
    height: 100%
}
.colorBox {
    width: 14px;
    height: 14px;
}
.verticalLine{
    border-left: 1px solid black;
    height: 20px;
}
</style>