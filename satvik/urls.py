from . import views
from django.urls import path, include
from django.http import HttpResponse 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_view, name='home'),  # Root URL handler
    path('book/', views.book_table, name='book_table'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('reservations/', views.view_bookings, name='view_bookings'),
    path('cancel/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    
    # Add login URL pattern
    path('login/', auth_views.LoginView.as_view(template_name='satvik/login.html'), name='login'),
]