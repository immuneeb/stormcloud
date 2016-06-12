### STORMCLOUD V1.0: Fetches all tweets from a USER between START_ID and END_ID, ignoring all retweets
#TODO: Figure out embed support through API for journalism applications
#TODO: Pulling tweetstorms from entire profile
#TODO: Add funnies like stormstyle (based on type of numbering/replies used) and ability (consistency)

# Assumptions: max 99 tweets in storm, no typos around numbering


# IMPORT LIBRARIES
import tweepy
import json
import time
from stormFinder import stormFinder
from stormFinderReply import stormFinderReply
from idExtract import idExtract

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


    ### START STORMCLOUD CODE ###

    # define START_ID and END_ID
    url = input('Enter url of last tweet in storm:\n')
    # url = 'https://twitter.com/DanielleMorrill/status/635615954093772800'
    END_ID = idExtract(url)
    storm_list = []

    # call stormFinder to return [list of tweets, no of tweets in storm, indexA, indexB]
    if stormFinder(END_ID, api) != 0:
        [storm_list, tweets_analyzed, indexA, indexB] = stormFinder(END_ID, api)

    elif stormFinder(END_ID, api) == 0:
        [storm_list, tweets_analyzed, indexA, indexB] = stormFinderReply(END_ID, api)



    # reverse list and print storm
    storm_list.reverse()
    for tweet in storm_list:
        print(tweet)
        print(' ')

    # print stats
    print('tweets analyzed:',tweets_analyzed)
    print('storm size:',len(storm_list),'tweets')
    print('thanks for using stormcloud!')
    print('    ')