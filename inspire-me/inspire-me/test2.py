#!/usr/local/bin/python
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter

dimX = 200
dimY = 50
color = "#ddd"
fontPath = "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf"
sans16  =  ImageFont.truetype ( fontPath, 16 )


im  =  Image.new ( "RGB", (dimX,dimY), color )
draw  =  ImageDraw.Draw ( im )
draw.text ( (10,10), "Run awayyyy!", font=sans16, fill="red" )
im.save ( "runaway2.jpg" )
