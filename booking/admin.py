from django.contrib import admin
from booking.models import Booking
from import_export.admin import ImportExportMixin
from modeltranslation.admin import TranslationAdmin

class BookingAdmin(ImportExportMixin, TranslationAdmin):
    list_display = ('id', 'table', 'date', 'time', 'user', 'number_of_guests')

admin.site.register(Booking, BookingAdmin)