#!/usr/bin/env python
## mapper.py
## Author: Megan Jasek
## Description: mapper code for HW3.5A
## Print the count of 1 for each unique product in the input file and print the
## largest basket size with a special marker: *largestbasket

import sys

# Create a counter called Mapper Counters that will count the calls to function
sys.stderr.write("reporter:counter:Mapper Counters,Calls,1\n")

count_basket = 0

# input comes from STDIN (standard input)
# Break up each line by space delimiter and print each product with a count of 1.
# Keep track of the largest basket size and print it with a special marker:  *largestbasket
# so that it is passed to the reducer
for line in sys.stdin:
    products = sorted(line.split())
    for i in range(len(products)-1):
        pi = products[i]
        H = {}
        for pj in products[i+1:]:
            H[pj] = 1
        print('%s\t%s' % (pi, H))
    count_basket += 1    
    
print('*basketcount\t%s' % ({'*basketcount':count_basket}))