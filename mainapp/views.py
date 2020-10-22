from django.shortcuts import render, get_object_or_404
from .models import Pictures, MainPicture, Testimonial
from django.http import HttpResponseRedirect
from .forms import EmailSendForm


def main_pict(request):
    pictures = Pictures.objects.all()
    main_pictur = MainPicture.objects.first()
    testimonials = Testimonial.objects.all()
    biography = Testimonial.objects.first()
    return render(request, "mainapp/pictures.html", {"pictures": pictures,
                                                     "main_pictur": main_pictur,
                                                     "testimonials": testimonials,
                                                     "biography": biography})


def contact(request):
    if request.method == "POST":
        form = EmailSendForm(request.POST)
        print("--------------------------------\n", form.as_p(), "\n----------------------------------")
        if form.is_valid():
            return HttpResponseRedirect("/contact")
    else:
        form = EmailSendForm()
    return render(request, "mainapp/contact.html", {"form": form})

