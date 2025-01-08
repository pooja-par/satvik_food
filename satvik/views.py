from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Reservation, Table
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReservationForm, RegisterForm
from datetime import date


# Home View
def home_view(request):
    return render(request, 'satvik/home.html')  # Points to satvik/templates/satvik/home.html


# View to handle table booking
def book_table(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            
            # Validate booking date to prevent past dates
            if reservation.date < date.today():
                messages.error(request, "The reservation date cannot be in the past. Please select a future date.")
                return render(request, 'satvik/book_table.html', {'form': form})
            
            # Assign the user to the reservation if authenticated
            if request.user.is_authenticated:
                reservation.user = request.user
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
            return render(request, 'satvik/book_table.html', {'form': form})
    else:
        form = ReservationForm()

    return render(request, 'satvik/book_table.html', {'form': form})


# View to display bookings
@login_required
def view_bookings(request):
    reservations = Reservation.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'satvik/view_bookings.html', {'reservations': reservations})


# View to handle reservation editing
@login_required
def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            updated_reservation = form.save(commit=False)
            
            # Validate the updated date
            if updated_reservation.date < date.today():
                messages.error(request, "The updated reservation date cannot be in the past. Please select a future date.")
                return render(request, 'satvik/edit_reservation.html', {'form': form, 'reservation': reservation})
            
            updated_reservation.save()
            messages.success(request, 'Your reservation has been updated successfully!')
            return redirect('view_bookings')
    else:
        form = ReservationForm(instance=reservation)

    return render(request, 'satvik/edit_reservation.html', {'form': form, 'reservation': reservation})


# View to display menu
def menu(request):
    return render(request, 'satvik/menu.html')


# View to display contact page
def contact(request):
    return render(request, 'satvik/contact.html')


# View to handle reservation cancellation
@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Your reservation has been cancelled successfully!')
        return redirect('view_bookings')
    return render(request, 'satvik/cancel_reservation.html', {'reservation': reservation})


# View to handle user registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in!')
            return redirect('login')  # Redirect to the login page
    else:
        form = RegisterForm()
    
    return render(request, 'satvik/register.html', {'form': form})
