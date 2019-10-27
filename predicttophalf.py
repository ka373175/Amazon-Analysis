import pandas as pd
import numpy as np
import re
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from scipy import stats

def removeAfter(string):
    """
    input is a string 
    output is a string with everything after comma removed
    """
    if type(string) == float:
    	return
    else:
    	return string.split('o')[0].strip()

def removeComma(string):
	return string.replace(',', '')

content = pd.read_csv("mainamazon.csv") #read in the file into pandas
content.price = content.price.str.replace("$","") #take out $ from price column
content.price = content.price.astype(float) #convert price column to floats
content.rating = content.rating.apply(removeAfter) #apply removeAfter function to rating column
content.numofratings = content.numofratings.apply(removeComma) #apply removeComma function to numofratings column
content.rating = content.rating.astype(float) #convert rating column to floats
content.numofratings = content.numofratings.astype(float) #convert numofratings column to floats


#print(content) #print content without new columns
pricemean = content.price.mean() #get the mean of the price column
pricemean = str(pricemean) #convert pricemean to string
ratingmean = content.rating.mean() #get the mean of the rating column
ratingmean = str(ratingmean) #convert ratingmean to string
#print("Testing price column mean: " + pricemean) #print the mean of the price column
#print("Testing rating column mean: " + ratingmean) #print the mean of the rating column
#print(content.price.describe()) #print the statistics of the price column


maxproductranking = content.shape[0]
print(maxproductranking)

tophalf = maxproductranking / 2
print(tophalf)
tophalfarray = []

endloop = 0
atfile = 1
while(endloop == 0):
	if(atfile < tophalf):
		tophalfarray.append(1)
		print("Added 1 to " + str(atfile))
		atfile = atfile + 1
	else:
		endloop = 1
endloop = 0

while(endloop == 0):
	if(atfile <= maxproductranking):
		tophalfarray.append(0)
		print("Added 0 to " + str(atfile))
		atfile = atfile + 1
	else:
		endloop = 1
print(tophalfarray)




numpyfullarray = content.to_numpy()
#print(numpyfullarray)
pricearray = numpyfullarray[:, [1]]
productrankingarray = numpyfullarray[:, [1]]
ratingarray = numpyfullarray[:, [3]]
numofratingsarray = numpyfullarray[:, [4]]
amazonchoicearray = numpyfullarray[:, [7]]


########## Log Regression #################

logx = numpyfullarray[:, [7]]
logy = tophalfarray

print(logx)
print(logy)

logmodel = LogisticRegression().fit(logx, logy)
print(logmodel)
logscore = logmodel.score(logx, logy)
predict = logmodel.predict(logx)

print(logscore)
print(predict)












