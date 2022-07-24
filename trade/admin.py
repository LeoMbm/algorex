from django.contrib import admin

# Register your models here.
from trade.models import Wire, Trade

admin.site.register(Trade)
admin.site.register(Wire)