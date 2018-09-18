from django.shortcuts import render, HttpResponse


def index(request):

    response = "Display Users here"
    return HttpResponse(response)


def new(request):

    response = "Add New Users here"
    return HttpResponse(response)


def form(request, word):
    if word == "register":
        response = "register users here"
        return HttpResponse(response)
    elif word == "new":
        response = "register new users here"
        return HttpResponse(response)
    elif word == "login":
        response = "Users Login here"
        return HttpResponse(response)
