<template>
    <UserLogin />
  </template>
  
  <script>
  // @ is an alias to /src
  import UserLogin from '@/components/Login.vue'
  
  export default {
    name: 'Login',
    components: {
        UserLogin
    }
  }
  </script>
  