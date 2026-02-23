from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView


# 🔹 Define home BEFORE urlpatterns
def home(request):
    return render(request, 'home.html')
def dashboard(request):
    return render(request, "dashboard.html")
def user_page(request):
    return render(request, "user_login.html")
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    # API Login
    path('login/', TokenObtainPairView.as_view(), name='login'),

    # Interactive User Page
    path('user/', user_page, name='user_page'),

    path('books/', include('books.urls')),
    path('borrow/', include('borrows.urls')),
]
