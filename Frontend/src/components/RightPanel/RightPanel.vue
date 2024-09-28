<template>
    <div class="flex flex-col justify-between bg-gray-100 rounded-lg h-full border border-black overflow-y-scroll">
        <div class="flex flex-col pt-3 px-5 gap-3">
            <div class="flex flex-row justify-between items-center">
                <p class="text-zinc-700 font-bold text-2xl">Task:</p>
                <i class="fas fa-times text-zinc-700 text-xl cursor-pointer" @click="closeTask"></i>
            </div>
            <input class="text-zinc-700 p-2 rounded-lg bg-transparent border border-black" autocomplete="off" placeholder='Task' v-model.lazy="newTaskObject.title"/>
            <textarea class="text-zinc-700 p-2 rounded-lg h-1/2 h-40 bg-transparent border border-black" autocomplete="off" placeholder='Description' maxlength="200" v-model="newTaskObject.description"></textarea>
            <div class="flex flex-row p-2 items-center gap-4">
                <p class="text-zinc-700">List</p>
                <select class="w-1/2 rounded-lg bg-transparent text-zinc-700 p-2 border border-black outline-none" v-model="selectedList">
                    <option class="text-zinc-700 bg-gray-100" value="Select" selected>Select</option>
                    <option class="text-zinc-700 bg-gray-100" v-for="list in listObject" :key="list.uuid" :value="list.uuid">{{ list.name }}</option>
                </select>
            </div>
            <div class="flex flex-row p-2 items-center gap-4">
                <p class="text-zinc-700">Priority</p>
                <!-- {{ rangeValue }} -->
                <div class="flex flex-col w-full">
                    <input type="range" min="0" max="100" v-model="rangeValue" class="range" step="25" />
                    <div class="flex w-full justify-between p-2 text-zinc-700">
                    <span v-for="n in 5" :key="n">
                        {{ n }}
                    </span>
                    </div>
                </div>
            </div>
            <div class="flex flex-row p-2 items-center gap-4">
                <p class="text-zinc-700">Due Date</p>
                <input 
                    type="date" 
                    class="w-1/2 rounded-lg bg-transparent text-zinc-700 p-2 cursor-pointer border border-black outline-none"  
                    v-model="newTaskObject.due_date"
                />
            </div>
        </div>
        <div class="flex flex-row justify-between p-4 gap-4">
            <button class="bg-transparent text-zinc-700 rounded-lg p-2 w-1/2 border border-black hover:bg-gray-300 hover:text-zinc-700" v-if="selectedTaskUuid" @click="deleteTask">Delete Task</button>
            <button class="bg-slate-800 text-white border border-black rounded-lg p-2 hover:bg-slate-900 transition" :class="selectedTaskUuid ? 'w-1/2' : 'w-full'" @click="taskUpdated">Save Changes</button>
        </div>
    </div>
</template>
<script setup lang="ts">
import { computed, defineEmits, defineProps, onBeforeMount, onMounted, ref, watch } from 'vue';
import { List } from '../../models/list.ts'
import { Task } from '../../models/task.ts';
import { storeKey } from '../../store/store'
import { useStore } from 'vuex'
import { createTodo, changeTodo, deleteTodo } from '../../utils/apiService/index';

const emit = defineEmits(['taskClosed']);
const props = defineProps(['selectedTask']);
const listObject = ref<Array>([]);
const taskObject = ref<Array<Task>>([]);
const selectedList = ref<string>('Select');
const selectedTaskUuid = ref<boolean>(false);
const store = useStore(storeKey);
const rangeValue = ref<Number>(1);

const newTaskObject = computed(() => props.selectedTask)

watch(() => {
    const data = JSON.parse(localStorage.getItem('listObject'));
    listObject.value = data ? data : [];

    rangeValue.value = (newTaskObject.value.priority-1)*25

    if (!newTaskObject.value.list_details) {
        selectedList.value = 'Select';
    } else {
        selectedList.value = newTaskObject.value.list_details['list_details_uuid'];
    }

    if(newTaskObject.value.uuid) {
        selectedTaskUuid.value = true
    } else {
        selectedTaskUuid.value = false
    }
});

const closeTask = () => {
    console.log(newTaskObject)
    emit('taskClosed', false)
}

const deleteTask = async() => {
    try{
        const response = await deleteTodo(newTaskObject.value.uuid);
        const status:number = response.status;
        const payload = response.data
        if (status == 204){
            emit('taskClosed', false)
        } 
    } catch (error: any) {
        console.log(error)
    }
}
const taskUpdated = async() => {
    console.log(newTaskObject.value)
    let data = {
        title: newTaskObject.value.title,
        description: newTaskObject.value.description,
        priority: (rangeValue.value/25)+1,
        due_date: newTaskObject.value.due_date,
        complete: false
    }
    console.log(selectedList.value)
    if(!(selectedList.value === 'Select')) {
        data['list_details_uuid'] = selectedList.value
    }

    console.log("data", data)

    if(newTaskObject.value.uuid)
    {
        try{
            const response = await changeTodo(newTaskObject.value.uuid, data);
            const status:number = response.status;
            const payload = response.data
            console.log("todo",payload)
            if (status == 204){
                emit('taskClosed', false)
            } 
        } catch (error: any) {
            console.log(error)
        }
    } else {
        try{
            const response = await createTodo(data);
            const status:number = response.status;
            const payload = response.data
            console.log("todo",payload)
            if (status == 201){
                emit('taskClosed', false)
            } 
        } catch (error: any) {
            console.log(error)
        }
    }
}
const setList = (e) => {
    console.log(e)
    newTaskObject.value.list_details_uuid = e.target.value
}
</script>
<style scoped>
textarea {
    resize: none;
}
::-webkit-calendar-picker-indicator {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="15" viewBox="0 0 24 24"><path fill="%23000000" d="M20 3h-1V1h-2v2H7V1H5v2H4c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 18H4V8h16v13z"/></svg>');
}
</style>