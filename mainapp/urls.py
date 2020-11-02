from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.main_pict, name="main"),
    path("contact/", views.contact, name="contact"),
    path("thanks/", views.thanks, name="thanks"),
    path("blog/", views.blog, name="blog"),
]
