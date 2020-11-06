from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

    #return HttpResponse("Hello, world. You're at the polls index.")

from django.template import loader

def index(request):

    template = loader.get_template('index.html')

    context = {
        'abc': "메롱",
    }
    return HttpResponse(template.render(context, request))