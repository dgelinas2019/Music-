#Create a part or phrase based on data from a file 
#use atleast 1 summary statistic somehow
#avg, median, mode 
#.sort() sorts your list in ascending order 
#output summary statistic data.write will write data to a text file for you 
##write down summary statistic in text file, median of GDP=..
#pg 213
from music import *
text = open("GDP.txt",'r')

GDPList= []
GrowthList = []

for i in text:
   column = i.split('\t')
   GDP= int(column[1])
   GDPList.append(GDP)
   Growth = float(column[2])
   GrowthList.append(Growth)
minGDP= min(GDPList)
maxGDP = max(GDPList)
minGrowth = min(GrowthList)
maxGrowth = max(GrowthList)

averageGDP = (sum(GDPList))/17
medianGrowthofGDP = (GrowthList[7]+GrowthList[8])/2
#print averageGDP
#print medianGDP
s = Score("Lets see", 120)
IDKPart = Part("the computer decides the instrument", 3)
phr = Phrase(0.0)
for j in range(len(GDPList)):
   pitch = mapScale(GDPList[j], minGDP, maxGDP, C2, C7, PENTATONIC_SCALE)
   duration = mapScale(GrowthList[j], minGrowth, maxGrowth, SN,WN)
   n = Note(pitch,duration)
   phr.addNote(n)
tempo = mapValue(averageGDP,minGDP,maxGDP,60,180)
phr.setTempo(tempo)
instr = mapValue(medianGrowthofGDP, minGrowth,maxGrowth, 1,40)
phr.setInstrument(instr)
IDKPart.addPhrase(phr)

#I added more to make it sound cool 
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


   
    