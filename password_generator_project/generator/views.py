from django.shortcuts import render
from django.http import HttpResponse
import random 

# Create your views here.
def home(request):
    # return HttpResponse('Hello there friend!')
    return render(request, 'generator/home.html', {'password':'abacbvad'})

def password(request):
    thePassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('numbers', True):
        characters.extend(list('0123456789'))
    if request.GET.get('uppercase', True):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special', True):
        characters.extend(list('@#$%^&*'))
    length =int(request.GET.get("length", 12))
    for i in range(length):
        thePassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thePassword})

def about(request):
    return render(request, 'generator/about.html')