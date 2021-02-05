import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import csv

from star_wars_analysis import *

"""
-----------------------------------------count of opinion-----------------------------------------------------
"""

whoShot = []
for row in starWarsFansData[1:]:
	whoShot.append(row[-9])



countHan = 0 
countGreedo = 0
countrest= 0

for element in whoShot:
	if element == 'Han':
		countHan += 1
	elif element == 'Greedo':
		countGreedo += 1
	else:
		countrest += 1

countHan = round(countHan/nbFans *100,2)
countGreedo = round(countGreedo/nbFans *100,2)
countrest = round(countrest/nbFans *100,2)
countshot= [countHan,countGreedo,countrest]

plt.figure(4)
plt.bar(['Han','Greedo',"Don' t understand"],[countHan,countGreedo,countrest])
plt.title('Who shot first? (Number of answer)')

print(" {}% of the fans think that Han shot first, {}% think that it is Greedo and {}% don't understand the question".format(countHan, countGreedo,countrest))


"""
--------------------------------------------Count per Age-----------------------------------------------------------
"""
nbHanFansAge = [0,0,0,0,0]
nbGreedoFansAge = [0,0,0,0,0]
nbFalseFansAge = [0,0,0,0,0]

for row in starWarsFansData:
	if row[29] =='Han':
		try:
			nbHanFansAge[ages.index(row[34])]+=1
		except:
			nbHanFansAge[0]+=1
	elif row[29] =='Greedo':
		try:
			nbGreedoFansAge[ages.index(row[34])]+=1
		except:
			nbGreedoFansAge[0]+=1
	else: 
		try:
			nbFalseFansAge[ages.index(row[34])]+=1
		except:
			nbFalseFansAge[0]+=1

avgHanFansAge = np.array(nbHanFansAge)/agesFansCountAr
avgGreedoFansAge = np.array(nbGreedoFansAge)/agesFansCountAr
avgFalseFansAge = np.array(nbFalseFansAge)/agesFansCountAr

plt.figure(5)
width=0.7
x4 = np.arange(len(agesAr))
hf = plt.subplot(111) #hf = Han fans 
hf.bar(x4-width/3, avgHanFansAge,color='b',width=0.25,label='Han fans')
hf.bar(x4,avgGreedoFansAge,color='r',width=0.20, label='Greedo fans')
hf.bar(x4+width/3,avgFalseFansAge,color='g',width=0.20, label="'False' fans")
hf.set_xticks(x4)
hf.set_xticklabels(agesAr)
hf.legend()
plt.title('% of fans that believe Han shot first (by age)')
plt.show()

"""
---------------------------------------------count in function of education----------------------------------------
"""

nbHanFansEdu= [0,0,0,0,0,0]
nbGreedoFansEdu= [0,0,0,0,0,0]
nbFalseFansEdu= [0,0,0,0,0,0]

for row in starWarsFansData:
	if row[29] =='Han':
		try:
			nbHanFansEdu[education.index(row[36])]+=1
		except:
			nbHanFansEdu[0]+=1
	elif row[29] =='Greedo':
		try:
			nbGreedoFansEdu[education.index(row[36])]+=1
		except:
			nbGreedoFansEdu[0]+=1
	else: 
		try:
			nbFalseFansEdu[education.index(row[36])]+=1
		except:
			nbFalseFansEdu[0]+=1


plt.figure(6)
width=0.7
x5 = np.arange(len(educationAr))
hf = plt.subplot(111) #hf = Han fans 
hf.bar(x5-width/3, nbHanFansEdu,color='b',width=0.25,label='Han fans')
hf.bar(x5,nbGreedoFansEdu,color='r',width=0.20, label='Greedo fans')
hf.bar(x5+width/3,nbFalseFansEdu,color='g',width=0.20, label="'False' fans")
hf.set_xticks(x5)
hf.set_xticklabels(educationAr)
hf.legend()
plt.title('Distribution of the answers by education')
plt.show()