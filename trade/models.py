from datetime import datetime

from django.db import models

# Create your models here.
from django.db.models import ForeignKey

import users.models


class Trade(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    profile_id = models.ForeignKey(users.models.Profile, on_delete=models.CASCADE)
    symbol = models.TextField(blank=True, null=True)
    quantity = models.FloatField(null=True, blank=True)
    open_price = models.FloatField(null=True, blank=True)
    close_price = models.FloatField(null=True, blank=True)
    open_datetime = models.DateTimeField(default=datetime.now())
    close_datetime = models.DateTimeField(null=True, blank=True)
    open = models.BooleanField(null=False, blank=True, default=True)


class Wire(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(users.models.Profile, on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True)
    withdraw = models.BooleanField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.withdraw:
            self.amount = self.amount * -1.0
        else:
            self.amount = self.amount * 1.0
        super(Wire, self).save(*args, **kwargs)
