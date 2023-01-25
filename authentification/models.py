from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from authentification.managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email addres', max_length=255, unique=True)
    name = models.CharField(verbose_name='Your name', max_length=255)
    photo = models.ImageField(verbose_name='Your photo', upload_to='users/photos/')

    is_active = models.BooleanField(verbose_name='Activate', default=False)    
    is_staff = models.BooleanField(verbose_name='Personal', default=False)
    is_superuser = models.BooleanField(verbose_name='Administrator', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'