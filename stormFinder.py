__author__ = 'muneeb'


def stormFinder (END_ID, api):

    ## Function takes in START_ID (first tweet in storm) and END_ID (any tweet >= last tweet in storm) and returns
    ## a list of tweets that fit storm characteristics.

    import tweepy

    # define variables
    indexA = 0; indexB = 0; index = 0;
    tweet_no = -1
    storm_list = []
    num_list = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbol_list = [')', '.', '/']                         # define list of symbols used b/w number and tweet

    # determine USER from START_ID
    end_tweet = api.get_status(str(END_ID))
    USER = end_tweet.user.screen_name

    # pull qualifying tweets from user timeline, ignoring RTs
    for tweet in tweepy.Cursor(api.user_timeline, id=USER, max_id=str(END_ID),include_rts=False).items(500):
        if tweet_no != 1:

            # Case A: storms of the form 1/ [tweet]
            if tweet.text[0] in num_list and tweet.text[1] in symbol_list:
                storm_list.append(tweet.text)
                tweet_no = int(tweet.text[0])
                indexA += 1

            elif tweet.text[0] in num_list and tweet.text[1] in num_list and tweet.text[2] in symbol_list:
                storm_list.append(tweet.text)
                tweet_no = 10*int(tweet.text[0])+int(tweet.text[1])
                indexA += 1

            # Case B: storms of the form /1 [tweet]
            if tweet.text[0] in symbol_list and tweet.text[1] in num_list:
                storm_list.append(tweet.text)
                tweet_no = int(tweet.text[1])
                indexA += 1

            elif tweet.text[0] in symbol_list and tweet.text[1] in num_list and tweet.text[2] in num_list:
                storm_list.append(tweet.text)
                tweet_no = 10*int(tweet.text[1])+int(tweet.text[2])
                indexA += 1

            # Case C: storms of the form [tweet] 1/
            elif tweet.text[len(tweet.text)-2] in num_list and tweet.text[len(tweet.text)-1] in symbol_list:
                storm_list.append(tweet.text)
                tweet_no = int(tweet.text[len(tweet.text)-2])
                indexB += 1

            elif tweet.text[len(tweet.text)-3] in num_list and tweet.text[len(tweet.text)-2] in num_list and tweet.text[len(tweet.text)-1] in symbol_list:
                storm_list.append(tweet.text)
                tweet_no = 10*int(tweet.text[len(tweet.text)-3])+int(tweet.text[len(tweet.text)-2])
                indexB += 1

            # Case D: storms of the form [tweet] /1
            elif tweet.text[len(tweet.text)-1] in num_list and tweet.text[len(tweet.text)-2] in symbol_list:
                storm_list.append(tweet.text)
                tweet_no = int(tweet.text[len(tweet.text)-1])
                indexB += 1
            elif tweet.text[len(tweet.text)-1] in num_list and tweet.text[len(tweet.text)-2] in num_list and tweet.text[len(tweet.text)-3] in symbol_list:
                storm_list.append(tweet.text)
                tweet_no = 10*int(tweet.text[len(tweet.text)-2])+int(tweet.text[len(tweet.text)-1])
                indexB += 1

            index += 1  # Tally all tweets analyzed


            # Identify non-numbered tweet storm; send to stormFinderReply
            if index == 1 and indexA+indexB == 0:
                break

    if indexA > 0 or indexB > 0:
        return [storm_list, index, indexA, indexB]

    else:
        return 0

# since_id=str(int(START_ID)-1),