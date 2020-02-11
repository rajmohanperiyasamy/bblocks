from django.http import HttpResponse
from django.template import loader
import logging
from .models import Car

def home(request):
    template = loader.get_template('task.html')
    cars = Car.objects.all()
    for item in cars:
        print (item )
    context = {'cars':cars
    }
    return HttpResponse(template.render(context, request))
