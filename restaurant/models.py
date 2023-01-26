from django.db import models
from menu.models import Menu
from authentification.models import User


class Restaurant(models.Model):
    title = models.CharField(verbose_name='Name of restaurant', max_length=255)
    description = models.TextField(verbose_name='Description')
    img = models.ImageField(verbose_name='Photo of restaurant', upload_to='users/photos/')
    menu = models.ForeignKey(Menu, verbose_name='Menu', on_delete=models.CASCADE, related_name='restauraunt')
    # menu

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

class FavouriteRestaurant(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, verbose_name='Restaurant', on_delete=models.CASCADE)
