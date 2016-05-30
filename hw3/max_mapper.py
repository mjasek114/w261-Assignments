#!/usr/bin/env python
## max_mapper.py
## Author: Megan Jasek
## Description: mapper code for HW3.3A
## Print the count of 1 for each unique product in the input file and print the
## largest basket size with a special marker: *largestbasket

import sys

# Create a counter called Mapper Counters that will count the calls to function
sys.stderr.write("reporter:counter:Mapper Counters,Calls,1\n")

largest_basket = 0

# input comes from STDIN (standard input)
# Break up each line by space delimiter and print each product with a count of 1.
# Keep track of the largest basket size and print it with a special marker:  *largestbasket
# so that it is passed to the reducer
for line in sys.stdin:
    basket_size = 0
    for product in line.split():
        basket_size += 1
        print('%s\t%d' % (product, 1))
    if basket_size > largest_basket:
        largest_basket = basket_size
print('*largestbasket\t%d' % (largest_basket))