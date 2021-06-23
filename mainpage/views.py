from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def Homepage(request):
    return HttpResponseRedirect("https://heheh699.herokuapp.com/next")

def Homepage1(request):
    return HttpResponseRedirect("https://youtu.be/dQw4w9WgXcQ?t=22")
