from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Second Page")
def new(request):
    return render(request, 'second_app/table.html')