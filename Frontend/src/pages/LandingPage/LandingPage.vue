<template>
    <div class="customGrid flex flex-row p-5 gap-4">
        <img class="h-full w-1/2 rounded-2xl object-cover border border-slate-500" src="/src/assets/landingPage.jpg" alt="Landing Page" >
        <div class="flex flex-col px-28 justify-center w-1/2 h-full rounded-2xl border border-slate-500">
            <h1 class="text-center font-bold font-sans text-4xl p-2">Task Tracker</h1>
            <h2 class="text-center font-bold font-sans text-lg pb-4">Track Your Tasks, Conquer Your Goals!!!</h2>
            <p class="flex text-justify whitespace-normal font-sans mx-2 my-5">
                Introducing our sleek webapp, a dynamic solution for your productivity needs. Seamlessly manage tasks with our 
                intuitive to-do list feature. Stay organized with customizable categories, priorities, and due dates. Experience 
                efficiency like never before with our user-friendly interface. 
            </p>
            <div class="flex justify-center">
                <button 
                    type="button" 
                    class="w-1/2 bg-amber-400 text-slate-900 font-bold font-sans rounded-lg flex justify-center m-2 p-2" 
                    @click="redirectToSignUp">Get Started
                </button>
            </div>
            <p class="flex font-bold font-sans justify-center m-2">Already have an account?<button @click="redirectToLogin" class="text-red-500">&nbsp;Login</button></p>
        </div>
    </div>
</template>
<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const redirectToLogin = () => {
    router.push("/login")
}
const redirectToSignUp = () => {
    router.push("/signup")
}

</script>
<style>
.customGrid{
    height: 100%;
}
.customLine{
    height: 1px;
    opacity: 1;
    background-color: rgb(221, 221, 221);
    border-radius: 12px;
}
</style>
