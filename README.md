<p align="center">
  <img src="https://github.com/JuditRoca/GPT_Googler/blob/main/src/static/header.png" alt="Portada"/>
</p>
<p align="center"> 
  <a href="#Intro">Intro</a> •
  <a href="#Instrucciones">Instrucciones</a> •
  <a href="#Equipo">Equipo</a> •
</p>
<h2 id="Intro">:book:Intro</h2>

Bienvenido al repositorio de GitHub del proyecto "GPT_Googler". Este proyecto tiene como objetivo proporcionar una solución integral para interactuar con diversas APIs, aprovechando el poder de ChatGPT y Google, y almacenando los datos obtenidos en AWS.

Los principales objetivos de este proyecto son:

-   **API Integration**: El repositorio proporciona un conjunto de módulos y utilidades para conectarse sin problemas con diferentes APIs. Te permite interactuar con servicios externos, recuperar datos y realizar operaciones utilizando interfaces bien definidas.

-   **ChatGPT & Google Integration**: El proyecto aprovecha el modelo ChatGPT de OpenAI para permitir conversaciones en lenguaje natural. Puedes utilizar la funcionalidad de chat para buscar respuestas, generar respuestas y obtener información del modelo de conversación impulsado por inteligencia artificial. Esto te permite mejorar las capacidades de tu aplicación y recuperar información relevante de manera eficiente.

-   **AWS Data Storage**: El proyecto incluye funcionalidades para almacenar y gestionar los datos obtenidos en AWS. Esto garantiza opciones seguras y escalables de almacenamiento de datos, lo que te permite manejar grandes cantidades de información de manera efectiva.

El repositorio proporciona una documentación completa, ejemplos y fragmentos de código para guiarte en la configuración, la instalación y el uso del proyecto. Su objetivo es simplificar el proceso de trabajo con APIs, aprovechar los servicios de ChatGPT y Google, y almacenar los datos de manera segura en AWS.

Te animamos a explorar el repositorio, contribuir a su desarrollo y aprovechar sus capacidades para mejorar tus proyectos. Si tienes alguna pregunta o comentario, no dudes en contactarnos. Happy coding!

<h3 id="Instrucciones">:bookmark_tabs:Instrucciones</h3>

Para clonar y ejecutar el Docker container, debes seguir los siguientes pasos.
  1. Clonar repositorio.

  <p align="center">
  <img src="https://github.com/JuditRoca/GPT_Googler/blob/main/src/static/gitclone.png" alt="clone"/>
</p>
  Debes ejecutar el codigo en tu terminal.

  2. Crea un archivo .env en la carpeta raíz del repositorio con las siguientes variables y reemplaza <API_KEY> con tu propia clave de API:

      SERPAPI_API_KEY= tu serpapi api key
      user_bd= nombre de la base de datos
      pass_bd= la contraseña de tu base de datos.
      host= el host
      OPENAI_API_KEY= tu openai key
  
  3. Asegúrate de agregar .env al archivo .gitignore para evitar que se suba al repositorio. Esto mantendrá tus claves de API seguras y privadas.
  
  4. Navegar a la carpeta raiz.

<p align="center">
  <img src="https://github.com/JuditRoca/GPT_Googler/blob/main/src/static/cd.png" alt="cd"/>
</p>

  5. Ahora podemos contruir la imagen del contenedor. IMPORTANTE EL PUNTO !

<p align="center">
<img src="https://github.com/JuditRoca/GPT_Googler/blob/main/src/static/dockerbuilt.jpg" alt="imagen"/>
</p>

  6. Ahora que hemos contruido la imagen de nuestro contenedor, podemos ejecutarlo con el siguiente comando:

<p align="center">
  <img src="https://github.com/JuditRoca/GPT_Googler/blob/main/src/static/docker_run.png" alt="run"/>
</p>

 
<h3 id="Equipo">:family:Equipo</h3>
Este proyecto ha sido posible gracias a las valiosas contribuciones de cada uno de los siguientes miembros, cuyos esfuerzos combinados han hecho posible su desarrollo:

-   Giacomo Salerno [:panda_face:](https://github.com/GiamoSalerno)
-   Judit Roca [:blossom:](https://github.com/JuditRoca)
-   Braulio Gilabert [:european_castle:](https://github.com/braugilabert) 
