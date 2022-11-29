from django.urls import path
from . import api

urlpatterns = [
    path('', api.api_overview, name='api_overview'),
    path('buy/<int:pk>/', api.get_buy, name='get_buy'),
    path('item/<int:pk>', api.get_item, name='get_item'),
]
