# Manual de instalación

## Requisitos

Antes de empezar, asegúrate de tener instalados los siguientes programas:

- [Git](https://git-scm.com/)
- [Node.js](https://nodejs.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [Python](https://www.python.org/)
- [MySQL Workbench](https://www.mysql.com/products/workbench/)
  
## Instalación

Sigue los siguientes pasos de manera ordenada para clonar e instalar el proyecto en tu máquina local:

### Clonar el Repositorio

1. Abre tu terminal o línea de comandos.
2. Navega al directorio donde deseas clonar el repositorio.
3. Ejecuta el siguiente comando:

    ```bash
    git clone https://github.com/usuario/Librerial-el-gran-poeta.git
    ```

4. Entra en el directorio del proyecto:

    ```bash
    cd Librerial-el-gran-poeta
    cd backend
    ```

### Instalación de Dependencias

#### Backend Python

1. Activa el entorno virtual:

    ```bash
    .\venv\Scripts\activate
    ```
2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```
    
### Configuración del Entorno

1. Crea un archivo `.env` en la raíz del proyecto y agrega las variables de entorno necesarias que se encuentran dentro del informe de este proyecto.
   (Las Credenciales actuales se encuentran alojadas en el informe enviado al tutor para su evaluación.)
2. Inicia el servidor de backend:
   ```bash
    python manage.py runserver
    ```
   
### Ejecución del Proyecto

#### Frontend Node.js
1. Asegúrate de continuar dentro de entorno virtual
2. Navega al directorio del frontend:

    ```bash
    cd frontend
    cd vue
    ```

3. Ejecuta el siguiente comando para iniciar el servidor frontend:

    ```bash
    npm run serve
    ```

4. Abre tu navegador y navega a `http://localhost:8080` para ver la aplicación en funcionamiento.

#### Para Proyectos Python

2. Abre tu navegador y navega a `http://127.0.0.1:8000` para visualizar el ambiente de aplicación de Django REST framework. 

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los pasos a continuación:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.
