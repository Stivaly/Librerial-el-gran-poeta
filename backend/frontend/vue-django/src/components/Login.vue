<template>
  <div class="fondo">
    <div class="container">
      <div class="contenido">
        <h3>Login</h3>
        <form @submit.prevent="enviarFormulario">
          <input ref="usernameInput" type="" placeholder="Username" v-model="form.username">
          <input ref="passwordInput" type="password" :class="{'error': validarPassword}" placeholder="Contraseña" v-model="form.password">
          <p v-if="validarPassword">Debe incluir al menos una mayúscula, una minúscula y un número</p>
          <a href="#" class="forgot-password">Olvidé mi contraseña</a>
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
          // Manejo de la respuesta exitosa
          // Redireccionar, mostrar mensaje, etc.
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
      font-size: 10px;
      font-style: italic;
      color: rgb(31, 70, 243);
      text-align: justify;

  }

  .error {
  border: 1px solid red;
  }
</style>
