#!/usr/bin/python
import sys
def CLASSIFY_LIBRARY_MAPPER():
    '''THIS FUNCTION WILL ACT AS MAPPER AND SEND KEY VALUE TO REDUCER.
    \nwords[0] is key and words[1] is value'''
    for line in sys.stdin:
        # split the line into keys
        words = line.split('\t')
        #check for validity of data if not valid skip!
        try:
            print '%s:::::%s' % (words[0],words[1])

        except:
            pass
if  __name__ =='__main__':CLASSIFY_LIBRARY_MAPPER()
