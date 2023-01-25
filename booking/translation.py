from .models import Booking
from modeltranslation.translator import TranslationOptions, register

@register(Booking)
class BookingTranslation(TranslationOptions):
    fields = ('id', 'table', 'date', 'time', 'number_of_guests')