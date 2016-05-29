#!/usr/bin/env python
## Identity mapper.  Takes in input and outputs it directly.
import sys
# Create a counter called Mapper Counters that will count the calls to function
sys.stderr.write("reporter:counter:Mapper Counters,Identity Calls,1\n")
for line in sys.stdin:    
    print("%s" % (line.strip()))