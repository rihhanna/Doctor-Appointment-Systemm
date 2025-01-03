from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(doctors)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Image)
admin.site.register(Contact)
