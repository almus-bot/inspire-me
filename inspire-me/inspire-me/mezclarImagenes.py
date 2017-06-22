#Carga image de archivo

from PIL import Image

archivo = "/home/hector/ALMUS/inspire-me/inspire-me/sol.jpg"
archivo2 ="/home/hector/ALMUS/inspire-me/inspire-me/luna.jpg"

f = Image.open(archivo)
f2 = Image.open(archivo2)

f.show()
f2.show()
f3 = Image.blend(f,f2,4)
f3.show()

exit
