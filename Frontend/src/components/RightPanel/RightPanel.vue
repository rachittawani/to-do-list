<template>
    <div class="flex flex-col justify-between bg-gray-100 rounded-lg h-full border border-black overflow-y-scroll">
        <div class="flex flex-col pt-3 px-5 gap-3">
            <div class="flex flex-row justify-between items-center">
                <p class="text-zinc-700 font-bold text-2xl">Task:</p>
                <i class="fas fa-times text-zinc-700 text-xl cursor-pointer" @click="closeTask"></i>
            </div>
            <input class="text-zinc-700 p-2 rounded-lg bg-transparent border border-black" autocomplete="off" placeholder='Task' v-model.lazy="newTaskObject.task"/>
            <textarea class="text-zinc-700 p-2 rounded-lg h-1/2 h-40 bg-transparent border border-black" autocomplete="off" placeholder='Description' maxlength="200" v-model="newTaskObject.description"></textarea>
            <div class="flex flex-row p-2 items-center gap-4">
                <p class="text-zinc-700 pr-10">List</p>
                <select class="w-1/2 rounded-lg bg-transparent text-zinc-700 p-2 border border-black outline-none" @change="setList($event)">
                    <option class="text-zinc-700 bg-gray-100" v-if="listObject.length === 0 || newTaskObject.list == ''" value="Select" selected>Select</option>
                    <option class="text-zinc-700 bg-gray-100" v-for="list in listObject" :key="list" :selected="list.name == newTaskObject.list">{{ list.name }}</option>
                </select>
            </div>
            <div class="flex flex-row p-2 items-center gap-4 ">
                <p class="text-zinc-700">Due Date</p>
                <input 
                    type="date" 
                    class="w-1/2 rounded-lg bg-transparent text-zinc-700 p-2 cursor-pointer border border-black outline-none"  
                    v-model="newTaskObject.dueDate"
                />
            </div>
        </div>
        <div class="flex flex-row justify-between p-4 gap-4">
            <button class="bg-transparent text-zinc-700 rounded-lg p-2 w-1/2 border border-black hover:bg-gray-300 hover:text-zinc-700">Delete Task</button>
            <button class="bg-slate-800 text-white border border-black rounded-lg p-2 w-1/2 hover:bg-slate-900 transition" @click="taskUpdated">Save Changes</button>
             <!-- px-4 py-2 rounded-lg hover:bg-slate-900 transition -->
        </div>
    </div>
</template>
<script setup lang="ts">
import { computed, defineEmits, defineProps, onBeforeMount, onMounted, ref } from 'vue';
import { List, Task } from '../../models/list.ts'
import { storeKey } from '../../store/store'
import { useStore } from 'vuex'

const emit = defineEmits(['taskClosed']);
const props = defineProps(['selectedTask']);
const listObject = ref<Array<List>>([]);
const taskObject = ref<Array<Task>>([]);
const store = useStore(storeKey);

onBeforeMount(() => {
    const data = JSON.parse(localStorage.getItem('listObject'))
    if(data!=undefined) {
        listObject.value = data;
    }
    else {
        listObject.value = []
    }
})

const onClick = () => {
    console.log("something changed")
}
const closeTask = () => {
    console.log(newTaskObject)
    emit('taskClosed', false)
}
const newTaskObject = computed(() => props.selectedTask)

const taskUpdated = () => {
    if(taskObject.value.length === 0)
    {
        newTaskObject.value.id = 1
    } else if(newTaskObject.value.id){
        newTaskObject.value.id = newTaskObject.value.id
    } else {
        newTaskObject.value.id = taskObject.value.length+1
    }
    
    const list = listObject.value.find((item) => {
        return item.name === newTaskObject.value.list
    })
    if(list!=undefined)
    {
        newTaskObject.value.listColor = list.hexCode
    }

    // taskObject.value.push(newTaskObject.value)
    // console.log("newTaskObject after saving", taskObject.value)
    // store.commit('taskMod/taskUpdatedStateMgt', newTaskObject.value)

    if(taskObject.value!=null || taskObject.value!=undefined) {
        let itemIndex: any;
        for(let i=0;i<taskObject.value.length;i++)
        {
            if(taskObject.value[i].id == newTaskObject.value.id)
            {
                itemIndex = i;
                break;
            }
            else{
                itemIndex = undefined;
            }
        }
        if(itemIndex != undefined) {
            taskObject.value.splice(itemIndex,1)
            taskObject.value.push(newTaskObject.value)
        }
        else {
            taskObject.value.push(newTaskObject.value)
        }
        localStorage.setItem('taskObject', JSON.stringify(taskObject.value));

    }
    else {
        const arr = []
        arr.push(newTaskObject.value)
        taskObject.value=arr
        localStorage.setItem('taskObject', JSON.stringify(taskObject.value));
    }
    emit('taskClosed', false)
}
const setList = (e) => {
    newTaskObject.value.list = e.target.value
}
onMounted(() => {
    const data = JSON.parse(localStorage.getItem('taskObject'))
    if(data!=undefined) {
        taskObject.value = data;
    }
    else {
        taskObject.value = []
    }
})
</script>
<style scoped>
textarea {
    resize: none;
}
::-webkit-calendar-picker-indicator {
    background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="15" viewBox="0 0 24 24"><path fill="%23000000" d="M20 3h-1V1h-2v2H7V1H5v2H4c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 18H4V8h16v13z"/></svg>');
}
</style>