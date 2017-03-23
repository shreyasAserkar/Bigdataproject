
import json
def BIFURCATETWEETS():
    '''our original data has tweets and retweets in same file.
       \nTweets and Retweets both have different formats.
       \nIt would be cumbersome to analyse the json with different format in same file.
       \nThis code sepearates retweets and tweets in 2 files.'''
    with open('final2.json', 'r') as f:
        for eachline in f:
            try:
                if "text\":\"RT" in eachline:
                    with open('RE_TWEETS_BY_LIBRARY.json', 'a') as f:
                            f.write(eachline)
                else:
                    with open('TWEETS_BY_LIBRARY.json', 'a') as f:
                        f.write(eachline)
            except:
                print "error"
if  __name__ =='__main__':BIFURCATETWEETS()
