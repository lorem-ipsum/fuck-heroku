from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import uuid
import json
from .models import Greeting, Person

# Create your views here.


def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def write_server(request):
    # data = json.loads(request.body)
    # data['id'] = uuid.uuid4()
    # Person.objects.create(**data)
    # return JsonResponse({'success': True})
    return HttpResponse("<h1>Hello!</h1>")
