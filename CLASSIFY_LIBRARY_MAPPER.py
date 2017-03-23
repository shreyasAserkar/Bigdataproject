#!/usr/bin/python
import sys

for line in sys.stdin:
    # split the line into keys
    words = line.split('\t')
    #check for validity of data if not valid skip!
    try:
        print '%s:::::%s' % (words[0],words[1])

    except:
        pass
