# **GPT Googler**

[Foto del gato]

*Para clonar este repositorio:* "git clone https://github.com/JuditRoca/GPT_Googler"

¡Bienvenidos! Somos Judith, Giacomo y Braulio, y hemos creado para todo aquel que lo necesite un bot que busca solución a todas tus dudas, usando tanto Google como ChatGPT.

El proyecto comenzó con el equipo entre sentando las bases del código, la estructura de carpetas y recopilando toda la información posible para sacar adelante un proyecto de calidad.

Judith y Giacomo se encargaron de picar código, mientras Braulio estuvo buscando ampliar la información que se disponia del objeto del proyecto.

Al final del primer día terminamos teniendo una interfaz de usuario a la altura y un código notablemente completo de ChatGPT fusionado con Google que ya respondía a lo que se le preguntaba y, posteriormente, se respondía a sí mismo.

A su vez, creamos las carpetas de "static", "templates" y "utils" para dejar el repositorio notablemente funcional y se listaron las instalaciones necesarias en requeriment.txt para que cualquiera disfrute del chatbot.

[requirements.txt aqui]

Este acelerado desarrollo nos permitió poder centrarnos para los siguientes días en Docker, en la base de datos de AWS y en perfeccionar lo que teníamos.

*Se han usado una KEY tanto de Serp Api como de OpenAI para que esto fuera posible. **Tranquilos que las claves están encriptadas***

----------

### [emoji de chili] Flask 

.En esta aplicación, se puede acceder a través de solicitudes HTTP.

Nuestro primer endpoint es @app.route('/', methods=['GET', 'POST']), que asigna la URL "/" a la función home(). Este punto acepta solicitudes GET y POST, que se pueden usar para recuperar la página de inicio e interactuar con DoritaBot, nuestro Bot personalizado.
.Tanto si la petición se trata de una pregunta como si no es así, la respuesta se guardará en index.html para tener un historial y mejorar así la experiencia del usuario.

.El segundo endpoint @app.route('/get_history', methods=['GET']) que es la que crea el historial (def get_all()).

.La función de render_template() se utiliza para renderizar plantillas HTML que se pueden devolver como respuesta a solicitudes HTTP.

*Este chatbot puede utilizarse directamente a través del servidor de desarrollo integrado de Flask. 
Sin embargo, no se recomienda usarlo puesto que no está optimizado para el rendimiento, la seguridad y la confiabilidad.*

[Foto de dev no production]

----------

### [emoji de la mano escribiendo] HTML

Hemos diseñado el DoritaBot a través de Canva para que atraiga más al público. 

Su interfaz muestra una gama de colores cálidos que mejoran la experiencia del usuario a diferencia de su competidor ChatGPT, Bing o Bard.

Las respuestas que genera no solo están en una letra más legible que en la de otros chats, sino que además el historial de respuestas es más claro.

[Foto de la interfaz del chat]

----------

### [emoji de datos] Database

Para crear la base de datos en AWS, se ha de ir a la sección de RDS para crear una DDBB. Allí, el usuario puede ajustar los parámetros, los cuales son:
* Cambiar las opciones del motor a MySQL.
* Cambiar las Plantillas a "free".
* Cambiar en el usuario y creación de la contraseña.
* Opcional: puede cambiarse el nombre en el identificador de instancia de base de datos.
* Opcional: en la opción "Asignar Almacenamiento", puedes cambiar la capacidad.

Tras esperar a que el servicio cree nuestra BBDD, necesitaremos cambiar una cosa para permitir la conectividad con nuestra máquina. 
Hacemos clic en nuestra BBDD y nos dirigimos a "Seguridad>Reglas de entrada" para crear una nueva línea con IPv4 que permita cualquier tráfico con origen (0.0.0.0/0).

[Foto en donde se vea esto, Miguel pasó una]

Una vez que lo tengamos en ejecución, debemos crear una tabla para almacenar nuestras indicaciones. 
Todas las preguntas y respuestas están escritas en archivo .txt. 
Tras ello, estamos listos para usar la BBDD.

----------

### [emoji] OpenAI

La principal herramienta que se ha utilizado viene de la mano de OpenAI, a la que se puede acceder por su API a ChatGPT iniciando sesión y obteniendo una clave privada. *Cada persona puede usar una diferente que ha de asegurarse de copiarla en un lugar seguro.* 

.Dicha API tiene sus límites y pueden mejorarse sus respuesta declarando constantes:
ENGINE = Elegimos text-davinci-003 por valor de eficiencia/costo. U otro.
MAX_TOKENS = 2500, 4000...
CONTEXT_SIZE = Este parámetro recuerda preguntas y respuestas anteriores.
PROMPT_ENGINEERING = Esta es información concreta que le damos a la IA para que nos dé una respuesta más acertada.

----------

### [emoji de una ballena] Docker

.Docker resultó ser ... y nos dio (o no) problemas de compatibilidad. Instalamos las bibliotecas de claves en un entorno alpine (FROM python:3.8-alpine).

.Hay un Dockerfile para producción.

[Foto del dockerfile]

Una vez que se han establecido todos los parámetros y comandos de Dockerfile, se ejecutan los siguientes comandos:

(completar con el codigo con los comandos.. tipo repositorio de miguel)

1. Crear imágenes de Docker:

2. Escaneo de vulnerabilidades:

3. Empuje las imágenes de Docker a Docker Hub:

4. Ejecutar contenedores Docker: