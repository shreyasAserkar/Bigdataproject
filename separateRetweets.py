#our original data has tweets and retweets in same file.
#Tweets and Retweets both have different formats.
#It would be cumbersome to analyse the json with different format in same file.
#This code sepearates retweets and tweets in 2 files.

import json

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
