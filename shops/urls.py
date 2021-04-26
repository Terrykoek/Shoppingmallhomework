from django.urls import path
from .views import *

urlpatterns = [
    path('', view_index, name='shops_index'),
    path('show/<uuid:pk>', view_show, name='shop_show')
]