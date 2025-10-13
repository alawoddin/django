from django.contrib import admin


from django.urls import path ,  include 




urlpatterns = [
    

    path('' , include('crm.urls')),
    # path('demo' , demo)
]