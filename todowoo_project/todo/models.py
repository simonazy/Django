from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateField(null=True, blank=True)
    important = models.BooleanField(default=False)
    '''ensures changes in the parent(referenced) table are cascade to the child(referencing) table: referential integrity'''
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self) -> None:
        return self.title