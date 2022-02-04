from django.shortcuts import render

# Create your views here.

def index(request):
    """ this exists to return a view for the index page """
    return render(request, 'home/index.html')