<template>

    <router-view/>

</template>

<script>
export default {
  name: 'app',
  computed: {
    // Computed property para determinar si estamos en la página de login
    isLoginPage() {
      return this.$route.path === '/api/login'; // Ajusta la ruta según la estructura de tus rutas
    }
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
