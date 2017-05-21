from music import *
from random import *
text = open("president Reag.txt", "r")
sco = Score("Reagan's Presidency", 120)
r_years = []
real_GDP = []
GDPGrowth = []
UU = []
C_PI = []
ds = []
ff = []
tenyy = []
discounty = []
for i in text:
   column = text.split("\t")
   years = int(column[0])
   r_years.append(years)
   realGDP = float(column[1])
   real_GDP.append(realGDP)
   GDPGrowthPerc = float(column[2])
   GDPGrowth.append(GDPGrowthPerc)
   Unemployment = float(column[3])
   UU.append(Unemployment)
   CPI = float(column[4])
   C_PI.append(CPI)
   ds= float(column[5])
   
   tenyear= float(column[6])
   fedfundrate = float(column[7])
   discountrate = float(column[8])


   
   
   
   
   

