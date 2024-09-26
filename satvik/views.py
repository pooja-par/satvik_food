from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Reservation, Table
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReservationForm

#from django.http import HttpResponse

# Create your views here.


def home_view(request):
    return render(request, 'satvik/home.html')  # Points to satvik/templates/satvik/home.html

# View to handle table booking
def book_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            
            # Handle anonymous users by assigning None to reservation.user if the user is not authenticated
            if request.user.is_authenticated:
                reservation.user = request.user  # Authenticated user is assigned to the reservation
            else:
                reservation.user = None  # For anonymous users, assign None to reservation.user
            
            guest_count = reservation.guest_count

            # Find available tables that can accommodate the guest count
            available_tables = Table.objects.filter(capacity__gte=guest_count)

            for table in available_tables:
                # Check if the table is available for the selected date and time
                if not Reservation.objects.filter(table=table, date=reservation.date, time=reservation.time).exists():
                    reservation.table = table
                    reservation.save()
                    messages.success(request, f'Table {table.table_number} has been booked for you!')
                    return redirect('view_bookings')

            messages.error(request, 'No available tables for the selected date and time.')
            return redirect('view_bookings')
    else:
        form = ReservationForm()

    return render(request, 'satvik/book_table.html', {'form': form})


def view_bookings(request):
    if request.user.is_authenticated:
        # Show bookings for logged-in users
        reservations = Reservation.objects.filter(user=request.user).order_by('-date', '-time')
        return render(request, 'satvik/view_bookings.html', {'reservations': reservations})
    else:
        # Redirect anonymous users to the home or login page
        messages.info(request, "Please log in to view your bookings.")
        return redirect('login')  # Redirect to login page or another relevant page


def menu(request):
    return render(request, 'satvik/menu.html')


def contact(request):
    return render(request, 'satvik/contact.html')


# View to handle reservation cancellation
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Your reservation has been cancelled successfully!')
        return redirect('view_bookings')
    return render(request, 'satvik/cancel_reservation.html', {'reservation': reservation})