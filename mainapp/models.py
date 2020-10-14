from django.db import models


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