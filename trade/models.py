from django.db import models

# Create your models here.
from django.db.models import ForeignKey

import users.models


class Trade(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    profile_id = models.ForeignKey(users.models.users)
    symbol = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    open_price = models.IntegerField(null=True, blank=True)
    close_price = models.IntegerField(null=True, blank=True)
    open_datetime = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    close_datetime = models.DateTimeField(null=True, blank=True, auto_now=True)
    open = models.BooleanField(null=True, blank=True, default=True)


class Wire(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(users.models.users)
    amount = models.IntegerField(null=True, blank=True)
    withdraw = models.BooleanField(null=True, blank=True)
