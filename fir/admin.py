from django.contrib import admin
from .models import FIR, CrimeType, Victim

admin.site.register(FIR)
admin.site.register(CrimeType)
admin.site.register(Victim)
