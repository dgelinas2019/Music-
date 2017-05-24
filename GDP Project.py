#If our countries economic well-being could be heard, what would it sound like?
#Linking data from text files to components of music to hear what our economy "sounds" like  
#Understanding how our country has grown throughout the twenty first century  
#Creating a musical part or phrase based on data from a text file 
#text files include data of annual GDP (Gross Domestic Product) per year, growth of annual GDP per year, and unemploymwnt rates between 2000 and 2016
#using atleast 1 summary statistic
#avgerage and  median

from music import *                
text = open("GDP.txt",'r')          

GDPList= []          #creating empty lists
GrowthList = []

for i in text:
   column = i.split('\t')     #separating data in text file with tabs
   GDP= int(column[1])        #converting data in columnm one to integers (GDP)
   GDPList.append(GDP)        #adding the integers (GDP) to empty GDPList
   Growth = float(column[2])  #converting the second column to floats (rate of growth)
   GrowthList.append(Growth)  #adding the floats (rate of growth) to empty GrowthList
minGDP= min(GDPList)         #storing the value of the min and max of the GDPList and GrowthList to use later     
maxGDP = max(GDPList)
minGrowth = min(GrowthList)
maxGrowth = max(GrowthList)

averageGDP = (sum(GDPList))/17      #calculating the average annual GDP between the years 2000 and 2016
medianGrowthofGDP = (GrowthList[7]+GrowthList[8])/2      #calculating the median value of the growth of GDP between 2000 and 2016

s = Score("Lets see", 120)    #Creating a score to store the musical parts, phrases, and notes
IDKPart = Part("The computer decides the instrument", 3)    #Creating part IDKPart to store phrases
phr = Phrase(0.0)       #Creating phrase phr to store notes 
for j in range(len(GDPList)):    #mapping the data of GDP stored in lists, GDPList and GrowthList, to musical pitch and duration to create a note
   pitch = mapScale(GDPList[j], minGDP, maxGDP, C2, C7, PENTATONIC_SCALE)     #mapping integers in GDPlist to pitch of note
   duration = mapScale(GrowthList[j], minGrowth, maxGrowth, SN,WN)         #mapping floats in GrowthList to duration of note 
   n = Note(pitch,duration)      #creating the note 
   phr.addNote(n)                #adding the note to the phrase
tempo = mapValue(averageGDP,minGDP,maxGDP,60,180)     #Using summary statistics of data to set the tempo of the phrase
phr.setTempo(tempo)                 #setting the tempo  
instr = mapValue(medianGrowthofGDP, minGrowth,maxGrowth, 1,40) #using the summary statistic to set the instrument the phrase will play
phr.setInstrument(instr)
IDKPart.addPhrase(phr)        #adding the phrase to the Part

#doing the same exact steps just with another text file containing data of Unemployment rates between the years 2000 and 2016
text2 = open("Unemployment.txt",'r')
UnemploymentList = []
YearList = []
for u in text2:
   column2 = u.split('\t')
   unee = float(column2[1])
   UnemploymentList.append(unee)
   unem = int(column2[0])
   YearList.append(unem)
   
minUnemployment = min(UnemploymentList)
maxUnemployment = max(UnemploymentList)
minYear = min(YearList)
maxYear = max(YearList)
GuitarPart = Part("Guitar Part", 0,9)
phr2 = Phrase(0.0)

for t in range(len(UnemploymentList)):
   pitch = mapScale(YearList[t], minYear,maxYear, C3, C7, PENTATONIC_SCALE)
   duration = mapScale(UnemploymentList[t], minUnemployment, maxUnemployment, SN,WN)
   velocity = 127
   panning = .8
   n2 = Note(pitch, duration, velocity, panning)
   phr2.addNote(n2)
phr2.setInstrument(GUITAR)
GuitarPart.addPhrase(phr2)
s.addPart(IDKPart)
s.addPart(GuitarPart)
Play.midi(s)

#Printing the summary statistcis in another text file to get a good visual of where our country stands 
data= open("stats.txt","w") 
data.write("Finding the average GDP: averageGDP = (sum(GDPList))/17")
data.write('\n')
data.write("The average GDP between 2000 and 2016 was 47,005")
data.write('\n')
data.write(str(averageGDP))
data.write('\n')
data.write("Finding the median growth rate of GDP: medianGrowthofGDP = (GrowthList[7]+GrowthList[8])/2")
data.write('\n')
data.write("The median value of growth between 2000 and 2016 was -.2%")
data.write('\n')
data.write(str(medianGrowthofGDP))
data.close()   


   
    
