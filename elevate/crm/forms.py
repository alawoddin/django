from django.forms import ModelForm

from . models import Task

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class TaskForm(ModelForm):
    class Meta:
        model = Task
        # fields = ['title', 'description', 'complete']
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    
    class Mate:
        Model = User
        fields = ['username', 'email', 'password1', 'password2']

        