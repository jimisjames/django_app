from django.shortcuts import render, HttpResponse, redirect



def index(request):

    response = "List Blogs here"
    return HttpResponse(response)


def new(request):

    response = "Some placeholder string for 'new' path (do logic here)"
    return HttpResponse(response)


def create(request):
    print("*"*50)

    print("*"*50)
    return redirect("/blogs")


def show(request, number):

    response = "placeholder to show blog %s"
    return HttpResponse(response %(number))


def edit(request, number):

    response = "placeholder to edit blog %s"
    return HttpResponse(response %(number))


def destroy(request, number):

    return redirect("/blogs")
