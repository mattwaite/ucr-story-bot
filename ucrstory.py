#!/usr/bin/env python
# encoding: utf-8
"""
ucrstory.py

Using a csv file of data, we're going to generate a simple story out of it.

"""
#First we're going to need some libraries. You simply import them.

import string, csv

#Next, we need to read from our CSV file. So to do that, we declare a variable called ucrdata and read the data using Python's csv library.

ucrdata = csv.reader(open('UCRdata.csv', 'rU'), dialect="excel")

#The rU part is reading it in Universal Line Ending Mode. It just means it'll read it correctly. Excel outputs some funky stuff.

#We need to skip the first row, because it's a header row.

ucrdata.next()

#Now we need to write a huge loop. In Python, you write a loop simply by saying for X in Y, where X can be whatever you want to call the individual item and Y must be the thing you're looping over.

for row in ucrdata:
    '''
    The great thing now is that we have all of our data in that row, and we can address it by number. The numbers start with zero. So the first column
    is row[0] and the second column is row[1] and so on. So we have to know the layout of our data. Keeping it up in a spreadsheet is handy.    
    
    It would be good to have a strategy here. We need to do the following:
    1. Calculate the crime rate for each year we have data.
    2. Compare them with percent changes.
    3. Calculate the property crime and violent crime rates.
    4. Compare them with percent changes.
    5. Calculate rates and changes for murder, rape, robbery, aggravated assault, theft, burglary and car theft.
    6. Write a lede.
    7. Write some context graphs.
    8. Write some code to switch these up depending on the rates for individual crimes.
    '''
    
    # Let's do step 1 in our strategy. We need to calculate the crime rate for each year we have data. So we need to add property crime and violent crime, divide that by the population and mulitply by 100000 to give us the per-capita rate.

    rate2012 = ((row[4]+row[9])/row(3))*100000
    rate2011 = ((row[15]+row[20])/row(14))*100000
    rate2010 = ((row[25]+row[30])/row(24))*100000

    #determine the year over year trend
    
    if rate2012 > rate2011:
        direction = "increased"
    elif rate2012 < rate2011:
        direction = "decreased"
    else:
        direction = "held steady"
    
    # determine the duration of the trend
    if rate2012 > rate2011 > rate2010:
        trend_length_clause = ", the second year in a row crime has increased"
    elif rate2012 < rate2011 < rate2010:
        trend_length_clause = ", the second year in a row crime has declined"
    else:
        trend_length_clause = ""

    # percent change math time -- remember (new-old)/old

    pct_change = (rate2012-rate2011) / rate2011)*100

    # lets get some verbiage on the direction of the change
    if pct_change > 0:
        pct_change_direction = "rose"
    elif pct_change < 0:
        pct_change_direction = "slid"
    else:
        pct_change_direction = "maintained"

    #Uh oh. If we have a decrease, it'll appear as a negative number. Since news organizations don't publish "a -10 percent decline", we have to fix that. It's simple -- we just need the absolute value.
    pct_change_text = abs(pct_change)
    

    #This is broken -- fixing it in the morning.

    #write the story
    lede = "%s police reported %s violent crime in 2010 compared to 2009%s, according to federal statistics." % (clean_city, direction, trend_length_clause)
    second = "The violent crime rate %s by %.0f percent from 2009 to 2010, the Federal Bureau of Investigation reported. In 2010, %s police reported %s violent crimes per 100,000 residents, versus %s violent crimes per 100,000 residents in 2009." % (pct_change_direction, pct_change_text, clean_city, city[4], city[3])
    context = "The 2010 violent crime rate in %s is %s than the statewide rate of %s per 100,000 people, and %s than the national rate of %s per capita." % (clean_city, state_comp, state[3], national_comp, national[3])
    story = lede + "\n" + second + "\n" + context + "\n"

    print story
