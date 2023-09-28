from django.contrib import admin
from machine.models import Machine, Standard, MeasurementPoint

admin.site.register(Machine)
admin.site.register(MeasurementPoint)
admin.site.register(Standard)

# Register your models here.
