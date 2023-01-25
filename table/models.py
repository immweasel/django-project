from django.db import models

class Table(models.Model):
    table = models.CharField(verbose_name='table', max_length=255)

    def __str__(self):
        return self.table
    
    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'

