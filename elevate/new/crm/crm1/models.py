from django.db import models

class Task(models.Model):   # ✅ Correct: Model with capital 'M'
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)