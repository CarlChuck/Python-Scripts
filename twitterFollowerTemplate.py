import tweepy

# create login variables
consumer_key = 'XXXXXXX'
consumer_secret = 'XXXXXXX'
access_token = 'XXXXXX'
access_token_secret = 'XXXXXXX'

# set up OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# This loop follows back those that have followed you.
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

# Swap out the topics to reflect actual topics of interest
for status in tweepy.Cursor(api.search, q='#topic').items(25):
    api.create_friendship(id=status.user.id)

for status in tweepy.Cursor(api.search, q='#topic').items(25):
    api.create_friendship(id=status.user.id)

for status in tweepy.Cursor(api.search, q='#topic').items(25):
    api.create_friendship(id=status.user.id)

for status in tweepy.Cursor(api.search, q='#topic').items(25):
    api.create_friendship(id=status.user.id)
