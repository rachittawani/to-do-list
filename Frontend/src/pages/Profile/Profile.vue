<template>
    <div class="customGrid flex flex-col px-2">
        <p class="text-5xl font-bold mb-4">Profile</p>
        <div class="flex flex-row gap-4 bg-gray-100 w-full h-full rounded-lg border border-black p-4 overflow-y-scroll">
            <div class="w-1/2 gap-2">
                <div class="flex flex-row gap-2 items-center mt-4 justify-between">
                    <label for="firstName" class="text-sm font-semibold text-gray-700">First Name</label>
                    <input 
                        type="text" 
                        id="firstName" 
                        autocomplete="off" 
                        class="rounded-lg bg-white outline-none w-2/3 border p-2 text-black border-slate-500"
                        disabled
                        v-model="firstName"
                    />
                </div>
                <div class="flex flex-row gap-2 items-center mt-4 justify-between">
                    <label for="lastName" class="text-sm font-semibold text-gray-700">Last Name</label>
                    <input 
                        type="text" 
                        id="lastName" 
                        autocomplete="off" 
                        class="rounded-lg bg-white outline-none w-2/3 border p-2 text-black border-slate-500"
                        disabled
                        v-model="lastName"
                    />
                </div>
                <div class="flex flex-row gap-2 items-center mt-4 justify-between">
                    <label for="username" class="text-sm font-semibold text-gray-700">User Name</label>
                    <input 
                        type="text" 
                        id="username" 
                        autocomplete="off" 
                        class="rounded-lg bg-white outline-none w-2/3 border p-2 text-black border-slate-500"
                        disabled
                        v-model="username"
                    />
                </div>
                <div class="flex flex-row gap-2 items-center mt-4 justify-between">
                    <label for="email" class="text-sm font-semibold text-gray-700">Email</label>
                    <input 
                        type="email" 
                        id="email" 
                        autocomplete="off" 
                        class="rounded-lg bg-white outline-none w-2/3 border p-2 text-black border-slate-500"
                        disabled
                        v-model="email"
                    />
                </div>
                <div class="flex flex-row gap-2 items-center mt-4 justify-between">
                    <label for="phoneNumber" class="text-sm font-semibold text-gray-700">Phone Number</label>
                    <input 
                        type="tel" 
                        id="phoneNumber" 
                        maxlength="10" 
                        autocomplete="off" 
                        class="rounded-lg bg-white outline-none w-2/3 border p-2 text-black border-slate-500"
                        disabled
                        v-model="phoneNumber"
                    />
                </div>
  
                <div class="flex flex-col mt-10">
                    <p class="flex text-lg font-bold text-black justify-center">Change Password</p>
                    <div class="flex flex-row gap-2 items-center mt-4 justify-between">
                        <label for="password" class="text-sm font-semibold text-gray-700">Old Password</label>
                        <div class="relative w-2/3">
                            <input
                                :type="isPasswordVisible ? 'text' : 'password'"
                                id="password"
                                autocomplete="off"
                                class="rounded-lg bg-white outline-none border w-full p-2 text-black border-slate-500 cursor-pointer"
                                v-model="password"
                            />
                            <button
                                type="button"
                                @click="togglePasswordVisibility"
                                class="absolute right-4 top-2 text-black"
                            >
                                <i :class="isPasswordVisible ? 'fas fa-eye-slash' : 'fas fa-eye'"></i>
                            </button>
                        </div>
                    </div>
                    <div class="flex flex-row gap-2 items-center mt-4 justify-between">
                        <label for="password" class="text-sm font-semibold text-gray-700">New Password</label>
                        <div class="relative w-2/3">
                            <input
                                :type="isNewPasswordVisible ? 'text' : 'password'"
                                id="newpassword"
                                autocomplete="off"
                                class="rounded-lg bg-white outline-none border w-full p-2 text-black border-slate-500 cursor-pointer"
                                v-model="newPassword"
                            />
                            <button
                                type="button"
                                @click="toggleNewPasswordVisibility"
                                class="absolute right-4 top-2 text-black"
                            >
                                <i :class="isNewPasswordVisible ? 'fas fa-eye-slash' : 'fas fa-eye'"></i>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="flex justify-center mt-8">
                    <button
                        type="button"
                        class="bg-slate-800 text-white px-4 py-2 rounded-lg hover:bg-slate-900 transition"
                        @click="updateNewPassword"
                    >
                        Update Password
                    </button>
                </div>
            </div>
            <div class="w-1/2 flex flex-col gap-4 justify-center items-center bg-gray-50 p-4 rounded-lg border border-black">
                <div class="flex flex-col gap-2 items-center">
                    <p class="text-lg font-semibold mb-2 text-black">Profile Picture</p>
                    <div class="w-32 h-32 rounded-full bg-gray-200 border border-black mb-4">
                        <img
                            :src="`https://ui-avatars.com/api/?name=${firstName}+${lastName}&background=1E293B&color=fff&size=128`"
                            alt="Profile Picture"
                            class="w-full h-full rounded-full"
                        />
                    </div>
                    <button
                        type="button"
                        class="bg-slate-800 text-white px-4 py-2 rounded-lg hover:bg-slate-900 transition"
                        >
                        Upload Picture
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { getUserDetail, updatePassword } from '../../utils/apiService/index';
import { onBeforeMount } from 'vue';
import { useRouter } from 'vue-router'

const router = useRouter()

const firstName = ref<string>('');
const lastName = ref<string>('');
const email = ref<string>('');
const username = ref<string>('');
const phoneNumber = ref<string>('');
const password = ref<string>('');
const newPassword = ref<string>('');
const isPasswordVisible = ref(false);
const isNewPasswordVisible = ref(false);


const setUserDetails = async() => {
    try{
        const response = await getUserDetail();
        const status:number = response.status;
        const payload = response.data
        if (status == 200){
            firstName.value = payload.first_name
            lastName.value = payload.last_name
            email.value = payload.email
            username.value = payload.username
            phoneNumber.value = payload.phone_number
        } 
    } catch (error: any) {
        console.log(error)
        router.push("/login")
    } 
}

const updateNewPassword = async() => {
    let data = {
        password: password.value,
        new_password: newPassword.value
    }
    try{
        const response = await updatePassword(data);
        const status:number = response.status;
        const payload = response.data
        console.log({payload})
        if (status == 200){
            console.log("Password updated")
        } 
    } catch (error: any) {
        console.log(error)
        router.push("/login")
    } 
}

onBeforeMount(() => {
    setUserDetails()
})
const togglePasswordVisibility = () => {
    isPasswordVisible.value = !isPasswordVisible.value;
};
const toggleNewPasswordVisibility = () => {
    isNewPasswordVisible.value = !isNewPasswordVisible.value;
};

</script>
  
<style scoped>
    .customGrid {
        height: 100%;
    }
</style>
  