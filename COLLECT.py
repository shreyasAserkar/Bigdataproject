from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1914365996-OdMlCzyEFkqpHkqUIuFfB8CncSdCTJYP8xUgrYS"
access_token_secret = "TCPgeZyZq4TKcYj2dBmfk4ftlOrXeYDyfeEiu3st2xlfT"
consumer_key = "gAsENP9Qv7FvzUsei4taAn0O4"
consumer_secret = "fOfKfiGJDYxcEh9tyeIH0mdvqEeR12Pc2hmuxKcbLmp59MmOjB"
target = open("librarydata4.txt", 'w')

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
	target.write(data)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

#these are the library IDs which are used to collect data
stream.filter(follow=['15172890', '1511254098', '32509562', '55295077', '459315164', '34720331', '20646678', '21799699', '94654133', '35066660'])
