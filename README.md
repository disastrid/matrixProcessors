# metrixProcessors
Python processors for the data that comes out of Metrix. Returns JSON files, but could easily return CSVs. 

So far, it contains the following:

GroupEvents
============
When people hit the feedback buttons they sometimes hit them over and over. This skews results when you're trying to perform statistical analysis. What a pain!

This is a processor that goes through all the data in your JSON file and groups together the related events (ie, button presses that can be grouped together within 2 seconds of each other) so you can count *events* and not just button hits. Because sometimes people just want to hammer buttons, over and over again.

CountEvents
============
Now that our events are grouped, we need to count them up! This just looks in each list and counts what's in it (a list inside that list is counted as one thing).
