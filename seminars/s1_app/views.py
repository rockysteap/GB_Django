from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Welcome to s1_app index page!')
