from PIL import Image
print 'Quieres un lol?\n'
print 'si o no\n'
x = raw_input('')
if x == 'si':
 f = Image.open("/home/hector/ALMUS/inspire-me/inspire-me/lol.jpg")
 f.show()
else:
 print 'no hay nada para ti'
exit
