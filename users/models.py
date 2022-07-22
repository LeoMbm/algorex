from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD
=======


>>>>>>> wire
# Create your models here.


class Profile(AbstractUser):
<<<<<<< HEAD
    email=models.EmailField(max_length=80,unique=True)
    adress = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f"{self.id} {self.username} {self.last_name} {self.first_name} {self.adress} "
=======
    adress = models.CharField(max_length=100, blank=True, null=True)
>>>>>>> wire
