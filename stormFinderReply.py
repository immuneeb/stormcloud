__author__ = 'muneeb'


def stormFinderReply (END_ID, api):

    ## Function takes in START_ID (first tweet in storm) and END_ID (any tweet >= last tweet in storm) and returns
    ## a list of tweets that fit reply storm characteristics.

    import tweepy

    # define variables
    index = 0;
    storm_list = []


    # determine USER from START_ID
    current_tweet_id = str(END_ID)
    end_tweet = api.get_status(str(END_ID))
    USER = end_tweet.user.screen_name

    # pull qualifying tweets from user timeline, ignoring RTs
    while True:
        try:
            tweet = api.get_status(current_tweet_id)
            storm_list.append(tweet.text)
            index += 1

            # Find previous tweet in reply chain
            tweet_pre = api.get_status(tweet.in_reply_to_status_id)
            current_tweet_id = str(tweet_pre.id)

        except tweepy.error.TweepError:
            break

    return [storm_list, index, 0, 0]

