from django.shortcuts import render, redirect
from . import models
# Create your views here.
def home(request):
    student = models.habib.objects.all()
    return render(request,"home.html", {'data': student})