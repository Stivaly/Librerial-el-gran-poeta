<template>
  <body>
    <div class="my-2">
      <div class="container-fluid text-center full-height  ingreso ">
        <div class="row g-0 ">
          <div class="col">
            <div class="row">
              <div class="col">
                <div class="logoUsuario">
                  <img src="../src/assets/usuario.png" class="imgUsuario" alt="..." />

                  <div class="card-body">
                    <h5 class="card-title">Juan Perez</h5>
                    <p class="card-text">Bodeguero</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="row g-0">
              <div class="col">
                <div class="menuVertical">
                  <div class="list-group">
                    <a
                      class="list-group-item list-group-item-action active"
                      aria-current="true"
                    >
                      Almacén
                    </a>


                    <button
                      @click="mostrarFormulario = true"
                      type="button"
                      class="list-group-item list-group-item-action"
                    >
                      Agregar Producto
                    </button>
                    <button
                      type="button"
                      class="list-group-item list-group-item-action"
                    >
                      Eliminar Producto
                    </button>
                    <button
                      type="button"
                      class="list-group-item list-group-item-action"
                      disabled
                    >
                      A disabled button item
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-10 encabezado">
            <nav class="navbar navbar-expand-lg bg-body-tertiary m-0 p-0">
              <div class="container-fluid arriba mt">
                <a class="navbar-brand" href="#">Navbar</a>
                <button
                  class="navbar-toggler"
                  type="button"
                  data-bs-toggle="collapse"
                  data-bs-target="#navbarNavAltMarkup"
                  aria-controls="navbarNavAltMarkup"
                  aria-expanded="false"
                  aria-label="Toggle navigation"
                >
                  <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                  <div class="navbar-nav">
                    <a class="nav-link active" aria-current="page" href="#"
                      >Home</a
                    >
                    <a class="nav-link" href="#">Features</a>
                    <a class="nav-link" href="#">Pricing</a>
                    <a class="nav-link disabled" aria-disabled="true"
                      >Disabled</a
                    >
                  </div>
                </div>
              </div>
            </nav>
            
            <div v-if="mostrarFormulario" class="con-derecho ">
              <div class="contenido">
                <h3>Ingreso de Libros</h3>
                <form class="formulario-productos" @submit.prevent="handleSubmit">
                  <div class="form-gruop text-start">
                    <span for="lnombre" class="text-dark">Ingrese nombre del libro: </span>
                    <input
                      v-model="lnombre"
                      class="form-control"
                      type="text"
                      id="lnombre"
                      placeholder="Nombre Libro"
                      required
                    /><br />
                    <span for="leditorial" class="text-dark"
                      >Ingrese nombre de la editorial:
                    </span>
                    <input
                      v-model="leditorial"
                      class="form-control"
                      type="text"
                      id="leditorial"
                      placeholder="Nombre Editorial"
                      required
                    /><br />
                    <span for="lautor" class="text-dark">Ingrese nombre del autor: </span>
                    <input
                      v-model="lautor"
                      class="form-control"
                      type="text"
                      id="lautor"
                      placeholder="Nombre Autor"
                      required
                    /><br />
                    <span for="lresumen" class="text-dark">Ingrese resumen del libro: </span>
                    <textarea
                      v-model="lresumen"
                      class="form-control"
                      id="lresumen"
                      placeholder="Resumen"
                      rows="3"
                      required
                    ></textarea><br>
                    <button type="submit" class="btn btn-primary me-3" value="Enviar">Enviar</button>
                    <button @click="mostrarFormulario = false" type="button" class="btn btn-primary" value="Cancelar">Cancelar</button>
                  </div>
                </form>

              </div>
            </div>

            <div v-if="libros.length > 0" class="mt-4">
            <h3>Lista de Libros</h3>
            <table class="table">
              <thead>
                <tr>
                  <th>Nombre</th>
                  <th>Editorial</th>
                  <th>Autor</th>
                  <th>Resumen</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="libro in libros" :key="libro.id">
                  <td>{{ libro.nombre }}</td>
                  <td>{{ libro.editorial }}</td>
                  <td>{{ libro.autor }}</td>
                  <td>{{ libro.resumen }}</td>
                </tr>
              </tbody>
            </table>
          </div>

          </div>
        </div>
      </div>

      
    </div>

    
  </body>
  
</template>

<script setup>

import {ref} from 'vue'

let nextId = 1

const mostrarFormulario = ref(false)

const lnombre = ref('')
const leditorial = ref('')
const lautor = ref('')
const lresumen = ref('')
const libros = ref([])

const handleSubmit = () => {
  if (!lnombre.value || !leditorial.value || !lautor.value || !lresumen.value){
    alert ('Ingrese todos los campos')
    return
  }

  
  const nuevoLibro = {
    id: nextId++,
    nombre: lnombre.value,
    editorial: leditorial.value,
    autor: lautor.value,
    resumen: lresumen.value
  }

  libros.value.push(nuevoLibro)


  console.log('Nombre:', lnombre.value)
  console.log('Editorial:', leditorial.value)
  console.log('Autor:', lautor.value)
  console.log('Resumen:', lresumen.value)

  

  mostrarFormulario.value = false

  lnombre.value = ''
  leditorial.value = ''
  lautor.value = ''
  lresumen.value = ''

}




</script>

<style>

html,body{
    padding:0px;
    margin: 0px;
    width: 100%;
    height: 100vh;
    
}

.imgUsuario{
    width: 150px;
    height: 150px;
    border-radius: 75px;
    position: relative;
    margin: 0px 0px;
}

.menuVertical{
    margin-top: 10px;
}

#crearProductos{
    max-width: 100%;
    text-align: center;
    
}

#exampleModal{
    max-width: 100%;
}

.modal{
    background: rgba(177, 161, 161, 0.322); 
      backdrop-filter: blur(10px);
}

.con-derecho{
    background-color: #FFFFFF;
    border-radius: 10px;
    padding: 20px;
    width: 950px;
    margin:auto;
    max-width: 100%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-top: 50px;
}

.encabezado{
    background-color: #F1F2F7;
}

.ingreso{
    background-color: #FFFFFF;
}

.arriba{
    background-color: #FFFFFF;
}

.full-height{
    min-height: 100vh;
}

.table{
  width: 950px;
  margin:auto;
  max-width: 100%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

</style>
