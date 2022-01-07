from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def montly_challenge(request, month):
  challenge_text = None
  if month == "january":
    challenge_text = "no meat"
  elif month == "february":
    challenge_text = "walk the dog"
  else:
    return HttpResponseNotFound("This month is not supported")
  return HttpResponse(challenge_text)
