from django.shortcuts import render
from time import gmtime, strftime
    
def time(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'time_display/time.html', context)
