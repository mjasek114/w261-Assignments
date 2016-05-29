#!/usr/bin/env python
## mapper.py
## Author: Megan Jasek
## Description: mapper code for HW3.2A

import sys

# Create a counter called Mapper Counters that will count the calls to function
sys.stderr.write("reporter:counter:Mapper Counters,Calls,1\n")

# input comes from STDIN (standard input)
# Break up each line by space delimiter and print each word with a count of 1.
for line in sys.stdin:
    for word in line.split():
        print('%s\t%d' % (word, 1))