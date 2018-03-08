import sys
import config
import tweepy

from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open(config.datafilename, 'a') as f:
                f.write(data)
                print('tweet received')
                return True
        except BaseException as e:
            print("Error on_data: {0}").format(str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__ == "__main__":
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)
    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(track=['#Disruptive', '#Digital', '#Data'])
