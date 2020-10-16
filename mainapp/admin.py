from django.contrib import admin
from .models import Pictures, MainPicture, Testimonial

# Register your models here.
@admin.register(Pictures)
class AdminPictures(admin.ModelAdmin):
    list_display = ["name", "picture", "date_upload"]
    name = 'mainapp'
    verbose_name = "Главная страница"


@admin.register(MainPicture)
class AdminMainPicture(admin.ModelAdmin):
    list_display = ["name", "date_upload", "main_picture"]


@admin.register(Testimonial)
class AdminTestimonial(admin.ModelAdmin):
    list_display = ["name_surname", "description", "photo"]


