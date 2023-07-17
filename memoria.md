# GPT Googler DoritaBot

¡Bienvenid@!
Somos Judith, Giacomo y Braulio, y hemos creado para todo aquel que lo necesite un bot que busca solución a todas tus dudas, usando tanto Google como ChatGPT.

<img width="959" alt="header" src="https://github.com/JuditRoca/GPT_Googler/assets/130987096/594165cc-414e-4a3b-9508-103536972ea3">

El proyecto comenzó con el equipo entre sentando las bases del código, la estructura de carpetas y recopilando toda la información posible para sacar adelante un proyecto de calidad.

Judith y Giacomo se encargaron de picar código, mientras Braulio estuvo buscando ampliar la información que se disponia del objeto del proyecto.

Al final del primer día terminamos teniendo una interfaz de usuario a la altura y un código notablemente completo de ChatGPT fusionado con Google que ya respondía a lo que se le preguntaba y, posteriormente, se respondía a sí mismo.

A su vez, creamos las carpetas de "static", "templates" y "utils" para dejar el repositorio notablemente funcional y se listaron las instalaciones necesarias en requeriments.txt para que cualquiera disfrute del chatbot.

Este acelerado desarrollo nos permitió poder centrarnos para los siguientes días en Docker, en la base de datos de AWS y en perfeccionar lo que teníamos.

*Se han usado una KEY tanto de Serp Api como de OpenAI para que esto fuera posible. **Las claves están encriptadas***

<p align="center">
<img src="https://github.com/JuditRoca/GPT_Googler/assets/130987096/5d521ab9-ac6b-43d2-9de5-fa9c4f0240aa height=300 width=300">
</p>

----------

### 🌶️ Flask 

A este proyecto se puede acceder a través de solicitudes HTTP.

Nuestro primer endpoint es @app.route('/', methods=['GET', 'POST']), que asigna la URL "/" a la función home(). Este punto acepta solicitudes GET y POST, que se pueden usar para recuperar la página de inicio e interactuar con DoritaBot, nuestro Bot personalizado favorito. Tanto si la petición se trata de una pregunta como si no es así, la respuesta se guardará en index.html para tener un historial y mejorar así la experiencia del usuario.

Y es nuestro segundo endpoint es @app.route('/get_history', methods=['GET']), el que crea el historial (funcion de def get_all() en el código) para que se vean todas las preguntas y respuestas del primer endpoint.

*Este chatbot puede utilizarse directamente a través del servidor de desarrollo integrado de Flask. Sin embargo, no se recomienda usarlo puesto que no está optimizado para el rendimiento, la seguridad y la confiabilidad.*

![dev no production](https://github.com/JuditRoca/GPT_Googler/assets/130987096/72d1c0f1-be99-47dd-a78f-eb8e7fa81622)

----------

### 💻 HTML

Hemos diseñado el DoritaBot a través de Canva para que atraiga más al público. 

Su interfaz muestra una gama de colores cálidos que mejoran la experiencia del usuario a diferencia de su competidor ChatGPT, Bing o Bard.

Las respuestas que genera no solo están en una letra más legible que en la de otros chats, sino que además el historial de respuestas es más claro.

 <p align="center">
<img src="https://github.com/JuditRoca/GPT_Googler/assets/130987096/7654b50a-dc31-47b7-9b7f-0c2c3fae925a">
 </p>
----------

### 📊 Database

Para crear la base de datos en AWS, se ha de ir a la sección de RDS para crear una DDBB. Allí, pueden ajustarse los parámetros, los cuales permiten:
* Cambiar las opciones del motor a MySQL.
* Cambiar las Plantillas a "free".
* Cambiar en el usuario y creación de la contraseña.
* Opcional: puede cambiarse el nombre en el identificador de instancia de base de datos.
* Opcional: en la opción "Asignar Almacenamiento", puedes cambiar la capacidad.

Tras esperar a que el servicio cree nuestra BBDD, se necesita cambiar una cosa para permitir la conectividad con la máquina. 
Hacemos clic en nuestra BBDD y nos dirigimos a "Seguridad>Reglas de entrada" para crear una nueva línea con IPv4 que permita cualquier tráfico con origen (0.0.0.0/0).

Una vez que lo tengamos en ejecución, debemos crear una tabla para almacenar nuestras indicaciones. 
Todas las preguntas y respuestas están escritas en archivo .txt.

----------

### 🤖 OpenAI

La principal herramienta que se ha utilizado para este proyecto viene de la mano de OpenAI, a la que se puede acceder por su API a ChatGPT iniciando sesión y estableciendo una clave privada (como decia previamente, a su vez hay que utilizar una clave privada de SERP API) para hacer funcional esta herramienta. 

*Cada persona puede usar una clave de OPEN AI diferente que ha de estar encriptada para que otras personas no hagan un mal uso de esta*

----------

### 🐳 Docker

Pensábamos que ibamos a tener grandes problemas con el Docker, pero resultó ser sencillo. Judith ya había usado el Dockerfile en un trabajo anterior y sabía usarlo. No nos dio problemas de compatibilidad, instalamos las bibliotecas de claves en un entorno alpine (FROM python:3.8-alpine) y poco más.

 <p align="center">
<img src="https://github.com/JuditRoca/GPT_Googler/assets/130987096/ab045ba9-d89e-4478-8aa1-4c0d385bfec5" height=600 width=830>
 </p>

Una vez establecimos todos los pasos de la imagen de arriba ya está todo en orden y listo para chatbotear.
