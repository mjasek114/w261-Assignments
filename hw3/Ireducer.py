#!/usr/bin/env python
## Identity reducer.  Takes in input and outputs it directly.
import sys
# Create a counter called Reducer Counters that will count the calls to function
sys.stderr.write("reporter:counter:Reducer Counters,Identity Calls,1\n")
for line in sys.stdin:    
    print("%s" % (line.strip()))