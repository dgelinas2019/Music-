#Makiing musical chords 
# A chord is multiple music notes playing at the same time

# First, I have to create a phrase and save it to a variable 
# this way the computer will be able to save and recall my phrase later if I want to 
# Then, I have to make I have to customize the notes I want to play, thereby assigning each chord pitch and duration
# Next, if I want to manipulate the phrase in any way by changing the instrument or tempo, I can do so
# Finlly, I just have to add/save the lists of pitches and durations to my phrase, and then use the Play class to play my chords 
from music import *     #Accessing music library
phr = Phrase(0.0)          #Creating a phrase that will possess all the chords I want to play 
homeChord = [C4,E4,G4]     # Creating two lists that holds chords I want to use throughout on the C major scale 
homeChord2 = [C6,E6,G6]
                              
pitches = [C4,G4,B4,[C4,E4,G5],[F4,A5,C4],[G4,B4,D4],homeChord]       #Lists holding pitches and durations of chords 
durations = [EN]*3+[HN]*3+[WN]*1     
pitches2 = [C5,G6,B5,[C5,E5,G6],[F5,A6,C5],[G5,B5,D5],homeChord2]
durations2 = [EN]*3+[HN]*3+[WN]*1
pitches3 = [C3,G4,B3,[C3,E3,G4],[F3,A4,C3],[G3,B3,D3],homeChord]
durations3 = [EN]*3+[HN]*3+[WN]*1
pitches4 = [B4,D4,G4,[A4,C4,E4,G4],G4,D4,[C4,A4,B3],[C4,B3],C3]
durations4 = [EN]*3+[WN]+[QN]*2+[HN]+[QN]+[HN]
phr.setTempo(220)                         #Setting the tempo of the phrase, phr that holds all the chords
phr.setInstrument(PIANO)                  #Setting the instrument of the phrase, phr 
phr.addNoteList(pitches,durations)        # Adds the lists of the pitches and durations to the phrase containing the chords, phr 
phr.addNoteList(pitches2,durations2)
phr.addNoteList(pitches3,durations3)
phr.addNoteList(pitches4,durations4)

Play.midi(phr)    #Play it!

