from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Table, Reservation

# Register your models here.

#admin.site.register(Table)
#admin.site.register(Reservation)

@admin.register(Reservation)
class ReservationAdmin(SummernoteModelAdmin):
    summernote_fields = ('special_request',)  # Use Summernote for the 'special_request' field
    list_display = ('user', 'table', 'date', 'time', 'guest_count')
    search_fields = ('user__username', 'special_request')
    list_filter = ('date', 'table')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity')
    search_fields = ('table_number', 'capacity')