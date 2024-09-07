<template>
    <div class="customGrid flex flex-row gap-2">
        <div class="flex flex-col gap-3 px-2" :class="rightToggle == true ? 'w-2/3': 'w-full'">
            <p class="text-5xl font-bold pb-5">{{ props.nameOfHeading }}</p>
            <div class="flex">
                <button class="btn btn-wide rounded-lg border border-black cursor-pointer bg-gray-100 text-zinc-600 hover:bg-gray-300" @click="addNewTask">
                    <i class="fas fa-plus text-xs"></i>
                    <span class="text-sm">Add New Task</span>
                </button>
            </div>
            <div class="flex flex-col justify-between bg-gray-100 rounded-lg border border-black" v-for="(dummyTask, index) in dummyTasks" @click="showTask(dummyTask)">
                <div class="flex flex-row justify-between cursor-pointer p-2 pb-4">
                    <div class="flex flex-row items-start gap-4">
                        <div class="p-2">
                            <input type="checkbox" class="flex checkbox checkbox-ms border-black hover:border-black checked:border-black">
                        </div>
                        <div class="flex flex-col gap-2">
                            <p class="text-zinc-600 text-md">{{ dummyTask.task }}</p>
                            <div class="flex flex-row gap-5">
                                <div v-if="dummyTask.dueDate" class="flex flex-row gap-2 items-center">
                                    <i class="fas fa-calendar-times text-zinc-600 text-md"></i>
                                    <p class="text-zinc-600 text-sm">{{ dummyTask.dueDate }}</p>
                                    <div class="verticalLine ml-3" v-if="dummyTask.list"></div>
                                </div>
                               
                                <div v-if="dummyTask.list" class="flex flex-row gap-2 items-center">
                                    <div :style="{ backgroundColor: dummyTask.listColor }" class="colorBox rounded-sm cursor-pointer"></div>
                                    <p class="text-zinc-600 text-sm">{{ dummyTask.list }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <i class="fas fa-angle-right text-zinc-600 text-lg"></i>
                    </div>
                </div>
                <div v-if="dummyTasks.length-1 != index">
                    <hr class="border border-slate-400">
                </div>
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
// import { dummyTasks } from '../../utils/Dummy'
import { Task } from '../../models/task.ts'

const rightToggle = ref<boolean>(false)
const taskSelected = ref<Task>({})
const props = defineProps(['nameOfHeading']);
const dummyTasks = ref<Array<Task>>([])

onMounted(() => {
    const data = JSON.parse(localStorage.getItem('taskObject'))
    if(data!=undefined) {
        dummyTasks.value = data;
    }
    else {
        dummyTasks.value = []
    }
})
// const dummyTasks = computed(() => store.getters['taskMod/newTask'])
const addNewTask = () => {
    rightToggle.value = true
    taskSelected.value = {
        id: 0,
        task: '',
        description: '',
        list: '',
        listColor: '',
        dueDate: ''
    }
}
const closingPanel = (closed:any) => {
    const data = JSON.parse(localStorage.getItem('taskObject'))
    if(data!=undefined) {
        dummyTasks.value = data;
    }
    else {
        dummyTasks.value = []
    }
    rightToggle.value = closed
}
const showTask = (dumTask) => {
    // taskSelected.value = dummyTasks.value.find(item => item.id === id)
    taskSelected.value = dumTask
    console.log(taskSelected.value)
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