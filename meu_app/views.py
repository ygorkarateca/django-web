from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def page_web(request):
    return render(request, 'index.html', {'nome': 'Wescley'})
