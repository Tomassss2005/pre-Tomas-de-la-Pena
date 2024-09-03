# pre-Tomas-de-la-Pena

COMO INSTALAR DJANGO, CREAR PROYECTO Y PONER EN MARCHA EL SERVIDOR:

-Primero se crea el entorno virtual(venv), que lo que hace es proporcionar soporte para crear entornos virtuales, y se crea de la siguiente manera:
Primer paso: se abre la terminal del proyecto.
Segundo paso: se ejecuta: python -m venv .venv.
Tercer paso: se activa el entorno virtual(venv) de la siguiente manera: .\.venv\Scripts\activate
-Instalar django: pip install django.
-"manage.py" se usa para crear aplicaciones, trabajar con bases de datos y empezar el desarrollo del servidor web.Sin su archivo no se podría hacer ninguna aplicación/proyecto.Para tener este archivo "manage.py" tenés que hacer el siguiente paso:
django-admin startproyect config.
-Después en la terminal se pone "cd <nombre del proyecto>"(donde se encuentre el archivo "manage.py") para crear una aplicación, que se hace con el comando: 
.manage.py startapp <nombre de la aplicación>
-Abrir la terminal en la carpeta proyect y poner "python manage.py runserver" para arrancar el servidor.


INDICACIONES DEL PROYECTO:

-En la carpeta config, en el archivo urls.py están ubicadas las url, es decir, las direcciones para ubicar cada sitio de la página web. Cada urls está relacionada con una función en especifico 4 (por ejemplo la función usuario_list está relacionada con la url "usuario/list/"),ubicadas en "/servicios/views.py". Cada url indica a donde lleva esa dirección.
-Dentro de la carpeta servicios se ecuentra la carpeta templates/servicios donde se ubican los archivos html.
-En el index.html se encuentra el título principal ("TOMÁS SERVICIOS") del sitio web.
-En los diferentes archivos html se ubica el frontend de la página y algo de lógica.Cada uno de los html se encuentran vinculados al html principal ("principal.html")de la página. Por otro lado está el navbar ("navbar.html") con sus diferentes links hacia los distintos sitios.
-Luego en "models.py" está ubicada la estructura de la base de datos con sus distintas clases y funciones.
-"models.py" está vinculado al archivo "admin.py" dónde usé algunos modelos para que se construya automáticamente un área dentro del sitio.
-Por otro lado, en el archivo "form.py" se encuentra un formulario el cuál están las distintas clases relacionados al los distintos html.
-El botón "Inicio" lo que hace es que cuando hace click vuelve a la pantalla princial. Y los botones "Usuarios", "Pedidos" y "Servicios" cuando haces click manda a la información de:
.En el caso de usuarios muestra a los distintos clientes: su apellido y nombre.
.En Pedidos los pedidos que se hicieron,es decir: el usuario que hizo el pedido, el motivo por el cual hizo el pedido ese usuario, la fecha del pedido y su estado.Y si no hay ningún pedido muestra "NO HAY REGISTROS".
.Y en el caso de Servicios las diferentes cosas que hago y su precio.
-Por último en cada uno de los modelos se vé el botón de "Crear registro", que al tocarlo te manda a un formulario:
.En el  caso de usuarios te manda a un formulario en donde tenés que poner tu nombre y apellido.
.Por el lado de Pedidos te manda a un formulario para selecionar el usuario, el servicio, una descripción del motivo del pedido, la fecha de entrega y su estado.
.Y en el caso de Servicios es un formulario para poner el producto(al que le haya pasado algo), la descripción del pedido, su precio y su estado.
-Y al tocar el botón enviar(en cualquiera de los 3 modelos) lo envía y automaticamente se actualiza la base de datos.
-El archivo db.sqlite3 es la base de datos.
-Al proyecto le puse algo de css para que se vea más aceptable.