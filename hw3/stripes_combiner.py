#!/usr/bin/env python
## stripes_combiner.py
## Author: Megan Jasek
## Description: combiner code for HW3.5A
## This function expects keys to come in sorted.  It sums the values in the associated arrays
## of all keys that are the same, then it outputs each key with its associative array.

import sys
from collections import Counter

# Create a counter called Combiner Counters that will count the calls to function
sys.stderr.write("reporter:counter:Combiner Counters,Calls,1\n")

cur_key = None
cur_count = Counter()
for line in sys.stdin:
    # Split the line on tabs
    items = line.split('\t')
    # Store the 1st and 2nd items as key and value
    key = items[0]
    # Convert the string in to a Python Counter object
    value = Counter(eval(items[1]))
    # If this key is the same as the previous key add the values for common
    # keys in the Counter objects together
    if key == cur_key:
        cur_count += value
    # Otherwise, reset the current key and start a new count total
    else:
        if cur_key:
            print('%s\t%s' % (cur_key, cur_count))
        cur_key = key
        cur_count = value

# Print the final element
print('%s\t%s' % (cur_key, cur_count))