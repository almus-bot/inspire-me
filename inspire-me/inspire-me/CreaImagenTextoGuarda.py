#Crea una imagen con los parametros:
#                    -resolucionImagen, 
#                    -colorFondo, 
#                    -colorTexto, 
#                    -texto, 
#                    -posicionTexto,
#                    -dimensionTexto, 
#                    -fuente, 
#                    -modoImagen
#La muestra y la guarda en el directorio local 

#!/usr/local/bin/python

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter

resolucionImagen = (640,480)
colorFondo = "#ddd"
colorTexto = "red"
texto = "Texto Inspirador en Imagen"
posicionTexto = (100,10)
dimensionTexto = 16
fuentePath = "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf"
fuente  =  ImageFont.truetype ( fuentePath, dimensionTexto )
modoImagen = "RGB"


im  =  Image.new ( modoImagen, resolucionImagen, colorFondo )
draw  =  ImageDraw.Draw ( im )
draw.text ( posicionTexto, texto, font=fuente, fill=colorTexto )
im.show()
im.save ( "imagenFlatColorTexto.jpg" )
