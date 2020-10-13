from django.shortcuts import render, get_object_or_404
from .models import Pictures


def main(request):
    pictures = Pictures.objects.all()
    return render(request, "djangoex/index.html", {"pictures": pictures})
