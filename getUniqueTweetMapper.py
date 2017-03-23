#!/usr/bin/python
import sys

for line in sys.stdin:
    # split the line into keys
    words = line.split(',')
    #check for validity of data

    try:
        print '%s:::::%s' % (words[0]+"|"+words[3]+"|"+words[1], int(words[4])+int(words[5])) 
    except:
        pass
