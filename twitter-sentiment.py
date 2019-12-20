from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob
import time
import json





#consumer key, consumer secret, access token, access secret.
ckey="ZAPfZLcBhYEBCeRSAK5PqkTT7"
csecret="M81KvgaicyJIaQegdgXcdKDeZrSsJz4AVrGv3yoFwuItQQPMay"
atoken="2591998746-Mx8ZHsXJHzIxAaD2IxYfmzYuL3pYNVnvWoHZgR5"
asecret="LJDvEa0jL7QJXxql0NVrULTAniLobe2TAAlnBdXRfm1xF"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        analysis = TextBlob(tweet)
        print((tweet))
        print(analysis.sentiment)

        output = open("twitter-out.txt","a")
        

        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["ttc"])
