from django.urls import path
from . import endpoints as checkout_api


urlpatterns = [
    path('checkout/', checkout_api.CheckoutEndpoint.as_view(), name="api-checkout"),
    path('books/', checkout_api.BooksEndpoint.as_view(), name="api-books"),
]