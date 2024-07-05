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


### Conexión a la Base de Datos

1. **Abrir MySQL Workbench**: Inicia MySQL Workbench desde tu menú de aplicaciones.

2. **Crear una Nueva Conexión**:
    - Haz clic en el icono de `+` junto a "MySQL Connections" para crear una nueva conexión.
    - Completa los detalles de la conexión:
        - `Connection Name`: Un nombre para tu conexión (puede ser cualquier cosa que te ayude a identificarla).
        - `Hostname`: La dirección del servidor donde está alojada tu base de datos.
        - `Port`: El puerto de conexión a MySQL (por defecto es 3306).
        - `Username`: Tu nombre de usuario de MySQL.
        - `Password`: Tu contraseña de MySQL (puedes dejarlo vacío si prefieres ingresar la contraseña cada vez).

3. **Probar la Conexión**:
    - Haz clic en el botón `Test Connection` para asegurarte de que MySQL Workbench puede conectarse a tu base de datos.
    - Si la conexión es exitosa, verás un mensaje de confirmación.
    - Si no es exitosa, revisa las credenciales y asegúrate de que el servidor de la base de datos esté en funcionamiento.

4. **Guardar la Conexión**:
    - Si la prueba de conexión es exitosa, haz clic en `OK` para guardar la conexión.
    - Tu nueva conexión aparecerá ahora en la lista de "MySQL Connections".

### Verificar la Base de Datos

1. **Conectarse a la Base de Datos**:
    - Haz doble clic en la conexión que acabas de crear.
    - Ingresarás a la interfaz principal de MySQL Workbench.

2. **Verificar las Bases de Datos**:
    - En el panel izquierdo, expande el nodo `Schemas` para ver las bases de datos disponibles en tu servidor MySQL.
    - Asegúrate de que todas las bases de datos que esperas ver estén listadas.

3. **Ejecutar una Consulta**:
    - En la barra de herramientas, selecciona `File > New Query Tab` para abrir una nueva pestaña de consulta.
    - Ejecuta una consulta simple para verificar que puedes interactuar con la base de datos. Por ejemplo:

    ```sql
    SHOW DATABASES;
    ```

    - Haz clic en el botón `Execute` (ícono del rayo) para ejecutar la consulta.
    - Verifica que la lista de bases de datos se muestre en el panel de resultados.


## Contribución

Si deseas contribuir a este proyecto, por favor sigue los pasos a continuación:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.
