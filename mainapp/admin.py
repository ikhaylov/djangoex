from django.contrib import admin
from .models import Pictures

# Register your models here.
@admin.register(Pictures)
class AdminPictures(admin.ModelAdmin):
    list_display = ["name", "picture", "date_upload"]
