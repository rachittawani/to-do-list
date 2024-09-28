<template>
    <div class="customGrid flex flex-row p-5 gap-4">
        <img class="h-full w-1/2 rounded-2xl object-cover border border-slate-500" src="/src/assets/landingPage.jpg" alt="Landing Page" >
        <div class="flex flex-col px-28 justify-center w-1/2 h-full rounded-2xl border border-slate-500">
            <h1 class="font-bold font-sans text-4xl m-2 p-2 text-center">Sign up</h1>
            <form class="flex flex-col">
                <div class="flex flex-row">
                    <input 
                        type="text" 
                        name="input-field" 
                        autocomplete="off" 
                        :class="['rounded-lg bg-white outline-none border w-1/2 m-2 p-2 text-black', errorVisible && !firstName ? 'border-red-500' : 'border-slate-500']"
                        placeholder="First name" 
                        v-model="firstName"
                    />
                    <input 
                        type="text" 
                        name="input-field" 
                        autocomplete="off" 
                        :class="['rounded-lg bg-white outline-none border w-1/2 m-2 p-2 text-black', errorVisible && !lastName ? 'border-red-500' : 'border-slate-500']"
                        placeholder="Last name" 
                        v-model="lastName"
                    />
                </div>
                <div class="flex flex-row">
                    <input 
                        type="text" 
                        name="input-field" 
                        autocomplete="off" 
                        :class="['rounded-lg bg-white outline-none border w-1/2 m-2 p-2 text-black', errorVisible && !email ? 'border-red-500' : 'border-slate-500']" 
                        placeholder="Email" 
                        v-model="email"
                    />
                    <input type="text" 
                        max="9999999999" 
                        maxlength="10" 
                        name="input-field" 
                        autocomplete="off" 
                        :class="['rounded-lg bg-white outline-none border w-1/2 m-2 p-2 text-black', errorVisible && !phoneNumber ? 'border-red-500' : 'border-slate-500']" 
                        placeholder="Phone number" 
                        v-model="phoneNumber"
                    />
                </div>
                <input 
                    type="text" 
                    name="input-field" 
                    autocomplete="off" 
                    :class="['rounded-lg bg-white outline-none border m-2 p-2 text-black', errorVisible && !username ? 'border-red-500' : 'border-slate-500']"
                    placeholder="User Name" 
                    v-model="username"
                />
                <div class="flex flex-row relative">
                    <input 
                        :type="isPasswordVisible ? 'text' : 'password'" 
                        name="input-field" 
                        autocomplete="off" 
                        :class="['rounded-lg bg-white outline-none border m-2 p-2 w-full text-black', errorVisible && !password ? 'border-red-500' : 'border-slate-500']" 
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
                <!-- <input type="password" name="input-field" autocomplete="off" class="rounded-lg bg-white outline-none border border-slate-500 m-2 p-2 text-black" placeholder="Confirm password"/> -->
                <span v-if="error" class="text-red-500 flex justify-center my-1">{{ error }}</span>
                <div class="flex justify-center">
                    <button 
                        type="button" 
                        class="w-1/2 bg-amber-400 text-slate-900 font-bold font-sans rounded-lg flex justify-center m-2 p-2" 
                        @click="createUsers"
                    >
                        Sign up
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
            <p class="flex font-bold font-sans justify-center m-2">Already have an account?<button @click="redirectToLogin" class="text-red-500">&nbsp;Login</button></p>
        </div>
    </div>
</template>
<script setup lang="ts">
import { useRouter } from 'vue-router'
import { createUser } from '../../utils/apiService/index';
import { ref } from 'vue';

const username = ref<string>('');
const email = ref<string>('');
const firstName = ref<string>('');
const lastName = ref<string>('');
const phoneNumber = ref<string>('');
const password = ref<string>('');
const error = ref<string>('');
const errorVisible = ref<boolean>(false);
const isPasswordVisible = ref<boolean>(false);

const router = useRouter()

const createUsers = async () => {
    if (!firstName.value || !lastName.value || !email.value || !phoneNumber.value || !username.value || !password.value) {
        error.value = 'Please fill in all required fields.';
        errorVisible.value = true;
        return;
    }
    error.value = '';
    errorVisible.value = false;
    let data = {
        email: email.value,
        username: username.value,
        first_name: firstName.value,
        last_name: lastName.value,
        password: password.value,
        phone_number: phoneNumber.value,
        role: '' 
    }
    console.log({data})
    try{
        const response = await createUser(data);
        const status:number = response.status;
        if (status == 201){
            redirectToLogin()
        } 
    } catch (error: any) {
        console.log(error)
    }
}

const redirectToLogin = () => {
    router.push("/login")
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
    border-radius: 12px;
}
</style>
