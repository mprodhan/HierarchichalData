import os
from django.shortcuts import render
from sci_fi.models import SciFi

def index(request):
    data = SciFi.objects.all()
    return render(request, "index.html", {"data": data})