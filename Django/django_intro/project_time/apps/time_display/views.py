from django.shortcuts import render
from time import localtime, strftime
from datetime import datetime

def time(request):
    context = {
        "times": [strftime("%b %d %Y"), strftime("%I:%M %p", localtime())]
    }
    return render(request,'time_display/time.html', context)
