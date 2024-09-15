from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),  # Root URL handler
    path('book/', views.book_table, name='book_table'),
    path('reservations/', views.view_bookings, name='view_bookings'),
    path('cancel/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
]