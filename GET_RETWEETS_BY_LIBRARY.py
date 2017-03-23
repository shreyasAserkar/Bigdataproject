
import json

def GET_RETWEETS_BY_LIBRARY():
	''' This program converts the json database into CSV file
	 \nAlong with this fucntion it filters the data by selecting only atrributes
	 \nwhich are useful for our research.
	'''
	with open('RE_TWEETS_BY_LIBRARY.json', 'r') as f:
	    for eachline in f:
             try:
                results=[]
                content = json.loads('['+eachline+']')
                for element in content:
                #this code will add the attributes which are helpful to us while analysis.
                    results.append(element['retweeted_status']['user']['id'])
                    results.append(element['retweeted_status']['user']['name'])
                    results.append(element['retweeted_status']['id'])
                    results.append(element['retweeted_status']['text'].replace(',',' '))
                    results.append(element['retweeted_status']['retweet_count'])
                    results.append(element['retweeted_status']['favorite_count'])
                    with open('RE_TWEETS_BY_LIBRARY.csv', 'a') as f:
                        print results
                        f.write(str(results).replace('[','').replace(']',''))
                        f.write('\n')
             except:
                print "error"
if  __name__ =='__main__':GET_RETWEETS_BY_LIBRARY()
