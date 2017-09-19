from __future__ import unicode_literals
from django.shortcuts import render
from datetime import datetime
# Create your views here.

def index(request):
    context = {
        "time": datetime.now()
    }
    return render(request, "display/index.html", context)
