from PIL import Image

print('Quieres un lol?\n')
print('si o no\n')
x = input('')

if x == 'si':
     f = Image.open("lol.jpg")
     f.show()
else:
    print('no hay nada para ti')

