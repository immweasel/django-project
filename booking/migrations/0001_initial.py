# Generated by Django 4.1.5 on 2023-01-25 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0002_alter_restaurant_options_alter_restaurant_menu_and_more'),
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('time', models.TimeField(verbose_name='Time')),
                ('number_of_guests', models.CharField(max_length=1, verbose_name='Number of guests')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='restaurant.restaurant', verbose_name='Restourant')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='table.table', verbose_name='Table')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
