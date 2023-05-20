from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bat at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51N9piuDe4Cla8ZNS2d4Jxc1aDSd9vJMUJchtPZaizNVdK72byMAmeyLDC34XinBlXO1zUiclW95nYTa2vvU7kp8Z00ljVKEXH2',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
