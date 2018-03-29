from django.shortcuts import render
from . import process_search


def index(request):
	return render(request, 'homepage/header.html')


def home(request):
	if request.method == 'GET':
		data = request.GET['search']
		if data:
			data = process_search.accept_input_for_processing(data)
			return render(request, 'homepage/search.html', {'data': data})


