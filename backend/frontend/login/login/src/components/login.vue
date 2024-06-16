<template>
    <div class="fondo">
      <div class="container">
        <div class="contenido">
          <h3>Login</h3>
          <form @submit.prevent="enviarFormulario">
            <input ref="usernameInput" type="email" :class="{'error': validarEmail}" placeholder="Email" v-model="form.username">
            <input ref="passwordInput" type="password" :class="{'error': validarPassword}" placeholder="Contraseña" v-model="form.password">
            <p v-if="validarPassword">Debe incluir al menos una mayúscula, una minúscula y un número</p>
            <a href="#" class="forgot-password">Olvidé mi contraseña</a>
            <button>Iniciar sesión</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
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
        console.log(this.form);
      }
    },
    computed: {
      validarEmail() {
        const exp = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        const isValid = exp.test(this.form.username);
        return !isValid;
      },
      validarPassword() {
        const exp = /^(?=.*\d)(?=.*[a-záéíóúñ]).*[A-ZÁÉÍÓÚÜÑ]/;
        const isValid = exp.test(this.form.password);
        return !isValid;
      }
    }
  };
  </script>
  
  <style scoped>
    .error {
    border: 1px solid red;
    }
  </style>
  