<template>
    <p>{{ selectedList.name }}</p>
</template>
<script setup lang="ts">
import { ref, onBeforeMount, computed } from 'vue';
import { List } from '../../models/list.ts'
import { useRoute } from 'vue-router';

const listObject = ref<Array<List>>([])
// const selectedList = ref<List>()
const route = useRoute();

const selectedList = computed(() =>  listObject.value.find((item) => {
    return item.id == route.params.id
}));
onBeforeMount(() => {
    const data = JSON.parse(localStorage.getItem('listObject'))
    if(data!=undefined) {
        listObject.value = data;
    }
    else {
        listObject.value = []
    }
})
 </script>
 <style>
 .customGrid{
     height: 100%;
 }
 </style>