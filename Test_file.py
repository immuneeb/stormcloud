# IMPORT LIBRARIES
import tweepy
import json
import requests
import urllib.request
import time

# AUTHENTICATION DETAILS
consumer_key = 'WOZd8dpM4T5S0yuX1PXCkvHOX'
consumer_secret = 'W5WG75ba4qLBovEDQD5hv6ZBCabHn59ghG8YsVFHDvD7P9ZrJT'
access_token = '74775404-byQX7knwQS8yXnK8horWa3jeGxABp1wu7FgqoK7B7'
access_token_secret = 'ZJ2OKqSZQ3ewFjGsTkLFzfxDBTWjkpjRF5N9hpsKuDujI'

if __name__=='__main__':
    # AUTHENTICATE USER
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    # GET API HANDLER
    api = tweepy.API(auth)

### START FINDER REPLY TEST ###

while True:
    try:
        tweet = api.get_status(str(641410009247551493))
        tweet_pre = api.get_status(tweet.in_reply_to_status_id)
        print(tweet_pre)
    except tweepy.error.TweepError:
        print('ayy budday')
        break



# ### START OEMBED TEST CODE ###
#
# #https://api.twitter.com/1.1/statuses/oembed.json
# url = "https://api.twitter.com/1/statuses/oembed.json?id=635902085536608257"
#
# r = requests.get(url)
# print(r.content)

### END OEMBED TEST CODE ###
