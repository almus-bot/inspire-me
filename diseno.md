Un paquete para generar imágenes motivadoras: inspire-me
========================================================

Se desea desarrollar un paquete en Python que facilite la generación de
imágenes motivadoras como las que encontramos con frecuencia en la redes
sociales. Estas son imágenes que constan usualmente de una imagen de fondo y un
texto superpuesto.

La imagen y el texto suelen relacionarse a un concepto que el autor desea
comunicar. Por un lado, la imagen de fondo suele ser un color plano o una
degradación, también son frecuentes imágenes prediseñadas o fotografías. Por el
otro, el texto suelen ser frases motivadoras que pueden ser ocurrencias del
propio autor o citas de alguna personalidad.

Se requiere entonces:

    * Información de la imagen: color, degradación, o localización de la
      imagen. La imagen podría estar localizada en un dispositivo de
      almacenamiento local o remoto.
      
    * Para especificar las imágenes remotas se podría indicar mediante un URL o
      mediante palabras clave que realicen búsquedas en servicios de imágenes
      en línea.

    * Información del texto: se requiere el propio texto, la fuente o fuentes
      tipográficas a utilizar, propiedades del texto como colores o tamaños, y
      la ubicación del texto en la imagen.

    * Para facilitar la introducción de especificaciones se podrían utilizar
      plantillas o temas. Igualmente contar con características de referencia
      para cada red social. Por ejemplo, las imágenes en formato PNG con
      transparencia suelen funcionar mal.

    * Sería útil llevar un registro de algunas de las imágenes generadas. En
      particular, las que hayan sido sido elegidas para ser publicadas. Los
      hashtags utilizados en las publicaciones.

    * El paquete debe proveer comandos para el terminal, y la posibilidad de
      llamar a sus funciones dentro de un programa en Python.

De esta manera, se ofrecerá al usuario funcionalidades para:

    * Crear la imagen de fondo indicando las opciones:
        * Un color por nombre o valor hexadecimal para el fondo plano.
        * Para la degradación, colores de inicio y finalización (por nombre o
          valor hexadecimal), y dirección de la degradación.
        * Para la imágenes o fotografías locales, la ruta al archivo. Para las
          remotas el URL.
        * En caso de búsqueda de imágenes, identificador del servicio de
          búsqueda y las palabras clave.
        * Especificar transformaciones o filtros básicos a ser aplicados a la
          imágen.
        * Especificar tamaño de la imagen, ya sea por pixeles o por la red
          social donde se desea publicar. Indicar si es escalado, recorte o
          mosaico.

    * Para el texto, ofrecer las opciones:
        * Introducir directamente la cadena texto.
        * Tomar el texto desde un archivo, para lo cuál se requiere la ruta del
          archivo. Debe ser un archivo de texto con una longitud máxima
          permisible total y por palabra.
        * En caso de búsqueda de citas, especificar una palabra clave e
          identificador del servicio de búsqueda.
        * Transformaciones o filtros básicos a ser aplicados a las fuentes.

        
          
