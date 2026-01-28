<script setup lang="ts">
import {useRoute, useRouter,} from "vue-router";

const route = useRoute(); // 操作当前url
const router = useRouter(); // 操作页面相关
</script>

<template>
个人空间:{{ route.params.user_id }}
</template>

<style scoped>

</style>
