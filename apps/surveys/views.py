from django.shortcuts import render, HttpResponse


def index(request):

    response = "Display Surveys here"
    return HttpResponse(response)


def new(request):

    response = "Add New Surveys here"
    return HttpResponse(response)


