from django.db import models


class Pictures(models.Model):
    name = models.CharField("Name of picture", max_length=50)
    date_upload = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField("Picture", upload_to="images/pictures", default="", blank=True)

    class Meta:
        verbose_name = "picture"
        verbose_name_plural = "pictures"
        ordering = ["name"]


