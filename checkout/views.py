from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from bag.contexts import bag_contents # returns dictionary

import stripe

# Create your views here.
def checkout(request):
    bag = request.session.get('bag',{})
    if not bag:
        messages.error(request, "nothin in bag bitch")
        return redirect(reverse('products'))
    
    current_bag = bag_contents(request) #gets bag contents
    total = current_bag['grand_total'] #gets the total from bag
    stripe_total = round(total * 100) #makes total an interger for Stripe

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KWikAHQSL2YtrmHIl710YHRFZuUDIR9EEgbCqrVJ2KGCCaCDjxwOan5o7QxuxAnmyMX1FVSTfn5K9GYIharpuXL00fYZIfLOb',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)