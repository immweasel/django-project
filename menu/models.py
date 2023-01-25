from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(verbose_name='Name', max_length=255)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'