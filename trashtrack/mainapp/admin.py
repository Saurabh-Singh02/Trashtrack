from django.contrib import admin
from .models import SmartBin, Vehicle, DumpingArea, Company, WastePurchase
# Register your models here.

# Register each model with the admin site
admin.site.register(SmartBin)
admin.site.register(Vehicle)
admin.site.register(DumpingArea)
admin.site.register(Company)
admin.site.register(WastePurchase)