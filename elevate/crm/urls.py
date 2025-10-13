
from django.urls import path

from . import views

urlpatterns = [

    # path('register/', register),
    path('', views.home),

    path("about", views.about),

    path('register/' , views.register),

]
