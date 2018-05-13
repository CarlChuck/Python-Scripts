import tweepy
import random
import time

# create login variables
screen_name = 'Twitter Handle'
consumer_key = 'XXXXXXX'
consumer_secret = 'XXXXXXX'
access_token = 'XXXXXX'
access_token_secret = 'XXXXXXX'

# set up OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# defines the followers and friends lists
followers = api.followers_ids(screen_name)
friends = api.friends_ids(screen_name)


# this function removes all who are not following back
def remove_non_followers():
    for f in friends:
        if f not in followers:
            api.destroy_friendship(f)
            nsecs=random.randint(5, 25)
            time.sleep(nsecs)
        else:
            continue


# This loop follows back those that have followed you.
def follow_followers():
    for follower in tweepy.Cursor(api.followers).items():
        follower.follow()


# Swap out the topics to reflect actual topics of interest
def follow_by_topic(topic):
    for status in tweepy.Cursor(api.search, q=topic).items(25):
        api.create_friendship(id=status.user.id)
        nsecs=random.randint(5, 25)
        time.sleep(nsecs)

