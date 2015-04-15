from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def example(request):
	print request
	return HttpResponse('Funciona!')