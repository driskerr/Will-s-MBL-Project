#William Ryan - Final Project

#importing of beautiful soup, pandas, numpy & matplotlib
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np
import matplotlib.pyplot as pp

#URL's to be scraped

urlOne = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018'
"""
urlTwo = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/51'
urlThree = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/101'
urlFour = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/151'
urlFive = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/201'
urlSix = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/251'
"""

#First BeautifulSoup URL
pageOne = urlopen(urlOne)
soupOne = BeautifulSoup(pageOne,'html.parser')
resultOne = soupOne.prettify()
"""
#Second BeautifulSoup URL
pageTwo = urlopen(urlTwo)
soupTwo = BeautifulSoup(pageTwo,'html.parser')
resultTwo = soupTwo.prettify()

#Third BeautifulSoup URL

pageThree = urlopen(urlThree)
soupThree = BeautifulSoup(pageThree,'html.parser')
resultThree = soupThree.prettify()

#Fourth BeautifulSoup URL

pageFour = urlopen(urlFour)
soupFour = BeautifulSoup(pageFour,'html.parser')
resultFour = soupFour.prettify()

#Fifth BeautifulSoup URL
pageFive = urlopen(urlFive)
soupFive = BeautifulSoup(pageFive,'html.parser')
resultFive = soupFive.prettify()

#Sixth BeautifulSoup URL
pageSix = urlopen(urlSix)
soupSix = BeautifulSoup(pageSix,'html.parser')
resultSix = soupFive.prettify()
"""
#Print HTML of URLs/ensure code actually works and can be scrapped


tagOne= soupOne.find_all('tr')
"""
tagTwo = soupTwo.find_all('tr')
tagThree = soupThree.find_all('tr')
tagFour = soupFour.find_all('tr')
tagFive = soupFive.find_all('tr')
tagSix = soupSix.find_all('tr')

"""
#Page One parsing of data & printing of data
title = tagOne[0:1]
playerOneThroughTen = tagOne[2:12]
playerElevenThroughTwenty = tagOne[13:23]
playerTwentyOneThroughThirty = tagOne[24:34]
playerThirtyOneThroughForty = tagOne[35:45]
playerFortyOneThroughFifty = tagOne[46:56]


for x in title:
        print(x.get_text(' '))

for x in playerOneThroughTen:
        print(x.get_text(' '))
        
playerOneThroughTen_nice = [x.get_text(' ') for x in playerOneThroughTen]


for x in playerElevenThroughTwenty:
    print(x.get_text(' '))

for x in playerTwentyOneThroughThirty:
    print(x.get_text(' '))

for x in playerThirtyOneThroughForty:
    print(x.get_text(' '))

for x in playerFortyOneThroughFifty:
    print(x.get_text(' '))
"""
#Page Two parsing & printing of data

playerFiftyOneThroughSixty = tagTwo[2:12]
playerSixtyOneThroughSeventy = tagTwo[13:23]
playerSeventyOneThroughEighty = tagTwo[24:34]
playerEightyOneThroughNinety = tagTwo[35:45]
playerNinetyOneThroughOneHundred = tagTwo[46:56]


for x in playerFiftyOneThroughSixty:
        print(x.get_text(' '))

for x in playerSixtyOneThroughSeventy:
    print(x.get_text(' '))

for x in playerSeventyOneThroughEighty:
    print(x.get_text(' '))

for x in playerEightyOneThroughNinety:
    print(x.get_text(' '))

for x in playerNinetyOneThroughOneHundred:
    print(x.get_text(' '))

#Page Three
playerOneHundredOneThroughOneHundredTen = tagThree[2:12]
playerOneHundredElevenThroughOneHundredTwenty = tagThree[13:23]
playerOneHundredTwentyOneThroughOneHundredThirty = tagThree[24:34]
playerOneHundredThirtyOneThroughOneHundredForty = tagThree[35:45]
playerOneHundredFortyOneThroughOneHundredFifty = tagThree[46:56]


for x in playerOneHundredOneThroughOneHundredTen:
    print(x.get_text(' '))

for x in playerOneHundredElevenThroughOneHundredTwenty:
    print(x.get_text(' '))

for x in playerOneHundredTwentyOneThroughOneHundredThirty:
    print(x.get_text(' '))

for x in playerOneHundredThirtyOneThroughOneHundredForty:
    print(x.get_text(' '))

for x in playerOneHundredFortyOneThroughOneHundredFifty:
    print(x.get_text(' '))

##Page Four
playerOneHundredFiftyOneThroughOneHundredSixty = tagFour[2:12]
playerOneHundredSixtyOneThroughOneHundredSeventy = tagFour[13:23]
playerOneHundredSeventyOneThroughOneHundredEighty = tagFour[24:34]
playerOneHundredEightyOneThroughOneHundredNinety = tagFour[35:45]
playerOneHundredNinetyOneThroughTwoHundred = tagFour[46:56]

for x in playerOneHundredFiftyOneThroughOneHundredSixty:
    print(x.get_text(' '))
    
    
for x in playerOneHundredSixtyOneThroughOneHundredSeventy:
    print(x.get_text(' '))

for x in playerOneHundredSeventyOneThroughOneHundredEighty:
    print(x.get_text(' '))

for x in playerOneHundredEightyOneThroughOneHundredNinety:
    print(x.get_text(' '))

for x in playerOneHundredNinetyOneThroughTwoHundred:
    print(x.get_text(' '))

##Page Five    
playerTwoHundredOneThroughTwoHundredTen = tagFive[2:12]
playerTwoHundredElevenThroughTwoHundredTwenty = tagFive[13:23]
playerTwoHundredTwentyOneThroughTwoHundredThirty = tagFive[24:34]
playerTwoHundredThirtyOneThroughTwoHundredForty = tagFive[35:45]
playerTwoHundredFortyOneThroughTwoHundredFifty = tagFive[46:56]

for x in playerTwoHundredOneThroughTwoHundredTen:
    print(x.get_text(' '))
    
for x in playerTwoHundredElevenThroughTwoHundredTwenty:
    print(x.get_text(' '))

for x in playerTwoHundredTwentyOneThroughTwoHundredThirty:
    print(x.get_text(' '))

for x in playerTwoHundredThirtyOneThroughTwoHundredForty:
    print(x.get_text(' '))

for x in playerTwoHundredFortyOneThroughTwoHundredFifty:
    print(x.get_text(' '))


##Page Six
playerTwoHundredFiftyOneThroughTwoHundredSixty = tagSix[2:12]
playerTwoHundredSixtyOneThroughTwoHundredSixtyFour = tagSix[13:23]

for x in playerTwoHundredFiftyOneThroughTwoHundredSixty:
    print(x.get_text(' '))

for x in playerTwoHundredSixtyOneThroughTwoHundredSixtyFour:
    print(x.get_text(' '))
"""
##importing to csv

#mlbStats = '/Users/wilryan/Desktop/MLBSTATS.csv'

mlbTitle = pd.DataFrame(playerOneThroughTen_nice)
mlbTitle.to_csv(r'C:\Users\Kerry.Driscoll\Desktop\MLBSTATS.csv', mode = 'w')

