from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
    return HttpResponseRedirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
