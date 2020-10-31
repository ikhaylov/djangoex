from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main_pict, name="main"),
    # path("ckeditor5/", include('django_ckeditor_5.urls')),
    path("contact/", views.contact, name="contact"),
    path("thanks/", views.thanks, name="thanks")
]
