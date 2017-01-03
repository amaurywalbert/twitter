from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv
access_token = ''
access_secret = ''
consumer_key = ''
consumer_secret = ''
csvfile = open('StreamSearch.csv','a')
csvwriter = csv.writer(csvfile, delimiter = ',')


class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)
    stream.filter(track='federer',locations = '-122.75,36.8,-121.75,37.8') #não vai funcionar com string e geotag
    #stream.filter(track='djokovic')