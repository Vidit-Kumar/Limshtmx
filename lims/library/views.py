from django.http import HttpResponse
from .models import Library
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserCreationForm, LoginForm

def is_superuser(user):
    return user.is_superuser

class LibraryView(LoginRequiredMixin,View):
    def get(self, request):
        books = Library.objects.values()
        context = {
            'books': books,
        }
        return render(request, 'books.html', context)

class UserListView(LoginRequiredMixin,View):
    def get(request):
        if not request.user.is_superuser:
            # Redirect to a different view or show an error message
            return HttpResponse("You are not authorized to access this page.")
        
        users = User.objects.all()
        return render(request, 'user_list.html', {'users': users})

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class UserSignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'signup.html', {'form': form})

class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
        return render(request, 'login.html', {'form': form})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
