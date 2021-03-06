from django.shortcuts import render, get_object_or_404

from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

# Create your views here.
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user) #profile here

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile) #is profile here
        if form.is_valid():
            form.save()
            messages.success(request, "nice, updated bitch")
        else:
            messages.error(request, 'error')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }
    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This past confirmation for order number {order_number}'
    ))

    template = 'checkout/checkou_success.html'

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)