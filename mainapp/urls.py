from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_pict, name="Main"),
    path('tinymce/', include('tinymce.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
]