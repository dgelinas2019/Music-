#Image Sonification 
#Demonstrartes how to create a soundscape from an image. 
#Pixels of the picture are mapped to the musical notes using these rules:
   #The amount of red in the pixel is mapped to the pitch of the note. Hence, the "redder" the pixel, the higher the pitch. 
   #The amount of blue in the pixel is mapped to the duration of the note. Hence, the "bluer" the pixel, the longer the duration of the note is. 
   #The instrument played for that particular note is random.
from music import *     #accessing music, random, and image libraries
from image import *
from random import * 
image = Image("mm.jpg")      #reading image, loads the image and scans it from left to right. 
#Defining data structure
phr = Phrase(0.0)
#Defining musical parameters 
minPitch = 0
maxPitch = 127 
minDur = 0.2
maxDur = 5.0
scale = MAJOR_SCALE

pixelRows = [15,78,90,125,167,199,215] #specification of which particular rows to sonify 
width = image.getWidth()      #how to get munber of columns in image 
height = image.getHeight()       #how to get number of rows in image 
#An image is defined as width x height 

def sonifyPixel(pixel,col):      #Define a function to sonify a pixel 
   red,blue,green = pixel     
   #RGB values make the pixel unique  
   pitch = mapScale(red,0,255,minPitch,maxPitch,scale)   #The pitch of the note mapped to the amount of red in the pixel 
   duration = mapValue(blue, 0,255, minDur, maxDur)      # The duration of the note mapped to the amount of blue in the pixel 
   n = Note(pitch,duration) #Creating a note. 
   phr.addNote(n)          #Adding note to the phrase 
   return phr              #Instructing the function to return the phrase the note was added into 
inst = randint(0,79) 
for r in pixelRows:              #Nested loops are used here to target the pixel at it's exact 
   for col in range(width):        #location in the row and column 
      instrument = inst          #Setting a random/different instrument for each pixel.
      phr.setInstrument(inst)
      pixel = image.getPixel(col,r)    #Get pixel at current coordinates, column and row (col and r)
      phr = sonifyPixel(pixel,col)     #Recalling defined function 

Play.midi(phr)       #Play!
View.sketch(phr)     #Sketch of the Phrase (phr) 
Write.midi(phr,"Ahhhh.mid")   #Writing the Phrase to an audio and MIDI file 
   

