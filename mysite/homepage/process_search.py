from twitter import *
import simplejson as json

token = '76608965-qok8bHTPepS7k0gGtbBg7tNHVtS6XgpbCL7kT8TDt'
token_secret = 'KvjPjxjRbuqs08dqABMgzkl5zCJIDGNt1sOuisdhMUEM0'
consumer_key = 'dKMoOcOFb5VhIiEDb7jn1qG0E'
consumer_secret = 'FSQPvpXy3YS3O9c19qysMibq4xNtzzYgzXX18nOFfRTaWYTXdY'

t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))


def get_top_tweets(search_string):
	tweets_file = t.search.tweets(q=search_string, result_type='recent', lang='en', count=10)
	print(type(t))
	status = tweets_file['statuses']
	top_tweets = []
	for tweet in status:
		tweet_id = tweet['id']
		top_tweets.append(t.statuses.oembed(_id=tweet_id, omit_script=True)['html'])
	return top_tweets


def accept_input_for_processing(search_string):
	top_tweets = get_top_tweets(search_string)
	return top_tweets
