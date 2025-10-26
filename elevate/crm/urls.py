
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

    path('create-task' , views.create_task , name='create-task'),

    path('update-task/<str:id>' , views.update_task , name='update-task'),

    path('delete-task/<str:id>' , views.delete_task , name='delete-task'),

]
