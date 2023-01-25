from django.db import models
from restaurant.models import Restaurant
from table.models import Table
from authentification.models import User

class Booking(models.Model):
    restaurant = models.ForeignKey(Restaurant, verbose_name='Restourant', on_delete=models.CASCADE, related_name='booking')
    table = models.ForeignKey(Table, verbose_name='Table', on_delete=models.CASCADE, related_name='booking')
    date = models.DateField(verbose_name='Date')
    time = models.TimeField(verbose_name='Time')
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, related_name='booking')
    number_of_guests = models.CharField(verbose_name='Number of guests', max_length=1)

    def __object__(self):
        return self.user
    
    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'