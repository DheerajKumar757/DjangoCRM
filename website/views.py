from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    return render(request, 'home.html', {})
    #template = loader.get_template('home.html')
    #return HttpResponse(template.render({}, request))
