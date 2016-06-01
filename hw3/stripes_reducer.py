#!/usr/bin/env python
## stripes_reducer.py
## Author: Megan Jasek
## Description: reducer code for HW3.5A
## This function expects keys to come in sorted.  It sums the values of all keys that are the same,
## then it outputs each product pair combination with its total sum of all of its values.

import sys
from collections import Counter

# Create a counter called Reducer Counters that will count the calls to function
sys.stderr.write("reporter:counter:Reducer Counters,Calls,1\n")

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
            # if the count is greater than 100, output all product pairs from the
            # key and all of the elements in its associated Counter object
            for k in cur_count:
                if cur_count[k] >= 100:
                    print('(%s,%s)\t%d' % (cur_key, k, cur_count[k]))
        cur_key = key
        cur_count = value

# Print the final element
for k in cur_count:
    if cur_count[k] >= 100:
        print('(%s,%s)\t%d' % (cur_key, k, cur_count[k]))