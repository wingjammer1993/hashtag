from django.shortcuts import render
from . import process_search


def index(request):
	return render(request, 'homepage/header.html')


def home(request):
	if request.method == 'GET':
		query = request.GET['search']
		if query:
			top_tweets_html = process_search.accept_input_for_processing(query)
			return render(request, 'homepage/search.html', {'query': query, 'top_tweets_html': top_tweets_html})


