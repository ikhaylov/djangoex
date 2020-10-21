from django.shortcuts import render, get_object_or_404
from .models import Pictures, MainPicture, Testimonial


def main_pict(request):
    pictures = Pictures.objects.all()
    main_pictur = MainPicture.objects.first()
    testimonials = Testimonial.objects.all()
    biography = Testimonial.objects.first()
    return render(request, "mainapp/pictures.html", {"pictures": pictures,
                                                     "main_pictur": main_pictur,
                                                     "testimonials": testimonials,
                                                     "biography": biography})

