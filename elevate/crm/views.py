from django.shortcuts import render



from django.http import HttpResponse

def register(request):
    return HttpResponse("this is for demo")


def home(request):
    # return HttpResponse("this is the home page")

    return render(request, 'crm/index.html')

def about(request):
    return HttpResponse("hello this is the about page page")