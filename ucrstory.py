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
    rate2012 = ((float(row[4])+float(row[9]))/float(row[3]))*100000
    rate2011 = ((float(row[15])+float(row[20]))/float(row[14]))*100000
    rate2010 = ((float(row[25])+float(row[30]))/float(row[24]))*100000

    #determine the year over year trend for the overall rate

    if rate2012 > rate2011:
        direction = "more"
    elif rate2012 < rate2011:
        direction = "less"
    else:
        direction = "the same"

    # determine the duration of the trend
    if rate2012 > rate2011 > rate2010:
        trend_length_clause = ", the second year in a row figures have increased"
    elif rate2012 < rate2011 < rate2010:
        trend_length_clause = ", the second year in a row figures have declined"
    else:
        trend_length_clause = ""

    # percent change math time -- remember (new-old)/old

    pct_change = ((rate2012-rate2011) / rate2011)*100

    # lets get some verbiage on the direction of the change
    if pct_change > 0:
        pct_change_direction = "rose"
    elif pct_change < 0:
        pct_change_direction = "slid"
    else:
        pct_change_direction = "maintained"

    #Uh oh. If we have a decrease, it'll appear as a negative number. Since news organizations don't publish "a -10 percent decline", we have to fix that. It's simple -- we just need the absolute value.
    pct_change_text = abs(pct_change)

# Now we can handle the violent crime rate

    vrate2012 = ((float(row[4]))/float(row[3]))*100000
    vrate2011 = ((float(row[15]))/float(row[14]))*100000
    vrate2010 = ((float(row[25]))/float(row[24]))*100000

    if vrate2012 > vrate2011:
        vdirection = "more"
    elif vrate2012 < vrate2011:
        vdirection = "less"
    else:
        vdirection = "the same"

    # determine the duration of the trend
    if vrate2012 > vrate2011 > vrate2010:
        vtrend_length_clause = ", the second year in a row figures have increased"
    elif vrate2012 < vrate2011 < vrate2010:
        vtrend_length_clause = ", the second year in a row figures have declined"
    else:
        vtrend_length_clause = ""

    # percent change math time -- remember (new-old)/old

    vpct_change = ((vrate2012-vrate2011) / vrate2011)*100

    # lets get some verbiage on the direction of the change
    if vpct_change > 0:
        vpct_change_direction = "rose"
    elif vpct_change < 0:
        vpct_change_direction = "slid"
    else:
        vpct_change_direction = "maintained"

    #Uh oh. If we have a decrease, it'll appear as a negative number. Since news organizations don't publish "a -10 percent decline", we have to fix that. It's simple -- we just need the absolute value.
    vpct_change_text = abs(vpct_change)

    #write the story
    if pct_change > 1:
        lede = "%s, %s -- %s police reported %.0f percent %s crime overall in 2012 compared to 2011%s, according to federal statistics." % (string.upper(row[2]), row[1], row[2], pct_change_text, direction, trend_length_clause)
    else:
        lede = "%s, %s -- %s police reported a little %s crime overall in 2012 compared to 2011%s, according to federal statistics." % (string.upper(row[2]), row[1], row[2], direction, trend_length_clause)

    second = "The violent crime rate %s by %.0f percent from 2011 to 2012, the Federal Bureau of Investigation reported. In 2012, %s police reported %s violent crimes per 100,000 residents, versus %s violent crimes per 100,000 residents in 2011." % (vpct_change_direction, vpct_change_text, row[2], row[4], row[15])

#    context = "The 2010 violent crime rate in %s is %s than the statewide rate of %s per 100,000 people, and %s than the national rate of %s per capita." % (clean_city, state_comp, state[3], national_comp, national[3])
    story = lede + "\n" + second # + "\n" + context + "\n"

    print story
    
