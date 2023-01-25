from django.db import models

from restaurant.models import Restaurant
from authentification.models import User

class Review(models.Model):
    title = models.CharField(verbose_name='Name of review', max_length=255)
    description = models.TextField(verbose_name='Description')
    restaurant = models.ForeignKey(Restaurant, verbose_name='Restaurant', on_delete=models.CASCADE, related_name='review_on')
    user = models.ForeignKey(User, verbose_name='Author of review', on_delete=models.CASCADE, related_name='review_from')


    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'