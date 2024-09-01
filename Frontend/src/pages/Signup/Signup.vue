<template>
    <div class="customGrid flex flex-row p-5 gap-4">
        <img class="h-full w-1/2 rounded-2xl object-cover" src="/src/assets/landingPage.jpg" alt="Landing Page" >
        <div class="flex flex-col px-28 justify-center w-1/2 h-full rounded-2xl border border-slate-950">
            <h1 class="text-black font-bold font-sans text-4xl m-2">Sign up</h1>
            <form action="POST" class="flex flex-col">
                <div class="flex flex-row">
                    <input 
                        type="text" 
                        name="input-field" 
                        autocomplete="off" 
                        class="rounded-lg bg-white outline-none border border-slate-950 text-black w-1/2 m-2 p-2" 
                        placeholder="First name" 
                        v-model="firstName"
                    />
                    <input 
                        type="text" 
                        name="input-field" 
                        autocomplete="off" 
                        class="rounded-lg bg-white outline-none border border-slate-950 text-black w-1/2 m-2 p-2" 
                        placeholder="Last name" 
                        v-model="lastName"
                    />
                </div>
                <div class="flex flex-row">
                    <input 
                        type="text" 
                        name="input-field" 
                        autocomplete="off" 
                        class="rounded-lg bg-white outline-none border border-slate-950 text-black w-1/2 m-2 p-2" 
                        placeholder="Email" 
                        v-model="email"
                    />
                    <input type="text" 
                        max="9999999999" 
                        maxlength="10" 
                        name="input-field" 
                        autocomplete="off" 
                        class="rounded-lg bg-white outline-none border border-slate-950 text-black w-1/2 m-2 p-2" 
                        placeholder="Phone number" 
                        v-model="phoneNumber"
                    />
                </div>
                <input 
                    type="text" 
                    name="input-field" 
                    autocomplete="off" 
                    class="rounded-lg bg-white outline-none border border-slate-950 text-black m-2 p-2" 
                    placeholder="User Name" 
                    v-model="username"
                />
                <input 
                    type="password" 
                    name="input-field" 
                    autocomplete="off" 
                    class="rounded-lg bg-white outline-none border border-slate-950 text-black m-2 p-2" 
                    placeholder="Password" 
                    v-model="password"
                />
                <!-- <input type="password" name="input-field" autocomplete="off" class="rounded-lg bg-white outline-none border border-slate-950 text-black m-2 p-2" placeholder="Confirm password"/> -->
                <button type="button" class="bg-yellow-400 text-slate-800 font-bold font-sans rounded-lg flex justify-center m-2 p-2" @click="redirectToLogin">Sign up</button>
            </form>
            <div class="flex flex-row">
                <hr class="customLine w-1/2 my-3 mx-2">
                <p class="text-slate-700 font-sans">or</p>
                <hr class="customLine w-1/2 my-3 mx-2">
            </div>
            <div class="flex flex-row">
                <button 
                    type="button" 
                    class="bg-gray-300 text-slate-800 font-bold font-sans rounded-lg flex justify-center m-2 p-2 w-1/2"
                >
                    Google
                </button>
                <button 
                    type="button" 
                    class="bg-gray-300 text-slate-800 font-bold font-sans rounded-lg flex justify-center m-2 p-2 w-1/2"
                >
                    Facebook
                </button>
            </div>
            <p class="flex text-gray-700 font-bold font-sans justify-center m-2">Already have an account?<button @click="redirectToLogin" class="text-red-500">&nbsp;Login</button></p>
        </div>
    </div>
</template>
<script setup lang="ts">
import { useRouter } from 'vue-router'
import { createUser } from '../../utils/apiService/index';

let username: string;
let email: string;
let firstName: string;
let lastName: string;
let phoneNumber: string;
let password: string;
let confirmPassword: string;

const router = useRouter()

const redirectToLogin = async () => {
    let data = {
        email: email,
        username: username,
        first_name: firstName,
        last_name: lastName,
        password: password,
        phone_number: phoneNumber,
        role: '' 
    }
    console.log({data})
    try{
        const response = await createUser(data);
        const status:number = response.status;
        if (status == 201){
            router.push("/login")
        } 
    } catch (error: any) {
        alert('Not authenicated!!')
    }
    
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
