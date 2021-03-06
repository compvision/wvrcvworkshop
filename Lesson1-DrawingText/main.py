#including neccesary libraries
from SimpleCV.base import *
from SimpleCV.Color import *
from SimpleCV.ImageClass import *
from SimpleCV.Font import *
from SimpleCV.ColorModel import *
from SimpleCV.DrawingLayer import *

#First, we need to get the image
img = Image("image.png")

#Simple writing text
  #optional: change font by img.dl().selectFont('font_name')
  #to see all supported fonts, run img.dl().listFonts()
img.drawText("Hello, World");

#show the image
img.show()
#wait for input (keeps the image shown, hit enter in the terminal to continue the code)
raw_input()

#Drawing Shapes

#Rectange
#First, We have to create a drawing layer to draw on
imgLayer = DrawingLayer((img.width,img.height))
sizeOfRect = (200,200)
point = (img.width/2 , img.height/2) #centering
rect = imgLayer.rectangle(point, sizeOfRect)
img.addDrawingLayer(imgLayer)
img.applyLayers()
img.show()
raw_input()

''' Shapes you can draw:
imgLayer.circle(point, radius)
imgLayer.centeredRectangle(centerPoint, (width, height))
imgLayer.rectangle(topLeftCornerPoint, (width, height))

polygons are a bit more complicated:
first, we need to define the points that the polygon will have
points = [(x, y), (x,y), (x,y), (x,y)]
imgLayer.polygon(points, filled=True) #again, you can add color if you want

optionally, add an additional parameter to choose color
example:
imgLayer.circle(point, radius, color=Color.RED)
'''
