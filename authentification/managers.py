from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        user = self.model(
            email = self.normalize_email(email),
            name=name
            )

        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, name, email, password):
        user = self.create_user(
            email=email,
            name=name,
            password=password
            )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        
        user.save()

        return user