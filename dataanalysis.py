#This code is our first attempt to analyze Amazon product ranking utilizing linear regression.


import pandas as pd
import numpy as np
import re
from sklearn.linear_model import LinearRegression

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

content = pd.read_csv("thirdamazonpageprices.csv") #read in the file into pandas
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

content["botranking"] = 0 #creates a new column and initializes all values to zero

counter = 1 #what the number will be set to in the row
atfile = 0 #where the loop is according to the file
next = 0 #when zero, loop continues. Loop exits when this is changed
numofrows = content.shape[0] #checks the number of rows 

print("Debugging message: Variables set!")

while(next == 0):
	if(content.at[atfile, "category"] == "Full"):
		content.at[atfile, "botranking"] = counter
		counter = counter + 1
		atfile = atfile + 1
	else:
		next = 1

#print("Debugging message: Category 'Full' complete")

counter = 1
next = 0

while(next == 0):
	if(content.at[atfile, "category"] == "Audio Headphones"):
		content.at[atfile, "botranking"] = counter
		counter = counter + 1
		atfile = atfile + 1
	else:
		next = 1

#print("Debugging message: Category 'Audio Headphones' complete")

counter = 1
next = 0

while(next == 0):
	if(content.at[atfile, "category"] == "Over-Ear Headphones"):
		content.at[atfile, "botranking"] = counter
		counter = counter + 1
		atfile = atfile + 1
	else:
		next = 1

#print("Debugging message: Category 'Over-Ear Headphones' complete")

counter = 1
next = 0

while(next == 0):
	if(content.at[atfile, "category"] == "On-Ear Headphones"):
		content.at[atfile, "botranking"] = counter
		counter = counter + 1
		atfile = atfile + 1
	else:
		next = 1

#print("Debugging message: Category 'On-Ear Headphones' complete")

counter = 1
next = 0

while(next == 0):
	if(content.at[atfile, "category"] == "Earbud & In-Ear Headphones"):
		content.at[atfile, "botranking"] = counter
		counter = counter + 1
		atfile = atfile + 1
	else:
		next = 1

#print("Debugging message: Category 'Earbud & In-Ear Headphones' complete")

counter = 1
next = 0

while(next == 0):
	if(content.at[atfile, "category"] == "Headphone Earpads"):
		content.at[atfile, "botranking"] = counter
		counter = counter + 1
		atfile = atfile + 1
	else:
		next = 1

#print("Debugging message: Category 'Headphone Earpads' complete")

counter = 1
next = 0

while(next == 0):
	if(atfile < numofrows and content.at[atfile, "category"] == "Electronic Equipment Warranties"):
		content.at[atfile, "botranking"] = counter
		counter = counter + 1
		atfile = atfile + 1
	else:
		next = 1

#print("Debugging message: Category 'Electronic Equipment Warranties' complete. This should mean that the bot ranks were successfully implemented!")
print(content)


#start of regression
numpyfullarray = content.to_numpy()
#print(numpyfullarray)
pricearray = numpyfullarray[:, [1]]
botrankingarray = numpyfullarray[:, [5]]
ratingarray = numpyfullarray[:, [3]]
numofratingsarray = numpyfullarray[:, [4]]
x = numpyfullarray[:, [1,3,4]]

model = LinearRegression().fit(x, botrankingarray)

r_sq = model.score(x, botrankingarray)

print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)










