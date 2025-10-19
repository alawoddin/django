from django.shortcuts import render



from django.http import HttpResponse

from .models import Task

from .models import Review

def register(request):
    return HttpResponse("this is for demo")


def home(request):

    context = {
        'first_name' : 'alawoddin'
    }

    return render(request, 'crm/index.html' , context)

def about(request):

    clients = [
        {
            'id' : 1,
            'name' : 'alawoddin',
            'age' : 20
        }
    ]




    return render(request , 'crm/about.html' , {'clients' : clients})

def task(request):

    # queryDataAll = Task.objects.all()

    # context = {'allTasks' : queryDataAll}

    queryDataSingle = Task.objects.get(id=4)
    context = {'singleTask' : queryDataSingle}

    return render(request, 'crm/task.html' , context)

def review(request):


    queryreview = Review.objects.all()

    context = {'allReviews' : queryreview}
    
    return render(request, 'crm/review.py', context )


def contact(request):


    content = {
        'first_name' : 'alawoddin',
        
    }

    return render(request, 'crm/contact.html' , content)


