from django.db import models
import uuid

# Create your models here.


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Person(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid1, editable=False, null=False)
    name = models.CharField(max_length=6, null=False)
    age = models.IntegerField()
    time = models.DateTimeField(auto_now=True, null=False)
