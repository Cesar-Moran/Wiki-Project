from django.shortcuts import render

from . import util


def wiki(request):
    return render(request, 'entry/index.html'
    )
    
