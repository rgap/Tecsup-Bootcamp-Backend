# from django.http import HttpResponse

# def hello_world(request):
#     return HttpResponse("Hello, World!")

from django.shortcuts import render


def hello_world(request):
    context = {"greeting_message": "Hello, World!"}  # Data to pass to the template
    return render(request, "hello/hello_world.html", context)
