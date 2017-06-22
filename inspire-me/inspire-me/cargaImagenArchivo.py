#Carga image de archivo

from PIL import Image

archivo = "/home/hector/ALMUS/inspire-me/inspire-me/lol.jpg"


print('Quieres la imagen desde el archivo?\n')
print('si o no\n')
x = input('')
if x == 'si':
 f = Image.open(archivo)
 f.show()
else:
 print('no deseas cargar la imagen')
exit
