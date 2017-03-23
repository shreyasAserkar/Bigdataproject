Step 1:
#COLLECTING THE DATA
	We have used tweepy library to collect data from the tweet streaming API.
	The code for this section is in COLLECT.py file
	run this code by:
		python COLLECT.py

Step 2A:
#DATA CLEANING AND CONVERSION TO CSV FORMAT
	
	CleanUsingJava.java is the code which does job of data cleaning but it is not as efficient as python code.
	therefore we are using python code.
	
	separateRetweets.py script creates two files: RE_TWEETS_BY_LIBRARY.json and TWEETS_BY_LIBRARY.json
	As json for Retweets and Tweets are different in format we are creating two separate files for them.
	and processing in STEP 2B:

Step 2B:
#DATA CLEANING AND CONVERSION TO CSV FORMAT
	GET_RETWEETS_BY_LIBRARY.py and GET_TWEETS_BY_LIBRARY.py are two scripts which analyse data generated in 
	step 2A.

	OUTPUT OF STEP 2 IS csv files having retweets and tweets with LIBRARY NAMES, IDs, TWEET, FAVOURITES, RETWEETS.
	we merge this data manually using excel in file FINAL_DATA.csv
	
	executing anyfile in this step:
	python <filename.py>

STEP 3: 
#In this step we remove the duplicate tweets which re retweeted by other users.
#It is permormed by mapreduce job written in Python
	getUniqueTweetMapper.py, getUniqueTweetReducer.py are excuted as streaming jobs

STEP 4:
#This mapredice stemp will classify each library on basis of type of tweets posted by them.
	CLASSIFY_LIBRARY_MAPPER.py and CLASSIFY_LIBRARY_REDUCER.py 
	are run as streaming jobs with input from step 3.

FINAL OUTPUT OF THIS PHASE IS LIBRARY NAME AND TYPE OF STRATEGY IT IS USING FOR GETTING AUDIENCE.

IN NEXT PHASE WE WILL BE DOING ANALYSIS AND PLOTTING GRAPH TO RELATIONS BETWEEN NUMBER OF FOLLOWERS AND 
STRATEGY EACH LIBRARY USING. 