from django.shortcuts import render
from django.shortcuts import resolve_url as r

def home(request):
    return render(request, 'index.html')
