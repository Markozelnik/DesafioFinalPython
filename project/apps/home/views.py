from django.shortcuts import redirect, render
from . import forms

# Create your views here.

from . import forms


def index(request):
    return render(request, "home/index.html")
