<template>
    <div v-if="toggle" class="flex flex-col bg-gray-100 rounded-lg h-full w-1/5 p-2 justify-between border border-black overflow-y-scroll">
        <div class="flex flex-col gap-3">
            <div class="flex flex-row justify-between p-2 items-center">
                <h1 class="text-2xl text-zinc-700 font-sans font-bold">Menu</h1>
                <i class="fas fa-bars text-zinc-700 cursor-pointer" @click="toggleMenu"></i>
            </div>
            <div class="relative">
                <input type="text" name="search" class="p-2 m-2 bg-white outline-none rounded-lg w-full pr-10 input-field border border-black" placeholder="Search"/>
                <i class="fas fa-search text-slate-700 absolute right-5 top-2" style="top: 50%; transform: translateY(-50%);"></i>
            </div>
            <h5 class="text-zinc-700 px-3 text-xs font-bold">TASKS</h5>
            <div>
                <ul class="flex flex-col gap-1 w-full rounded-box">
                    <li v-for="(tab, index) in tabs" :key="index" class="cursor-pointer rounded-lg p-2 hover:bg-gray-200 hover:text-zinc-700" :class="tab.value === activeTab ? 'bg-gray-300 text-zinc-900' : 'text-zinc-700'" @click="setActiveTab(tab.value)">
                        <span class="px-2 gap-3">
                            <i class="pl-2 pr-3 text-xs" :class="tab.icon"></i>{{tab.name}}
                        </span>
                    </li>
                </ul>
            </div>
            <hr class="flex border-zinc-300">
            <h5 class="text-zinc-700 px-3 text-xs font-bold">LISTS</h5>
            <div class="overflow-y-scroll overflow-x-hidden h-44">
                <div>
                    <h1 class="text-zinc-700 px-3 text-sm gap-2 cursor-pointer" @click="addNewList">
                        <i class="fas fa-plus text-zinc-700 text-xs pr-1"></i> Add New List
                    </h1>
                    <div v-if="listOpen" class="flex flex-col border border-black rounded-md p-2 pt-6 relative">
                        <i class="fas fa-times text-zinc-700 text-xs absolute top-2 right-2 cursor-pointer" @click="closeList"></i>
                        <div class="flex flex-row px-2 gap-2 border rounded-md items-center">
                            <div class="color-box rounded-sm cursor-pointer p-2" :style="{ backgroundColor: colorSelected }"></div>
                            <input type="text" name="list" autocomplete="off" class="w-full text-zinc-700 p-2 bg-transparent focus:outline-none text-sm" placeholder="List" v-model="listName" @keypress.enter="listDetails"/>  
                        </div>
                        <ColorPalette @customColor="clickedColor"/>
                    </div>
                </div>
                <ul class="flex flex-col gap-2 pt-2">
                    <li class="flex flex-row gap-2 items-center pl-4 cursor-pointer rounded-lg hover:bg-gray-200 hover:text-zinc-700" :class="activeTab === data.name ? 'bg-gray-300 text-zinc-900' : ''" v-for="(data, index) in listObject" :key="data.id" @click="selectedList(data)">
                        <div class="small-box rounded-sm p-2 h-1/2 " :style="{ backgroundColor: data.hex_color }"></div>
                        <p class="text-zinc-700 p-2">{{ data.name }}</p>
                    </li>
                </ul>
            </div>
        </div>
        <div class="flex flex-col">
            <div class="flex flex-row p-2 gap-2 items-center cursor-pointer rounded-lg hover:bg-gray-200 hover:text-zinc-700" @click="redirectToSettings" :class="activeTab === 'profile' ? 'bg-gray-300 text-zinc-900' : 'text-zinc-700'">
                <i class="fas fa-user text-zinc-700 text-xs"></i>
                <p>Profile</p>
            </div>
            <div class="flex flex-row p-2 gap-2 items-center cursor-pointer hover:bg-gray-200 hover:text-zinc-700" @click="redirectToLogin">
                <i class="fas fa-sign-out-alt text-zinc-700 text-xs"></i>
                <p class="text-zinc-700">Logout</p>
            </div>
        </div>
    </div>
    <div v-else class="p-2">
        <i class="fas fa-bars text-zinc-700 m-2 cursor-pointer" @click="toggleMenu"></i>
    </div>
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import ColorPalette from '../ColorPalette/ColorPalette.vue'
import { List } from '../../models/list'
import { defineEmits } from 'vue';
import Cookies from 'js-cookie';
import { getTodo, readLink } from '../../utils/apiService/index';

const router = useRouter();
const emit = defineEmits(['toggleSidePanel']);

const toggle = ref<boolean>(true)
const activeTab = ref<string>("today")
const listOpen = ref<boolean>(false)
const colorSelected = ref<string>("#000000")
const listName = ref<string>("")
const listObject = ref<Array<List>>([])

const tabs = 
[
    {
        name: 'Upcoming',
        value: 'upcoming',
        icon: 'fas fa-angle-double-right'
    },
    {
        name: 'Today',
        value: 'today',
        icon: 'fas fa-tasks'
    },
    {
        name: 'Sticky Wall',
        value: 'stickywall',
        icon: 'fas fa-sticky-note'
    }
]

const toggleMenu = () => {
    toggle.value = !toggle.value
    emit('toggleSidePanel', toggle.value)
}

const setActiveTab = (tab: string) => {
    activeTab.value = tab
    if(tab == 'today')
    {
        router.push('/home')
    } else {
        router.push('/home/'+tab)
    }
}
const addNewList = () => {
    listOpen.value = true
}
const closeList = () => {
    listOpen.value = false
}
const clickedColor = (data:any) => {
    colorSelected.value = data.hexCode
}
const listDetails = () => {
    const newList = {
        id: listObject.value.length + 1,
        name: listName.value,
        hexCode: colorSelected.value
    }
    listObject.value.push(newList)
    localStorage.setItem('listObject',JSON.stringify(listObject.value))
    listOpen.value = false
    listName.value = ''
    colorSelected.value = '#000000'
}
const redirectToSettings = () => {
    router.push("/home/profile")
    activeTab.value = 'profile'
}
const redirectToLogin = () => {
    Cookies.remove('token')
    Cookies.remove('tokenType')
    router.push("/login")
}
const selectedList = (selectedData: any) => {
    activeTab.value = selectedData.name
    router.push("/home/" + selectedData.id)
}
const getTodoDataForUser = async () => {
    try{
        const response = await getTodo();
        const status:number = response.status;
        const payload = response.data
        console.log("todo",payload)
        if (status == 200){
            router.push("/home")
        } 
    } catch (error: any) {
        console.log(error)
    }
}
const readLinkTags = async() => {
    try{
        const response = await readLink();
        const status:number = response.status;
        const payload = response.data
        console.log("linkTags",payload)
        if (status == 200){
            if(payload!=undefined) {
                listObject.value = payload;
                console.log(listObject.value)
            }
            else {
                listObject.value = []
            }
        } 
    } catch (error: any) {
        console.log(error)
    }
}
onMounted(() => {
    getTodoDataForUser()
    readLinkTags()
    // const data = JSON.parse(localStorage.getItem('listObject'))
    // if(data!=undefined) {
    //     listObject.value = data;
    // }
    // else {
    //     listObject.value = []
    // }
})
</script>
<style scoped>
.input-field {
    width: calc(100% - 15px);
}
.customLine{
    height: 1px;
    opacity: 1;
    background-color: rgb(221, 221, 221);
    border-radius: 12px;
}
.color-box {
    width: 20px;
    height: 20px;
}
.small-box{
    width: 10px;
    height: 10px;
}
</style>
