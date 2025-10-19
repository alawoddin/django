
from django.urls import path

from . import views

urlpatterns = [

    # path('register/', register),
    path('', views.home , name='home'),

    path("about", views.about , name='about'),

    path("contact", views.contact , name='contact'),

    path('task' , views.task, name='task'),

    
    path("review", views.review , name='review'),

    path('register/' , views.register , name='register'),

    path('task-form/' , views.task_form , name='task-form'),

]
