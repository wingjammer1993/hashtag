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

	g = open('tweets.txt', 'a')
	with g as outfile:
		json.dump(tweets_file, outfile, indent=4)


def accept_input_for_processing(search_string):
	get_top_tweets(search_string)
	print('this is being processed')
	return 'amruta'


