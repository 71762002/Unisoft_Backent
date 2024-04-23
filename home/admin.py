from django.contrib import admin
from .models import Transfers


@admin.register(Transfers)
class TransfersAdmin(admin.ModelAdmin):
    list_display = ("id", "ext_id", "ref_name", "cardnumber", "owner", "commision", "state", "amount", "currency")