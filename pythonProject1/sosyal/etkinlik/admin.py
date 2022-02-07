from django.contrib import admin
from .models import Activate

#admin.site.register(Activate)
@admin.register(Activate)
class EtkinlikAdmin(admin.ModelAdmin):
    list_display = 'adi', 'turu'

