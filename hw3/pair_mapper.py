#!/usr/bin/env python
## mapper.py
## Author: Megan Jasek
## Description: mapper code for HW3.4A
## Print the count of 1 for each unique product pair in each basket in the input file and print the
## basket count with the special marker: (*basketcount,*basketcount)

import sys

# Create a counter called Mapper Counters that will count the calls to function
sys.stderr.write("reporter:counter:Mapper Counters,Calls,1\n")

count_basket = 0

# input comes from STDIN (standard input)
# Break up each line by space delimiter and print each product pair in each basket with a count of 1.
# Keep track of the basket count and print it with a special marker: (*basketcount,*basketcount)
# so that it is passed to the reducer
for line in sys.stdin:
    products = line.split()
    for i in range(len(products)-1):
        pi = products[i]
        for pj in products[i+1:]:
            if pi > pj:
                print('(%s,%s)\t%d' % (pj, pi, 1))
            else:
                print('(%s,%s)\t%d' % (pi, pj, 1))
    count_basket += 1

print('(*basketcount,*basketcount)\t%d' % (count_basket))