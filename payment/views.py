import stripe

from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'


def render_buy_page(request, item):
    return render(request, 'BuyPage.html', {'item': item,
                                            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY})


def create_checkout_session(request, pk):
    item = get_object_or_404(Item, pk=pk)
    your_domain = "http://127.0.0.1:8000"
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'rub',
                    'unit_amount': int(item.price),
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                },
                'quantity': 1,
            },
        ],
        metadata={
            "item_id": item.id
        },
        mode='payment',
        success_url=your_domain + '/success/',
        cancel_url=your_domain + '/cancel/',
    )
    return JsonResponse({
        'id': checkout_session.id
    })
