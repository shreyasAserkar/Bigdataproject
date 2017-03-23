#This program converts the json database into CSV file
#Along with this fucntion it filters the data by selecting only atrributes
#which are useful for our research.

import json

with open('TWEETS_BY_LIBRARY.json', 'r') as f:
    for eachline in f:
	try:
		results=[]
    		content = json.loads('['+eachline+']')
    		for element in content:
			#this section collection the attribute which are helpful to our purpose.
				results.append(element['user']['id'])
				results.append(element['user']['name'])
				results.append(element['id'])
				results.append(element['text'].replace(',',' '))
				results.append(element['retweet_count'])
				results.append(element['favorite_count'])
		with open('TWEETS_BY_LIBRARY.csv', 'a') as f:
       			print results
       			f.write(str(results).replace('[','').replace(']',''))
			f.write('\n')
	except:
		print "error"
