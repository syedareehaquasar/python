import csv
import tweepy

# Twitter API credentials
consumer_key = 'eeSnutOqqknGGGqiso8DPEfdn'
consumer_secret = 'uqKKBzpp96NJTBwEBge9wmsVKEJBdoSuMOmsaQiUphikReuJaH'
access_key = "1276097905363828736-RQfCc3FuSvhdwyYhjpoDfO7QH6Q4gB"
access_secret = "nL8jdSU1j0cuRNiGGum8uTaLrq0blGEwqI8kmfwzAMSsJ"
screen_name = "AnushkaSharma"


def get_all_tweets():
    # initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    # request first 200 tweets, the max allowed
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    alltweets.extend(new_tweets)
    # oldest = alltweets[-1].id - 1

    # keep grabbing tweets until the 3200 tweet limit is hit
    while len(new_tweets) > 0:
        print("getting tweets before id: %s" % (alltweets[-1].id - 1))
        new_tweets = api.user_timeline(screen_name=screen_name,
                                       count=200,
                                       max_id=alltweets[-1].id - 1)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print("...%s tweets downloaded so far" % (len(alltweets)))

    return alltweets


def write_tweets_to_csv(tweets):
    # transform the tweepy tweets into an array
    outtweets = [[tweet.id_str, tweet.created_at,
                  tweet.text.encode("utf-8"), tweet.retweet_count,
                  tweet.favorite_count] for tweet in tweets]

    # write the csv
    with open('%s_tweets.csv' % screen_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text", "Retweets", "Favorites"])
        writer.writerows(outtweets)

    pass


# pass in the username of the account you want to download
tweets = get_all_tweets()
write_tweets_to_csv(tweets)