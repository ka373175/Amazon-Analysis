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
    	return 3
    else:
    	return string.split('o')[0].strip()

def removeComma(string):

	if type(string) == float:
		return
	else:
		return string.replace(',', '')

content = pd.read_csv("edited.csv") #read EDITED (not mainamazon.csv) in the file into pandas which removed missing values

content["onpage1"] = 0 #creates a new column named onpage1 and initializes all its values to 0.

endloop = 0
atfile = 0
while(endloop == 0):
	if(content.at[atfile, "page"] <= 10):
		content.at[atfile, "onpage1"] = 1
		atfile = atfile + 1
	else:
		endloop = 1


content.price = content.price.str.replace("$","") #take out $ from price column
content.price = content.price.astype(float) #convert price column to floats
content.rating = content.rating.apply(removeAfter) #apply removeAfter function to rating column
content.numofratings = content.numofratings.apply(removeComma) #apply removeComma function to numofratings column
content.rating = content.rating.astype(float) #convert rating column to floats
content.numofratings = content.numofratings.astype(float) #convert numofratings column to floats
content.dropna().head() #drops all rows with NaN
#*** OLD CODE, USE IF NEEDED LATER
"""pricecopy = content.copy()
pricecopy = pricecopy.price.str.replace("$", "")
ratingcopy = content.copy()
print(type(ratingcopy.rating))
#ratingcopy = ratingcopy.rating.
ratingcopy = ratingcopy.rating.str.replace("out of", '')
ratingcopy = ratingcopy.str.replace("stars", '')
content['price'] = pricecopy
content['rating'] = ratingcopy""" 
#OLD CODE, USE IF NEEDED LATER

#print(content) #print content without new columns
pricemean = content.price.mean() #get the mean of the price column
pricemean = str(pricemean) #convert pricemean to string
ratingmean = content.rating.mean() #get the mean of the rating column
ratingmean = str(ratingmean) #convert ratingmean to string
#print("Testing price column mean: " + pricemean) #print the mean of the price column
#print("Testing rating column mean: " + ratingmean) #print the mean of the rating column
#print(content.price.describe()) #print the statistics of the price column


numpyfullarray = content.to_numpy()
#print(numpyfullarray)
pricearray = numpyfullarray[:, [1]]
productrankingarray = numpyfullarray[:, [1]]
ratingarray = numpyfullarray[:, [3]]
numofratingsarray = numpyfullarray[:, [4]]
amazonchoicearray = numpyfullarray[:, [7]]
onpage1array = numpyfullarray[:, [9]]
x = numpyfullarray[:, [5]]
x = x.ravel().astype(float).reshape(-1,1)
y = onpage1array.ravel().astype(float).reshape(-1,1)
print(y.dtype) #PLEASE LOOK, CURRENTLY X AND Y ARE OBJECTS THEY NEED TO BE CONVERTED TO FLOATS
print(x)
print(y)
model = LogisticRegression().fit(x, y)
print(model.predict(x))


#model = LinearRegression().fit(x, productrankingarray)

#r_sq = model.score(x, productrankingarray)
"""
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)

#NEED TO RESHAPE ARRAYS INTO AN ARRAY OF INTEGERS INSTEAD AN ARRAY OF ARRAYS
#slope, intercept, r_value, p_value, std_err = stats.linregress(amazonchoicearray,productrankingarray)



print("slope:", slope)
print("intercept:", intercept)
print("r value:", r_value)
print("p value", p_value)
print("std error:", std_err)



"""







