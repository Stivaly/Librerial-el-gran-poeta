<template>
  <div class="container-fluid text-center full-height ingreso">
    <div class="row g-0">
      <div class="col">
        <div class="row">
          <div class="col">
            <div class="logoUsuario">
              <img src="../assets/usuario.png" class="imgUsuario mt-5" alt="..." />
              <div class="card-body">
                <h5 class="card-title">Juan Perez</h5>
                <p class="card-text">Jefe de Bodega</p>
              </div>
            </div>
          </div>
        </div>

        <div class="row g-0">
          <div class="col">
            <div class="menuVertical">
              <div class="list-group mx-4">
                <button @click="mostrarFormulario = false; mostrarResumen = true; setActive('almacen')" 
                        :aria-current="activeButton === 'almacen' ? 'true' : 'false'" 
                        type="button" 
                        class="list-group-item list-group-item-action" 
                        :class="{ active: activeButton === 'almacen' }">
                  Almacén
                </button>
                <button @click="mostrarFormulario = true; mostrarResumen = true; setActive('agregar')" 
                        :aria-current="activeButton === 'agregar' ? 'true' : 'false'" 
                        type="button" 
                        class="list-group-item list-group-item-action"
                        :class="{ active: activeButton === 'agregar' }">
                  Agregar Producto
                </button>
                <button @click="mostrarFormulario = false; toggleColumnas(); setActive('eliminar'); "
                        :aria-current="activeButton === 'eliminar' ? 'true' : 'false'" 
                        type="button" 
                        class="list-group-item list-group-item-action"
                        :class="{ active: activeButton === 'eliminar'}">
                  Eliminar Producto
                </button>
                <button @click="mostrarFormulario = false; mostrarResumen = true; setActive('informe')"
                        :aria-current="activeButton === 'informe' ? 'true' : 'false'"  
                        type="button" 
                        class="list-group-item list-group-item-action"
                        :class="{ active: activeButton === 'informe' }">
                  Generar Informe de Movimientos
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-10 encabezado">
        <div v-if="mostrarFormulario && !ocultarFormulario" class="con-derecho">
          <div class="contenido">
            <h3>Ingreso de Libros</h3>
            <div class="d-flex justify-content-start">
              Campos obligatorios: <span class="text-danger">* </span> 
            </div>
            <br>
            <form class="formulario-productos" @submit.prevent="handleSubmit">
              <div class="form-group text-start">
                <label for="lnombre" class="text-dark"><span class="text-danger">* </span> Ingrese nombre del libro: </label>
                <input v-model="lnombre" class="form-control" type="text" id="lnombre" placeholder="Nombre Libro"
                   /><br />
                <label for="lpaginas" class="text-dark"><span class="text-danger">* </span> Ingrese número de páginas del libro: </label>
                <input v-model="lpaginas" class="form-control" type="text" id="lpaginas" placeholder="Numero de páginas del Libro"
                 /><br />
                <label for="leditorial" class="text-dark"><span class="text-danger">* </span>Ingrese nombre de la editorial:</label>
                <select v-model="idEditorialSeleccionada" class="form-control" id="leditorial">
                    <option value="null" disabled selected>Seleccione una editorial</option>
                    <option v-for="editorial in editorialesExistentes" :key="editorial.id" :value="editorial.id">{{ editorial.editorial }}</option>
                </select><br />
                <label for="lautor" class="text-dark"><span class="text-danger">* </span>Ingrese nombre del autor: </label>
                <select v-model="idAutorSeleccionado" class="form-control" id="lautor">
                    <option value="null" disabled selected>Seleccione un autor</option>
                    <option v-for="autor in autoresExistentes" :key="autor.id" :value="autor.id">{{ autor.autor }}</option>
                </select><br />
                <label for="lfecha" class="text-dark"><span class="text-danger">* </span> Ingrese fecha de publicación del libro: </label>
                <input v-model="lfecha" class="form-control" type="text" id="lfecha" placeholder="Fecha de publicación del Libro YYYY-MM-DD"
                 /><br />
                 <label for="lisbn" class="text-dark"><span class="text-danger">* </span> Ingrese código ISBN del libro: </label>
                <input v-model="lisbn" class="form-control" type="text" id="lisbn" placeholder="Fecha de publicación del Libro"
                 /><br />
                <label for="lidioma" class="text-dark"><span class="text-danger">* </span> Ingrese el idioma del libro: </label>
                <select v-model="idIdiomaSeleccionado" class="form-control" id="lidioma">
                    <option value="null" disabled selected>Seleccione un idioma</option>
                    <option v-for="idioma in idiomasExistentes" :key="idioma.id" :value="idioma.id">{{ idioma.idioma }}</option>
                </select><br />
                <label for="lgenero" class="text-dark">
                  <span class="text-danger">* </span>Ingrese Género del libro: </label>
                  <select v-model="idGeneroSeleccionado" class="form-control" id="lgenero">
                    <option value="null" disabled selected>Seleccione un género</option>
                    <option v-for="genero in generosExistentes" :key="genero.id" :value="genero.id">{{ genero.genero }}</option>
                  </select>
                  <br>
                <button type="submit" class="btn btn-primary me-3" value="Enviar">Agregar</button>
                <button @click="mostrarFormulario = false" type="button" class="btn btn-primary"
                  value="Cancelar">Cancelar</button>
              </div>
            </form>
          </div>
        </div>

        <div class="mt-4">
          <div class="mx-3">

            <h3>Lista de Libros</h3>
            <table class="table">
              <thead>
                <tr>
                  <th>Id</th>
                  <th>Nombre</th>
                  <th>Nro. Páginas</th>
                  <th>Editorial</th>
                  <th>Autor</th>
                  <th>Fecha publicación</th>
                  <th>Idioma</th>
                  <th>Género</th>
                  <th v-if="!mostrarResumen">Acciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-if="librosPaginados.length === 0">
                  <td colspan="8" class="text-center">No hay libros ingresados</td>
                </tr>
                <tr v-for="libro in librosPaginados" :key="libro.id_libro">
                  <td>{{ libro.id_libro }}</td>
                  <td>{{ libro.libro_nombre }}</td>
                  <td>{{ libro.libro_numpaginas }}</td>
                  <td>{{ libro.editorial.editorial }}</td>
                  <td>{{ libro.autor.nombre_autor }}</td>
                  <td>{{ libro.libro_fecha_publicacion }}</td>
                  <td>{{ libro.idioma.idioma }}</td>
                  <td>{{ libro.genero.genero }}</td>
                  <td v-if="!mostrarResumen">
                    <button @click="eliminarProducto(libro.id)" type="button" class="btn btn-danger">Eliminar</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Controles de paginación -->
        <nav aria-label="Page navigation example">
          <ul class="pagination justify-content-center">
            <li class="page-item" :class="{ 'disabled': paginaActual === 1 }">
              <a class="page-link" href="#" @click.prevent="cambiarPagina(paginaActual - 1)">Anterior</a>
            </li>
            <li class="page-item" v-for="pagina in totalPaginas" :key="pagina"
              :class="{ 'active': pagina === paginaActual }">
              <a class="page-link" href="#" @click.prevent="cambiarPagina(pagina)">{{ pagina }}</a>
            </li>
            <li class="page-item" :class="{ 'disabled': paginaActual === totalPaginas }">
              <a class="page-link" href="#" @click.prevent="cambiarPagina(paginaActual + 1)">Siguiente</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue'
  import axios from 'axios';

  let lastId = 0; 

  const mostrarFormulario = ref(false)
  const ocultarFormulario = mostrarFormulario.value = false
  const lnombre = ref('')
  const lpaginas = 0
  const leditorial = ref('')
  const lautor = ref('')
  const lfecha = ref('')
  const lisbn = ref('')
  const lidioma = ref('')
  const lgenero = ref('')
  const libros = ref([])
  const librosPorPagina = 8
  const paginaActual = ref(1)
  const mostrarResumen = ref(true)

  const idGeneroSeleccionado = null, idIdiomaSeleccionado = null, idAutorSeleccionado = null, idEditorialSeleccionada = null;

  const generosExistentes = [
  { id: 1, genero: 'Novela' },
  { id: 2, genero: 'Poesía' },
  { id: 3, genero: 'Drama' },
  { id: 4, genero: 'Ciencia Ficción' },
  { id: 5, genero: 'Fantasía' },
  { id: 6, genero: 'Terror' },
  { id: 7, genero: 'Aventura' },
  { id: 8, genero: 'Histórica' },
  { id: 9, genero: 'Romance' },
  { id: 10, genero: 'Ensayo' }
  ];

  const idiomasExistentes = [
  { id: 1, idioma: 'Español' },
  { id: 2, idioma: 'Inglés' },
  { id: 3, idioma: 'Francés' }
  ];

  const autoresExistentes = [
    {id: 4, autor: 'Douglas Adams'},
    {id: 7, autor: 'Bill Bryson'},
    {id: 16, autor: 'Edith Wharton'}
  ]

  const editorialesExistentes = [
    {id: 14, editorial: '1500 Books LLC'},
    {id: 28, editorial: '826 Books'},
    {id: 37, editorial: 'A&C  Black'}
  ]

  const obtenerLibros = async () => {
    const baseURL = '/api/home/'
    try {
      const response = await axios.get(baseURL);
      return response.data; 
    } catch (error) {
      console.log('Error al obtener libros:', error);
      throw error; 
    }
  };

  const cargarLibros = async () => {
    try {
      const librosObtenidos = await obtenerLibros();
      libros.value = librosObtenidos;
      if (librosObtenidos.length > 0) {
      lastId = librosObtenidos[librosObtenidos.length - 1].id; 
      }
    } catch (error) {
      console.log('Error al cargar libros:', error);
    }
  };

  onMounted(() => {
    cargarLibros();
  }) 
    

  const librosPaginados = computed(() => {
    const inicio = (paginaActual.value - 1) * librosPorPagina
    const fin = paginaActual.value * librosPorPagina
    return libros.value.slice(inicio, fin)
  })

  const truncate = (text, length) => {
    if (text) {
      return text.length > length ? text.substring(0, length) + '...' : text;
    } else {
      return '';
    }
  };

  const totalPaginas = computed(() => Math.ceil(libros.value.length / librosPorPagina))

  const handleSubmit = async () => {
    
    if (!lnombre.value || !leditorial.value || !lpaginas.value || !lfecha.value || !lisbn.value || !lidioma.value || !lautor.value || !lgenero.value) {
      alert('Ingrese todos los campos')
      return
    }

    const nuevoLibro = {
      id: lastId + 1,
      libro_nombre: lnombre.value,
      libro_numpaginas: lpaginas.value,
      editorial: {
        id_editorial: leditorial.value,  
        editorial: leditorial.options[leditorial.selectedIndex].text  
      },
      autor: {
        id_autor: lautor.value,  
        nombre_autor: lautor.options[lautor.selectedIndex].text,  
        pais: {
          id_pais: lautor.options[lautor.selectedIndex].dataset.paisId,  
          pais: lautor.options[lautor.selectedIndex].dataset.paisNombre,  
          latitud: lautor.options[lautor.selectedIndex].dataset.paisLatitud,  
          longitud: lautor.options[lautor.selectedIndex].dataset.paisLongitud  
        },
        autor_genero: lautor.options[lautor.selectedIndex].dataset.genero,  
        autor_rating_promedio: lautor.options[lautor.selectedIndex].dataset.ratingPromedio,  
        cantidad_rating_autor: lautor.options[lautor.selectedIndex].dataset.cantidadRating,  
        cantidad_comentarios: lautor.options[lautor.selectedIndex].dataset.cantidadComentarios  
      },
      idioma: {
        id_idioma: lidioma.value,  
        idioma: lidioma.options[lidioma.selectedIndex].text  
      },
      libro_rating_promedio: 0, 
      libro_fecha_publicacion: lfecha.value,
      libro_review_counts: 0,  
      libro_ISBN: lisbn.value, 
      id_autor: lautor.value, 
      id_editorial: leditorial.value,  
      id_idioma: lidioma.value,  
      id_genero: lgenero.value,
    };

    try {
      const baseURL = `/api/agregar/${id}`
      const response = await axios.post(baseURL, nuevoLibro);
      if (response.status === 201) {
        alert('Libro guardado exitosamente');
        libros.value.push(nuevoLibro)
    
        mostrarFormulario.value = false
    
        lnombre.value = ''
        lpaginas.value = ''
        leditorial.value = ''
        lautor.value = ''
        lfecha.value = ''
        lidioma.value = ''
        lresumen.value = ''
      } 
      // Ajustar la página actual para mostrar el nuevo libro si está en una nueva página
      if (libros.value.length > paginaActual.value * librosPorPagina) {
        paginaActual.value = totalPaginas.value
      }
    } catch (error) {
      console.error('Error al guardar el libro:', error);
      alert('Ocurrió un error al guardar el libro. Por favor, inténtelo de nuevo.');
    }
  }

  const toggleColumnas = () => {
    mostrarResumen.value = !mostrarResumen.value;
  }

  const eliminarProducto = async (id) => {
    const baseURL = `/api/eliminar/${id}`
    try {
      const response = await axios.delete(baseURL); 
      if (response.status === 200) {
        const index = libros.value.findIndex(libro => libro.id === id);
        if (index !== -1) {
          libros.value.splice(index, 1);
        } else {
          console.error(`No se encontró un libro con ID ${id} en la página actual`);
        }
        alert('Producto eliminado exitosamente');
      } else {
        alert(`Error al eliminar libro con ID ${id}. Estado de respuesta: ${response.status}`);
      }
    } catch (error) {
        alert(`Error al eliminar libro con ID ${id}:`, error);
        // Puedes manejar el error según tu lógica de la aplicación
        throw error;
    }
  };

  const cambiarPagina = (pagina) => {
    if (pagina >= 1 && pagina <= totalPaginas.value) {
      paginaActual.value = pagina
    }
  }

  const activeButton = ref('almacen')
  const setActive = (button) => {
    activeButton.value = button;
    mostrarFormulario.value = button === 'agregar';
  }
</script>

<style>
  html,
  body {
    padding: 0px;
    margin: 0px;
    width: 100%;
    height: 100vh;
  }

  td {
    text-align: center; 
    vertical-align: middle;
    white-space: pre-wrap; 
    max-width: 60px; 
    overflow-wrap: break-word;
  }

  .imgUsuario {
    width: 150px;
    height: 150px;
    border-radius: 75px;
    position: relative;
    margin: 0px 0px;
  }

  .menuVertical {
    margin-top: 10px;
  }

  #crearProductos {
    max-width: 100%;
    text-align: center;
  }

  #exampleModal {
    max-width: 100%;
  }

  .modal {
    background: rgba(177, 161, 161, 0.322);
    backdrop-filter: blur(10px);
  }

  .con-derecho {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px;
    width: 950px;
    margin: auto;
    max-width: 100%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-top: 50px;
  }

  .encabezado {
    background-color: #f1f2f7;
  }

  .ingreso {
    background-color: #ffffff;
  }

  .arriba {
    background-color: #ffffff;
  }

  .full-height {
    min-height: 100vh;
  }

  .table {
    width: 1450px;
    margin: auto;
    max-width: 100%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  .pagination {
    margin-top: 20px;
  }

  .page-item.disabled .page-link {
    pointer-events: none;
    cursor: not-allowed;
  }
</style>