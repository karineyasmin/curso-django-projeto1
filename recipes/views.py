from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# HTTP REQUEST
def home(request):
    return HttpResponse("Home")


def sobre(request):
    return HttpResponse("Sobre")


def contato(resquest):
    return HttpResponse("Contato")
