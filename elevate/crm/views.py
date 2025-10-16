from django.shortcuts import render



from django.http import HttpResponse

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


def contact(request):


    content = {
        'first_name' : 'alawoddin',
        
    }

    return render(request, 'crm/contact.html' , content)