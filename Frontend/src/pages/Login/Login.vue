<template>
    <div class="customGrid flex flex-row p-5 gap-4">
        <img class="h-full w-1/2 rounded-2xl object-cover" src="/src/assets/landingPage.jpg" alt="Landing Page" >
        <div class="flex flex-col px-28 justify-center w-1/2 h-full rounded-2xl border border-slate-950">
            <h1 class="text-black font-bold font-sans text-4xl m-2">Login</h1>
            <form action="POST" class="flex flex-col">
                <input type="text" name="username" autocomplete="off" class="rounded-lg bg-white outline-none border border-slate-950 text-black m-2 p-2 input-field" placeholder="Username"/>
                <input type="password" name="password" autocomplete="off" class="rounded-lg bg-white outline-none border border-slate-950 text-black m-2 p-2 input-field" placeholder="Password"/>
                <button type="button" class="bg-yellow-400 text-slate-800 font-bold font-sans rounded-lg flex justify-center m-2 p-2" @click="redirectToHome">Login</button>
            </form>
            <div class="flex flex-row">
                <hr class="customLine w-1/2 my-3 mx-2">
                <p class="text-slate-700 font-sans">or</p>
                <hr class="customLine w-1/2 my-3 mx-2">
            </div>
            <div class="flex flex-row">
                <button type="button" class="bg-gray-300 text-slate-800 font-bold font-sans rounded-lg flex justify-center m-2 p-2 w-1/2">Google</button>
                <button type="button" class="bg-gray-300 text-slate-800 font-bold font-sans rounded-lg flex justify-center m-2 p-2 w-1/2">Facebook</button>
            </div>
            <p class="flex text-gray-700 font-bold font-sans justify-center m-2">Don't have an account?<button @click="redirectToSignUp" class="text-red-500">&nbsp;Sign up</button></p>
        </div>
    </div>
</template>
<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const redirectToSignUp = () => {
    router.push("/signup")
}
const redirectToHome = () => {
    router.push("/home")
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
