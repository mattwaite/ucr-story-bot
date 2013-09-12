#How to write 261 ledes in a fraction of a second

If you're the kind of person who worries about your job when they read about bots writing stories or the kind who tweets something snarky/dumb after reading something like [this](http://www.poynter.org/latest-news/mediawire/221669/washington-post-considered-using-robot-sportswriters/), stop.

Just stop. 

If a bot can write a better story than you can, it's not you: It's the story. It's a crappy one and a human being shouldn't be writing it.

Bots can write stories. Some of them can do a pretty decent job at basic stories. Get over it. 

What can this bot never do? Be human. Humans are flawed, empathetic, complex beings, and no bot will ever be able to capture the human experience through writing like a human can.

There is no algorithm for humanity. 

This bot will never put a human face on crime. It'll never challenge the police chief on her reasoning for crime going up or down. It'll never uncover cops re-classifying violent crimes to artificially drive crime down. It will never do any of these things. Ever.

But this bot will free you from having to write that awful "Crime is up!" or "Crime is down!" story six months after anyone cares because that's when the FBI releases the data.

Given structured data and some time, a programmer can write a bot that can write stories. __You__ can write a bot that can write stories with first-week-of-class programming skills. I can teach you how to write a bot that writes a lede of a story in a single blog post.

In fact, let's do that.

This bot is going to take some structured data from the FBI's Uniform Crime Reports and write a lede that says crime was up or down in a community. This bot will do some math, craft a lede and lay out the trend. And it will do it for every city over 100,000 people reporting data to the UCR in about a tenth of a second.

Neat, eh?

To keep this post manageable, I'm just going to write the lede. But, [I've posted a script that will write the lede, a nut graph, some trend graphs and some context graphs on GitHub](https://github.com/mattwaite/ucr-story-bot). I've also posted the data if you want to follow along.

We're going to use Python because it's beginner friendly and pretty readable as programming languages go. If you're on a Mac or Linux machine, you're good. If you're on Windows, you might need to install it.

First, create a file called ucrstory.py in the same directory as the [data file](https://raw.github.com/mattwaite/ucr-story-bot/master/UCRdata.csv). We'll put everything we need in this file and run it on the command line later.

At the top of the file, we'll need to import some libraries you're going to need, specifically the string and csv libraries. To do that, you simply type:

    import string, csv

Next, we need to read our data file. It's a CSV file -- that means comma-separated values -- which is a standard datafile format. There's a thousand tutorials online on how to read a CSV file with Python, but it's pretty straightforward.

    ucrdata = csv.reader(open('UCRdata.csv', 'rU'), dialect="excel")

In English, that says create a variable called ucrdata and stuff it with the results of the csv library's reader function, which is going to open a file called UCRdata.csv, which is a csv file created by Excel, so do some special things to deal with that. So now, we've got a thing -- in programming terms, it's called an object -- that has a bunch of data in it called ucrdata. And because that data is structured, we can do things with it.

To do what we need to do, we need to loop through each line of this file. A loop is one of the basic building blocks of programming. 

Imagine you had five sheets of paper in front of you, two white and three yellow, and you need to write your name on the yellow ones. 

In a programming loop, that would look like this: for each sheet of paper, determine its color. If it's yellow, write your name on it. If it's not, move on. Do this until you run out of paper, then quit.

So, we're going to do something similar with ucrdata, our object. We're going to read each row and do things with the data in each row.

But first, we need to skip the header row: 

    ucrdata.next()

Now, let's loop.

    for row in ucrdata:

No seriously. That's it. We've just started a loop. It means what it says. For each row in ucrdata, let's do something.

When you're inside a loop, you have to indent four spaces -- tabs are bad in Python. So add four spaces and then add this: 

        rate2012 = ((row[4]+row[9])/row(3))*100000
        rate2011 = ((row[15]+row[20])/row(14))*100000
        rate2010 = ((row[25]+row[30])/row(24))*100000
        
Let's uppack this a bit. 

First, it creates a variable called rate2012, and it says add the fifth and tenth elements in the row together. Wait, it says four and nine, not five and ten. What gives? Python uses zero based counting. So the first element in a list is zero, second is one, third is two and so on. It messes with your head for a while. So, after getting the fifth and tenth elements, it divides it by the fourth element, the total population, and multiplies the results by 100,000. 

That gives you the total per capita crime rate for a city.

So now we can do some simple comparisons with our variables.

    if rate2012 > rate2011:
        direction = "more"
    elif rate2012 < rate2011:
        direction = "less"
    else:
        direction = "the same"
            
This literally says what it says. If rate2012 is greater than rate2011, crime went up. If it went up, create a variable called direction and make it increased. Or if it went down, make it decreased. Otherwise, it held steady.

Well, that's easy. Let's add some more context using that same kind of logic. Since we have three years of data, we can determine how many years in a row crime has gone up or down. We do that like this: 
    
    if rate2012 > rate2011 > rate2010:
        trend_length_clause = ", the second year in a row figures have increased"
    elif rate2012 < rate2011 < rate2010:
        trend_length_clause = ", the second year in a row figures have declined"
    else:
        trend_length_clause = ""

You'll see the clause I've created starts with a comma. You'll see why in a minute.

Let's do some more math. How about percent change. Remember the formula for percent change is new minus old divided by old. We can multiply that by 100 to get the percentage. We can also do some more comparisons with different words to note the change.

    pct_change = (rate2012-rate2011) / rate2011)*100

    if pct_change > 0:
        pct_change_direction = "rose"
    elif pct_change < 0:
        pct_change_direction = "slid"
    else:
        pct_change_direction = "maintained"

We have a problem with this, though.

If we have a decrease, it'll appear as a negative number. Since news organizations don't publish "a -10 percent decline", we have to fix that. It's simple. We'll just create a new variable and populate it with the the absolute value of our percent change.

    pct_change_text = abs(pct_change)

Now, we've got the change, we've got the percent change and we've got the trend. All that's left is to put these pieces together.

So this is how that gets done.
    
    lede = "%s, %s -- %s police reported %.0f percent %s crime overall in 2012 compared to 2011%s, according to federal statistics." % (string.upper(row[2]), row[1], row[2], pct_change_text, direction, trend_length_clause)
    
    print lede
    
So, by now, you can recognize creating a variable called lede. The %s bit means we're going to substitute something in here, which we'll name later. Think of it like Mad Libs you did as a kid. You're swapping in nouns, verbs, adjectives, etc. The %.0f bit is the same idea, but it's a different type of data called a float, which is just a number with a decimal point. The .0 means don't include any digits after the decimal point. In other words, round our percent changes to the nearest whole number.

After the quote mark, you'll see a percent sign, then a list of variables and references in parenthesis. These are the things we're going to be swapping in. For this to work, you have to include the same number of subtitutions you said you were going to include, and they'd better be in the right order or your story is going to read wrong. 

So what does this produce? This: 

ANAHEIM, Calif. -- Anaheim police reported 15 percent more crime overall in 2012 compared to 2011, the second year in a row figures have increased, according to federal statistics.

Except that it will do it 261 times, one for each city we have data for, re-written for each depending on the data we have.

All in a blink of an eye.

Award winning? Not hardly. Gripping? Nope. But these UCR stories never are. They're drudgery. You do them to log them in, because the UCR data comes out in the middle of the following year.

If a bot can write the story better than you can, let it. Use your humanity to find a better one.

Note: If you're interested, a more complete bot that writes two more paragraphs is [posted on GitHub](https://github.com/mattwaite/ucr-story-bot).