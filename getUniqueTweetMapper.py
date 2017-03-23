#!/usr/bin/python
import sys

def GET_UNIQUE_TWEET_MAPPER():
    'This module gets all the tweets for each library in the dataset.'
    for line in sys.stdin:
        # split the line into keys
        words = line.split(',')
        #check for validity of data
        try:
            print '%s:::::%s' % (words[0]+"|"+words[3]+"|"+words[1], int(words[4])+int(words[5]))
        except:
            pass
if  __name__ =='__main__':GET_UNIQUE_TWEET_MAPPER()

