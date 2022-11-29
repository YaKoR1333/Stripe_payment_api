from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import ItemSerializer
from .models import Item
from .views import create_checkout_session, render_buy_page


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Buy': '/buy/<int:pk>/',
        'Detail_item': 'item/<int:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def get_buy(request, pk):
    checkout_session_id = create_checkout_session(request, pk)
    return checkout_session_id


@api_view(['GET'])
def get_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.price = item.get_display_price()
    serializer = ItemSerializer(item, many=False)
    return render_buy_page(request, serializer.data)


