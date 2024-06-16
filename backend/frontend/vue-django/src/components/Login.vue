<template>
  <div class="fondo">
    <div class="container">
      <div class="contenido">
        <h2>Login</h2>
        <form @submit.prevent="enviarFormulario" id="login-form">
          <input ref="usernameInput" id="usernameInput" type="" placeholder="Correo Electrónico" v-model="form.username">
          <input ref="passwordInput" id="passwordInput" type="password" :class="{'error': validarPassword}" placeholder="Contraseña" v-model="form.password">
          <p v-if="validarPassword">Si no recuerdas tu contraseña debes contactar al administrador</p>
          <button type="submit">Iniciar sesión</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "UserLogin",
  data() {
    return {
      form: {
        username: "",
        password: ""
      }
    };
  },
  methods: {
    enviarFormulario() {
      const loginUrl = '/api/login/';
      
      // Asume que Axios ya está configurado para enviar el token CSRF
      axios.post(loginUrl, this.form)
        .then(response => {
          console.log("Login exitoso", response);
          localStorage.setItem('token', response.data.token);
          // Manejo de la respuesta exitosa
          // Redireccionar, mostrar mensaje, etc.
          // Redireccionar a la página de inicio
          this.$router.push('/home'); // Redirige a la ruta principal, ajusta según tu configuración de rutas
        })
        .catch(error => {
          console.error("Error en el login", error);
          // Manejo del error
          // Mostrar mensaje de error al usuario
        });
    }
  },
  computed: {
    validarPassword() {
      const exp = /^(?=.*\d)(?=.*[a-záéíóúñ]).*[A-ZÁÉÍÓÚÜÑ]/;
      const isValid = exp.test(this.form.password);
      return !isValid;
    }
  }
};
</script>

<style scoped>

  @import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Truculenta:opsz,wght@12..72,100..900&display=swap');

  html,body{
      padding:0px;
      margin: 0px;
      width: 100%;
      height: 100vh;
      font-family: "open-sans";
      color: black;
  }

  .fondo{
      background-image: url(../assets/image/fondo.jpg);
      background-size: cover;
      background-position: center center;
      width: 100%;
      height: 100vh;
      display:flex;
      align-content: center;
      align-items: center;
      
      
  }

  .fondo .container{
      width: 100%;
      text-align: center;
  }

  .fondo .container .contenido{
      width: 100%;
      max-width: 400px;
      max-height: 350px;
      background: rgba(255, 255, 255, 0.89);
      padding: 20px;
      border-radius: 10px;
      display: inline-block;
  }

  .fondo .container .contenido h3{
      margin-top: 0px;
  }

  .fondo .container .contenido input{
      height: 55px;
      margin: 0px;
      border:0px;
      outline: none;
      padding: 10px;
      border-radius: 5px;
      width: 100%;
      margin-bottom: 10px;
      font-size: 18px;
  }

  .fondo .container .contenido input.error{
      border-bottom: 3px solid rgb(175, 82, 82);
  } 

  .fondo .container .contenido button{
      
      margin: 0px;
      border: 0px;
      display: block;
      margin: auto;
      padding: 10px 30px;
      background: black;
      color: white;
      border-radius: 5px;
  }

  p{
      font-size: 14px;
      font-style: italic;
      color: rgb(31, 70, 243);
      text-align: justify-center;

  }

  .error {
  border: 1px solid red;
  }
</style>
