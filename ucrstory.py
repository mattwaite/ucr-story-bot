#!/usr/bin/env python
# encoding: utf-8
"""
ucrstory.py

Created by Matthew Waite on 2013-01-26.

Using a list of data, we're going to generate a simple story out of it. The story will have several forms, composed of paragraphs.

"""
import string

# our data, for cities, state and national
cities = [["Beatrice Police Dept","NE",433.7,281.4,280.9],
["Bellevue City Police Dept","NE",159.5,125.2,139.6],
["Columbus Police Dept","NE",107.3,69.3,122.1],
["Fremont Police Dept","NE",209.0,130.8,189.4],
["Grand Island Police Dept","NE",417.6,486.1,346.2],
["Hastings Police Dept","NE",188.8,204.1,132.5],
["Kearney Police Dept","NE",219.9,204.8,201.4],
["Lavista Police Dept","NE",58.5,52.0,101.5],
["Lexington Police Dept","NE",255.6,207.1,303.0],
["Lincoln Police Dept","NE",509.6,457.9,486.9],
["Norfolk City Police Dept","NE",147.2,148.5,181.7],
["Omaha Police Dept","NE",605.6,533.4,556.0],
["Papillion Police Dept","NE",61.3,77.9,142.9],
["Scotts Bluff Police Dept","NE",375.0,358.8,232.7],
["South Sioux Police Dept","NE",124.9,134.1,142.3]]

state = ["Nebraska",310.7,289.4,279.5]

national = ["United States of America",457.5,431.9,403.6]

#first, loop through our list of cities
for city in cities:

    #clean up the city name
    clean_city = city[0].replace(" Police Dept", "")
    #Lets get rid of that City business
    clean_city = clean_city.replace(" City", "")

    #determine the year over year trend
    
    if city[4] > city[3]:
        direction = "more"
    elif city[4] < city[3]:
        direction = "less"
    else:
        direction = "the same"
    
    # determine the duration of the trend
    if city[4] > city[3] > city[2]:
        trend_length_clause = ", the second year in a row crime has increased"
    elif city[4] < city[3] < city[2]:
        trend_length_clause = ", the second year in a row crime has declined"
    else:
        trend_length_clause = ""

    # percent change math time -- remember (new-old)/old

    pct_change = ((city[4]-city[3]) / city[3])*100

    # lets get some verbiage on the direction of the change
    if pct_change > 0:
        pct_change_direction = "increased"
    elif pct_change < 0:
        pct_change_direction = "decreased"
    else:
        pct_change_direction = "held steady"

    #Uh oh. If we have a decrease, it'll appear as a negative number. Since news organizations don't publish "a -10 percent decline", we have to fix that. It's simple -- we just need the absolute value.
    pct_change_text = abs(pct_change)

    # so we know what the trend was in the city. How about some context? What about the state?
    if city[4] > state[3]:
        state_comp = "higher"
    elif city[4] < state[3]:
        state_comp = "lower"
    else:
        state_comp = "same"
        
    #or the nation.
    if city[4] > national[3]:
        national_comp = "higher"
    elif city[4] < national[3]:
        national_comp = "lower"
    else:
        national_comp = "same"
    
    #write the story
    lead = "%s police reported %s violent crime in 2010 compared to 2009%s, according to federal statistics." % (clean_city, direction, trend_length_clause)
    second = "The violent crime rate %s by %.0f percent from 2009 to 2010, the Federal Bureau of Investigation reported. In 2010, %s police reported %s violent crimes per 100,000 residents, versus %s violent crimes per 100,000 residents in 2009." % (pct_change_direction, pct_change_text, clean_city, city[4], city[3])
    context = "The 2010 violent crime rate in %s is %s than the statewide rate of %s per 100,000 people, and %s than the national rate of %s per capita." % (clean_city, state_comp, state[3], national_comp, national[3])
    story = lead + "\n" + second + "\n" + context + "\n"

    print story