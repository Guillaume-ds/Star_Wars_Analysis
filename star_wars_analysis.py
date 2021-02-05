"""
Guillaume-ds | 02/2021

Analysis of data about Star Wars Viewers
I am using a data set posted by "fivethirtyheight" on github : "https://github.com/fivethirtyeight/data/tree/master/star-wars-survey"
The data set can be divided in two parts : specific questions about Star Wars and questions about the respondent 
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import csv

"""
-----------------------------------------------------Dataset---------------------------------------------------------
"""

starWarsData=[]
with open('StarWars.csv',newline='') as starWars:
	reader = csv.reader(starWars, delimiter =',')
	for row in reader:
		starWarsData.append(row)


"""
Some of the rows are of length 38, others of 1 because of " ' "
It is necessary to split the rows
"""

for index,row in enumerate(starWarsData):
	if len(row)==1:
		starWarsData[index] = row[0].split(',')

"""
As the tuition fees include a comma, the split method return rows of a lenght of 39 or 40 char
Join method is used to join the tuition fees
"""

for index,row in enumerate(starWarsData):
	if len(row)==39:
		row[35]=''.join((row[35],row[36]))
		row.pop(36)
	elif len(row)==40:
		row[35]=''.join((row[35],row[36],row[37]))
		row.pop(37)
		row.pop(36)

nbRespondent = len(starWarsData)-2

starWarsDf = pd.DataFrame(starWarsData)

"""
Some of the respondent never watched a star wars movie. Therefore their data might not be relevant.
The second column of the csv file is the answer to the question "Have you seen any of the 6 film in the star wars franchise"
"""

starWarsViewersData = []
starWarsViewersData.append(starWarsData[0])

for row in starWarsData:
	if row[1] == 'Yes':
		starWarsViewersData.append(row)

nbViewers = len(starWarsViewersData)-2

"""
Finnaly not all user are fans. The third column is the answer to the question "Do you consider yourself to be a fan of the Star Wars film franchise?"
"""

starWarsFansData = []
starWarsFansData.append(starWarsData[0])

for row in starWarsData:
	if row[2] == 'Yes':
		starWarsFansData.append(row)

nbFans = len(starWarsFansData)-2

starWarsFansDf = pd.DataFrame(starWarsFansData)
"""
The data is clean
"""

print("Analysis on Star Wars, with {} respondents, {} of which saw the 6 movies and {} are fans".format(nbRespondent,nbViewers,nbFans))


"""
-------------------------------------------------Viewers per film----------------------------------------------------------
"""


nbFilmSeen = [0,0,0,0,0,0,0]
"""
The number of film the respondents watched, the index being the number of film, and the value the number of respondent
"""
for row in starWarsData:
	nbfilm = 0
	for i in range(0,6):
		if row[3+i] != '':
			nbfilm +=1
	nbFilmSeen[nbfilm]+=1


nbFilmSeenFans = [0,0,0,0,0,0,0]
"""
The number of film the fans watched, the index being the number of film, and the value the number of fans
"""
for row in starWarsFansData:
	nbfilm = 0
	for i in range(0,6):
		if row[3+i] != '':
			nbfilm +=1
	nbFilmSeenFans[nbfilm]+=1

plt.figure(1)
plt.bar(range(7),nbFilmSeen)

plt.figure(2)
plt.bar(range(7),nbFilmSeenFans)


nbViewersFilm =[0,0,0,0,0,0]
"""
The number of viewers per film, the index being the number of the film and the value the number of viewers
"""
for i in range(0,6):
	for row in starWarsData:
		if row[3+i] != '':
			nbViewersFilm[i]+=1
nbViewersFilm = np.array(nbViewersFilm)
prctViewersFilm = np.round(nbViewersFilm/nbRespondent *100,2)


nbFansViewersFilm =[0,0,0,0,0,0]
"""
The number of fans-viewers, the index being the number of the film and the value the number of viewers
"""
for i in range(0,6):
	for row in starWarsFansData:
		if row[3+i] != '':
			nbFansViewersFilm[i]+=1
nbFansViewersFilm = np.array(nbFansViewersFilm)
prctFansViewersFilm = np.round(nbFansViewersFilm/nbFans *100,2)

"""
------------------------------------------------Age distribution----------------------------------------------------------------
"""


ages = []
for i in starWarsDf[34][2:]:
	if i not in ages:
		ages.append(i)
ages=sorted(ages)
ages[0]='NA'
agesAr=np.array(ages)


agesCount = [0,0,0,0,0]
for i in starWarsDf[34][2:]:
	if i == '':
		agesCount[0] +=1
	elif i =='18-29':
		agesCount[1]+=1
	elif i =='30-44':
		agesCount[2]+=1
	elif i =='45-60':
		agesCount[3]+=1
	elif i =='> 60':
		agesCount[4]+=1
agesCountAr=np.array(agesCount)

agesFansCount = [0,0,0,0,0]
for i in starWarsFansDf[34][2:]:
	if i == '':
		agesFansCount[0] +=1
	elif i =='18-29':
		agesFansCount[1]+=1
	elif i =='30-44':
		agesFansCount[2]+=1
	elif i =='45-60':
		agesFansCount[3]+=1
	elif i =='> 60':
		agesFansCount[4]+=1
agesFansCountAr=np.array(agesFansCount)

plt.figure(3)
width = 0.5
x3 = np.arange(len(agesAr))
ad = plt.subplot(111) #ad = ages distribution
ad.bar(x3 - width/2,agesCount,color='b',width=0.4)
ad.bar(x3 + width/3,agesFansCount,color='r',width=0.4)
ad.set_xticks(x3)
ad.set_xticklabels(agesAr)
ad.legend(['respondents','fans'])
plt.title('Age distribution of the respondents and fans')
plt.show()

"""
-------------------------------------------------Education-------------------------------------------------------
"""

education = ['NA','Less than high school degree','High school degree','Bachelor degree','Some college or Associate degree','Graduate degree']
educationAr = np.array(education)
#starWarsDf[36][2:]:

eduCount = [0,0,0,0,0,0]
for i in starWarsDf[36][2:]:
	if i == '':
		eduCount[0]+=1
	else:
		for j in range(1,6):
			if i == education[j]:
				eduCount[j]+=1

eduFansCount = [0,0,0,0,0,0]
for i in starWarsFansDf[36][2:]:
	if i == '':
		eduFansCount[0]+=1
	else:
		for j in range(1,6):
			if i == education[j]:
				eduFansCount[j]+=1

