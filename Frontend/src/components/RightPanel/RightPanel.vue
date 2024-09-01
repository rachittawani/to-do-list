<template>
    <div class="flex flex-col justify-between bg-gray-100 rounded-lg h-full">
        <div class="flex flex-col pt-3 px-5 gap-3">
            <div class="flex flex-row justify-between items-center">
                <p class="text-zinc-600 font-bold text-2xl">Task:</p>
                <i class="fas fa-times text-zinc-600 text-xl cursor-pointer" @click="closeTask"></i>
            </div>
            <!-- <p class="text-black">{{ props.selectedTask.task }}</p> -->
            <input class="text-zinc-600 p-2 rounded-lg outline-none bg-transparent border-2" autocomplete="off" placeholder='Task' v-model.lazy="newTaskObject.task"/>
            <textarea class="text-zinc-600 p-2 rounded-lg h-1/2 outline-none h-40 bg-transparent border-2" autocomplete="off" placeholder='Description' maxlength="200" v-model="newTaskObject.description"></textarea>
            <div class="flex flex-row p-2 items-center gap-4">
                <p class="text-zinc-600 pr-10">List</p>
                <select class="w-1/2 border rounded-lg bg-transparent text-zinc-600 p-2 outline-none" @change="setList($event)">
                    <option class="text-zinc-600 bg-gray-100" v-if="listObject.length === 0 || newTaskObject.list == ''" value="Select" selected>Select</option>
                    <option class="text-zinc-600 bg-gray-100" v-for="list in listObject" :key="list" :selected="list.name == newTaskObject.list">{{ list.name }}</option>
                </select>
            </div>
            <div class="flex flex-row p-2 items-center gap-4">
                <p class="text-zinc-600">Due Date</p>
                <input type="date" class="w-1/2 border rounded-lg bg-transparent text-zinc-600 p-2 outline-none cursor-pointer"  v-model="newTaskObject.dueDate"/>
            </div>
        </div>
        <div class="flex flex-row justify-between p-4 gap-4">
            <button class="bg-transparent text-zinc-600 border-2 rounded-lg p-2 w-1/2 hover:bg-gray-300 hover:text-zinc-700">Delete Task</button>
            <button class="bg-yellow-400 text-zinc-600 border rounded-lg p-2 w-1/2 hover:bg-yellow-500 hover:text-zinc-700" @click="taskUpdated">Save Changes</button>
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
</style>