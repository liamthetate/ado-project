from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    bag = request.session.get('bag',{})
    if not bag:
        messages.error(request, "nothin in bag bitch")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KWikAHQSL2YtrmHIl710YHRFZuUDIR9EEgbCqrVJ2KGCCaCDjxwOan5o7QxuxAnmyMX1FVSTfn5K9GYIharpuXL00fYZIfLOb',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)