from django.db import models
from django.utils import timezone

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    done = models.BooleanField(default=False)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
