from django.urls import path
from . import views
from .views import IndexView, UserSignupView, UserLoginView, UserLogoutView,LibraryView,UserListView

urlpatterns = [
    path('library/',LibraryView.as_view(),name='library'),
    path('user-list/', UserListView.as_view(), name='user_list'),
    
    path('', IndexView.as_view(), name='index'),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
