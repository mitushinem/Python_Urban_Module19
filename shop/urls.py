from django.urls import path
from . import views
from .views import index, game, cart

urlpatterns = [
    path('', index),
    path('shop/', game),
    path('cart/', cart),
    path('reg/', views.sign_up_by_django),
]