from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ this exists to return a view of the bag page """
    return render(request, 'bag/bag.html')