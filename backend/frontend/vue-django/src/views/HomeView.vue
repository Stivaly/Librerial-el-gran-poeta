<template>
  <nav>
    <div>
      <router-link to="/home">Home</router-link>
    </div>
    <div>
      <router-link to="/about">About</router-link>
    </div>
  </nav>
  <router-view/>
</template>

<script>
// @ is an alias to /src
import Home from '@/components/Home.vue'

export default {
  name: 'HomeView',
  components: {
    Home
  }
}
</script>
