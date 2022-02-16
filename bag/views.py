from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ this exists to return a view of the bag page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ adds quanittiy """

    quantity = int(request.POST.get('quantity')) #comes from template as a string
    redirect_url = request.POST.get('redirect')
    bag = request.session.get('bag', {}) #get bag variable if it exists, or create it if it doesn;t

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag #overwrite the session with new info for bag
    return(redirect_url)