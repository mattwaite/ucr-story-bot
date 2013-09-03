#How to write 282 ledes in a second

If you're the kind of person who worries about your job when they read about bots writing stories or the kind who tweets something snarky/dumb after reading something like [this](http://www.poynter.org/latest-news/mediawire/221669/washington-post-considered-using-robot-sportswriters/), stop.

Just stop. 

If a bot can write a better story than you can, it's not you: It's the story. It's a crappy one and a human being shouldn't be writing it.

Given structured data and some time, a programmer can write a bot that can write stories. __You__ can write a bot that can write stories with first-week-of-class programming skills. I can teach you how to write a bot that writes a lede of a story in a single blog post.

In fact, let's do that.

This bot is going to take some structured data from the FBI's Uniform Crime Reports and write a lede that says crime was up or down in a community. This bot will do some math, craft a lede and lay out the trend. And it will do it for every city over 100,000 people reporting data to the UCR in a matter of seconds.

Neat, eh?

What can this bot never do? Be human. Humans are flawed, empathetic, complex beings, and no bot will ever be able to capture the human experience through writing like a human can.

There is no algorithm for humanity. 

This bot will never put a human face on crime. It'll never challenge the police chief on her reasoning for crime going up or down. It'll never uncover cops re-classifying violent crimes to artificially drive crime down. It will never do any of these things. Ever.

But this bot will free you from having to write that awful "Crime is up!" or "Crime is down!" story six months after anyone cares because that's when the FBI releases the data.

To keep this post manageable, I'm just going to write the lede. But, [I've posted a script that will write the lede, a nut graph, some trend graphs and some context graphs on GitHub](https://github.com/mattwaite/ucr-story-bot). I've also posted the data if you want to follow along.

We're going to use Python because it's beginner friendly and pretty readable as programming languages go. So the first thing you need to do is first get used to the idea that if you type a command correctly, and you didn't tell Python to print something to the screen, you'll see nothing. Nothing means it worked. That baffles my students the first time out. 

So we need to import some libraries you're going to need, specifically the string and csv libraries. To do that, you simply type:

import string, csv

Easy, right? Note: Nothing happened. And that's good.

Next, we need to read our data file. It's a CSV file -- that means comma-separated values -- which is a standard datafile format. There's a thousand tutorials online on how to read a CSV file with Python, but it's pretty straightforward.

ucrdata = csv.reader(open('UCRdata.csv', 'rU'), dialect="excel")

In English, that says create a variable called ucrdata and stuff it with the results of the csv library's reader function, which is going to open a file called UCRdata.csv, which is a csv file created by Excel, so do some special things to deal with that. So now, we've got a thing -- in programming terms, it's called an object -- that has a bunch of data in it. And because that data is structured, we can do things with it.

To do what we need to do, we need to loop through this file. A loop is one of the basic building blocks of programming. Imagine you had five sheets of paper in front of you, two white and three yellow, and you need to write your name on the yellow ones. In a programming loop, that would look like this: for each sheet of paper, determine its color. If it's yellow, write your name on it. If it's not, move on.

So, we're going to do something similar with ucrdata, our object. We're going to read each row and do things with the data in each row.

But first, we need to skip the header row: 

ucrdata.next()

Now, let's loop.

for row in ucrdata:

No seriously. That's it. We've just started a loop. It means what it says. For each row in ucrdata, let's do something.

When you're inside a loop, you have to indent four spaces -- tabs are bad in Python. 

    rate2012 = ((row[4]+row[9])/row(3))*100000
    rate2011 = ((row[15]+row[20])/row(14))*100000
    rate2010 = ((row[25]+row[30])/row(24))*100000

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

Uh oh. If we have a decrease, it'll appear as a negative number. Since news organizations don't publish "a -10 percent decline", we have to fix that. It's simple -- we just need the absolute value.

    pct_change_text = abs(pct_change)

Now, all that's left is to put these pieces together.
    
    lede = "%s police reported %s violent crime in 2010 compared to 2009%s, according to federal statistics." % (clean_city, direction, trend_length_clause)

