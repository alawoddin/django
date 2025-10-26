from django.shortcuts import render , redirect



from django.http import HttpResponse

from .models import Task

from .forms import TaskForm

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

    # queryDataSingle = Task.objects.get(id=4)
    # context = {'singleTask' : queryDataSingle}

    queryDataAll = Task.objects.all()

    context = {'allTasks' : queryDataAll}

    return render(request, 'crm/task.html' , context)

def update_task(request , id):

    taskobj = Task.objects.get(id=id)

    form = TaskForm(instance=taskobj)


    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

            return redirect('task')

    context = {'UpdateTask' : form}

    return render(request, 'crm/update-task.html' , context )

def delete_task(request , id):
    
    task = Task.objects.get(id=id)


    if request.method == 'POST':
        task.delete()

        return redirect('task')

    context = {'DeleteTask' : task}

    return render(request, 'crm/delete-task.html' , context )

def review(request):


    queryreview = Review.objects.all()

    context = {'allReviews' : queryreview}
    
    return render(request, 'crm/review.py', context )


def contact(request):


    content = {
        'first_name' : 'alawoddin',
        
    }

    return render(request, 'crm/contact.html' , content)

def create_task(request):

    form = TaskForm()


    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('task')

    context = {'TaskForm' : form}

    return render(request, 'crm/create-task.html' , context )


