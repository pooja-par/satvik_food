from django.shortcuts import render, redirect
from django.views import generic
from .models import Reservation, Table
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#from django.http import HttpResponse

# Create your views here.


def home_view(request):
    return render(request, 'satvik/home.html')  # Points to satvik/templates/satvik/home.html

# View to handle table booking
def book_table(request):
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        guest_count = int(request.POST['guest_count'])  # Convert to integer

        available_tables = Table.objects.filter(capacity__gte=guest_count)
        for table in available_tables:
            if not Reservation.objects.filter(table=table, date=date, time=time).exists():
                Reservation.objects.create(
                    user=request.user,
                    table=table,
                    date=date,
                    time=time,
                    guest_count=guest_count  # Correct field usage
                )
                messages.success(request, 'Your table has been booked!')
                return redirect('view_bookings')
        messages.error(request, 'No available tables for that time.')
        return redirect('book_table')

    return render(request, 'satvik/book_table.html')

# View to show user reservations
def view_bookings(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'satvik/view_bookings.html', {'reservations': reservations})

# View to handle reservation cancellation
def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id, user=request.user)
    reservation.delete()
    messages.success(request, 'Reservation canceled successfully!')
    return redirect('view_bookings')