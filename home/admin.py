from django.contrib import admin
from .models import Data

@admin.register(Data)
class Data(admin.ModelAdmin):
    list_display = ("date_created", "prediction")
    list_filter = ("prediction", )
