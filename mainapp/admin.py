from django.contrib import admin
from django import forms
from .models import Pictures, MainPicture, Testimonial
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
@admin.register(Pictures)
class AdminPictures(admin.ModelAdmin):
    list_display = ["name", "picture", "date_upload"]
    name = 'mainapp'
    verbose_name = "Главная страница"


class BiographyAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Testimonial
        fields = "__all__"





@admin.register(MainPicture)
class AdminMainPicture(admin.ModelAdmin):
    list_display = ["name", "date_upload", "main_picture"]


@admin.register(Testimonial)
class AdminTestimonial(admin.ModelAdmin):
    list_display = ["name_surname", "photo"]
    # list_editable = ("photo", )
    search_fields = ('name_surname',)
    form = BiographyAdminForm


