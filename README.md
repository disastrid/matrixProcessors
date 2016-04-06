# metrixProcessors
Metrix uses MongoDB to store data. Mongo stores things in JSON, which is great!

However, you get a bunch of garbage back from Mongo that you might not want, and all this extraneous stuff makes your lovely data kind of a pain to deal with. And time stamps are all in epoch time. And a lot of other things. This means when you dump the database you're just starting.

Becasue of this I had to process this data. Here's a library of Python processors for the data that comes out of Metrix. These all return txt files - you can then save them as JSON or CSV or do whatever you want to them. Cool!

So far, it contains the following:

GroupEvents
============
When people hit the feedback buttons they sometimes hit them over and over. This skews results when you're trying to perform statistical analysis. What a pain!

This is a processor that goes through all the data in your JSON file and groups together the related events (ie, button presses that can be grouped together within 2 seconds of each other) so you can count *events* and not just button hits. Because sometimes people just want to hammer buttons, over and over again.

CountEvents
============
Now that our events are grouped, we need to count them up! This just looks in each list and counts what's in it (a list inside that list is counted as one thing).
