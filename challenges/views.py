from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
  "january": "No Meat",
  "february": "Walk the dog",
  "march": "Know someone new",
  "april": "a",
  "may": "b",
  "june": "c",
  "july": "d",
  "august": "e",
  "september": "f",
  "october": "g",
  "november": "h",
  "december": "i"
}

def monthly_by_number(request, month):
  return HttpResponse(month)

def montly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
  except:
    return HttpResponseNotFound("This month is not supported")
  return HttpResponse(challenge_text)
