from django.urls import path
from .views import (
    BookListApiView,
    ChekoutApiView
)

from . import views

urlpatterns = [
    path('books/', BookListApiView.as_view(),name="books"),
    path('checkout/', views.checkout,name="checkout"),
]