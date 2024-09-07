<template>
    <div class="customGrid flex flex-row p-5 gap-4">
        <img class="h-full w-1/2 rounded-2xl object-cover border border-slate-500" src="/src/assets/landingPage.jpg" alt="Landing Page" >
        <div class="flex flex-col px-28 justify-center w-1/2 h-full rounded-2xl border border-slate-500">
            <h1 class="font-bold font-sans text-4xl m-2 p-2 text-center">Login</h1>
            <form class="flex flex-col">
                <input 
                    type="text"
                    name="username"
                    autocomplete="off"
                    :class="['rounded-lg bg-white outline-none border m-2 p-2 text-black', errorVisible && !username ? 'border-red-500' : 'border-slate-500']"
                    placeholder="Username"
                    v-model="username"
                />
                <div class="flex flex-row relative">
                    <input 
                        :type="isPasswordVisible ? 'text' : 'password'" 
                        name="password" 
                        autocomplete="off" 
                        :class="['w-full rounded-lg bg-white outline-none border m-2 p-2 text-black', errorVisible && !password ? 'border-red-500' : 'border-slate-500']"
                        placeholder="Password"
                        v-model="password"
                    />
                    <button 
                        type="button" 
                        @click="togglePasswordVisibility" 
                        class="p-1 text-black absolute right-4 top-3"
                        >
                        <i :class="isPasswordVisible ? 'fas fa-eye-slash' : 'fas fa-eye'"></i>
                    </button>
                </div>
                <div class="flex justify-center">
                    <button 
                        type="button" 
                        class="w-1/2 bg-amber-400 text-slate-900 font-bold font-sans rounded-lg flex justify-center m-2 p-2" 
                        @click="redirectToHome"
                    >
                        Login
                    </button>
                </div>
            </form>
            <div class="flex flex-row">
                <hr class="customLine w-1/2 my-3 mx-2">
                <p class="font-sans">or</p>
                <hr class="customLine w-1/2 my-3 mx-2">
            </div>
            <div class="flex flex-row">
                <button 
                    type="button" 
                    class="bg-neutral-300 text-slate-900 font-bold font-sans rounded-lg flex justify-center m-2 p-2 w-1/2"
                >
                    Google
                </button>
                <button 
                    type="button" 
                    class="bg-neutral-300 text-slate-900 font-bold font-sans rounded-lg flex justify-center m-2 p-2 w-1/2"
                >
                    Facebook
                </button>
            </div>
            <p class="flex font-bold font-sans justify-center m-2">Don't have an account?
                <button @click="redirectToSignUp" class="text-red-500">&nbsp;Sign up</button>
            </p>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { useRouter } from 'vue-router'
import { ref } from 'vue';
import { login } from '../../utils/apiService/index';
import Cookies from 'js-cookie';

const router = useRouter()

const username = ref<string>('');
const password = ref<string>('');
const error = ref<string>('');
const errorVisible = ref<boolean>(false);
const isPasswordVisible = ref<boolean>(false);

const redirectToSignUp = () => {
    router.push("/signup")
}
const redirectToHome = async () => {
    if (!username.value || !password.value) {
        error.value = 'Please fill in all required fields.';
        errorVisible.value = true;
        return;
    }
    error.value = '';
    errorVisible.value = false;
    let data = {
        username: username.value,
        password: password.value
    }
    try{
        const response = await login(data);
        const status:number = response.status;
        const payload = response.data
        Cookies.set('token', payload.access_token)
        Cookies.set('tokenType', payload.token_type)
        if (status == 200){
            router.push("/home")
        } 
    } catch (error: any) {
        console.log(error)
    }
}
const togglePasswordVisibility = () => {
    isPasswordVisible.value = !isPasswordVisible.value;
}

</script>
<style>
.customGrid{
    height: 100%;
}
.customLine{
    height: 1px;
    opacity: 1;
    /* background-color: rgb(221, 221, 221); */
    border-radius: 12px;
}
</style>
