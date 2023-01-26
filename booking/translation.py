from .models import Booking
from modeltranslation.translator import translator, TranslationOptions

class BookingTranslation(TranslationOptions):
    fields = ('table', 'date', 'time', 'number_of_guests')

translator.register(Booking, BookingTranslation)