from django.db import models
from tinymce.models import HTMLField
from django_ckeditor_5.fields import CKEditor5Field
from djrichtextfield.models import RichTextField


class Pictures(models.Model):
    name = models.CharField("Name of picture", max_length=50)
    date_upload = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField("Picture", upload_to="images/pictures")

    class Meta:
        verbose_name = "список картинок"
        verbose_name_plural = "список картинок"
        ordering = ["name"]

    def __str__(self):
        return self.name


class MainPicture(models.Model):
    name = models.CharField("Name of MainPicture", max_length=50)
    date_upload = models.DateTimeField(auto_now_add=True)
    main_picture = models.ImageField("Main picture", upload_to="images/mainpicture")

    class Meta:
        verbose_name = "Главная картинка"
        verbose_name_plural = "Главная картинка"

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name_surname = models.CharField("Name, Surname", max_length=60)
    description = models.TextField("Description", max_length=600)
    photo = models.ImageField("Photo", upload_to="images/photo")
    text1 = RichTextField(blank=False)
    text2 = CKEditor5Field(blank=False, config_name = 'extends')
    text3 = HTMLField(blank=False)
    # config_name = 'extends'

    class Meta:
        verbose_name = "Рекомендация"
        verbose_name_plural = "Рекомендации"

    def __str__(self):
        return self.name_surname
