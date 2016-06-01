#!/usr/bin/env python
## stripes_mapper.py
## Author: Megan Jasek
## Description: mapper code for HW3.5A
## Read in each record (basket) from the product file.  Sort each basket alphabetically
## by product ID.  For each product in the basket make an array of all of the products that follow it in the
## sorted list and the count of 1.  Then print the product and its associated array.
## Print the basket count with a special marker: *basketcount

import sys

# Create a counter called Mapper Counters that will count the calls to function
sys.stderr.write("reporter:counter:Mapper Counters,Calls,1\n")

# Initialize a basket count
count_basket = 0

# input comes from STDIN (standard input)
for line in sys.stdin:
    # Break up each line by space delimiter and sort the products alphabetically by product ID
    products = sorted(line.split())
    # For each product in the record except for the last one
    for i in range(len(products)-1):
        # Store the product which will be the key for the reducer output
        pi = products[i]
        # Initialize a dictionary for storing the pairs
        H = {}
        # For each product, pj, that follows product, pi, store pj and a count of 1
        # in the dictionary H
        for pj in products[i+1:]:
            H[pj] = 1
        # For each product in the basket except for the last one, print the product and
        # its dictionary H to send to the reducer.
        print('%s\t%s' % (pi, H))
    # Keep track of the basket count and print it with a special marker: *basketcount
    # so that it is passed to the reducer
    count_basket += 1    
    
# Pass the basket count to the reducer
print('*basketcount\t%s' % ({'*basketcount':count_basket}))