from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def Homepage(request):
    return HttpResponse("Hello World")


def Homepage1(request):
    return HttpResponseRedirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
