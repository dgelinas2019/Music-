#What does my name sound like?
#mapping the characteristics in my name to components of music (pitch and duration) to hear what my name sounds like 
#comming up with a system that maps each character to a pitch 
#my name consists of text data 
#ascii table has  mapping, 33-124 for each letter,
#each letter, symbol has a corresponding number, computers are binary
#each pitch ranges from 0-127
#convert letters into integers, then we will have pitches
#can use a for loop to run though letters of my name 
from music import *
from random import *
name = "Danielle Gelinas"     #saving my name to a variable 
vowels = "AEIOUYaeiouy"       #saving vowels and a space to variables 
space = " " 
phr = Phrase(0.0)  #map char to pitch, duration, and velocity 
for char in name:        
   ascii_val= ord(char)    #convert the letters in my name to numerical values
   if char in vowels:        # if char is a vowel, the duration of the note will be longer and louder
      pitch = ascii_val
      duration = HN
      velly = 127       #velly is the velocity/loudness of the note
   elif char in space:     # if the characteristic in my name is a space, the note will rest 
      pitch= REST
      duration = WN
      velly = 0 
      
   else:          #accounts what happens to the note if char is a consonant 
      pitch =ascii_val     #when the letter in my name is not a vowel, the duration of the note will be shorter and softer 
      duration = QN
      velly = randint(0,30)      #The volume of the note will randomly range from 0 to 30.
   
   
   n = Note(pitch, duration,velly)     #creating the note that will play for each letter 
   phr.addNote(n)    #adding the note to the phrase
    
phr.setTempo(300)
Play.midi(phr)       #Play!


