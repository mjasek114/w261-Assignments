#!/usr/bin/env python
## reducer.py
## Author: Megan Jasek
## Description: reducer code for HW3.4A
## This function expects keys to come in sorted.  It sums the values of all keys that are the same,
## then it outputs each key with its total sum of all of its values.  It only outputs keys with
## values of at least 100.

import sys

# Create a counter called Reducer Counters that will count the calls to function
sys.stderr.write("reporter:counter:Reducer Counters,Calls,1\n")

cur_key = None
cur_count = 0
for line in sys.stdin:
    # Split the line on tabs
    items = line.split('\t')
    # Store the 1st and 2nd items as key and value
    key = items[0]
    value = items[1]
    # If this key is the same as the previous key add the value to the count
    if key == cur_key:
        cur_count += int(value)
    # Otherwise, reset the current key and start a new count total
    else:
        if cur_key:
            if cur_count >= 100:
                print '%s\t%s' % (cur_key, cur_count)
        cur_key = key
        cur_count = int(value)

if cur_count >= 100:
    print '%s\t%s' % (cur_key, cur_count)