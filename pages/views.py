from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("This is the about page.")
def ceo(request):
    return HttpResponse("CEO :Bose is a CEO of our company and..........")
# Create your views here.
