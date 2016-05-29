#!/usr/bin/env python
## product_reducer.py
## Author: Megan Jasek
## Description: reducer code for HW3.4
## This function expects keys to come in sorted.  The special value from the mapper: (*basketcount,*basketcount)
## is used here to mark total basket count.
## Because this value is so high, it will come in first from the mappers and used in the rest of 
## the function.

import sys

# Create a counter called Reducer Counters that will count the calls to function
sys.stderr.write("reporter:counter:Reducer Counters,Calls,1\n")

# Initialize the counters
count_basket = 0
i = 0

for line in sys.stdin:
    # Split the line on tabs
    items = line.split('\t')
    # Store the 1st and 2nd and items as key and value
    key = items[0]
    value = int(items[1])
    # If the value equals the special number (*basketcount,*basketcount), this indicates this is a total 
    # basket count value and it should be added to the count_basket total
    if key == '(*basketcount,*basketcount)':
        count_basket += float(value)
    else:
        # Only print the top 50 most frequent product pairs
        if i < 50:
            key1, key2 = key.strip('()').split(',')
            print('%s, %s, %s, %f' % (key1, key2, value, value/count_basket))
        i += 1