from django.shortcuts import render, get_object_or_404, redirect
from .models import Pictures, MainPicture, Testimonial
from django.http import HttpResponseRedirect
from .forms import EmailSendForm
from django.core.mail import send_mail


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
    # sent = False
    if request.method == "POST":
        form = EmailSendForm(request.POST)
        print(form.errors)
        if form.is_valid():
            cd = form.cleaned_data
            # cd["last_name"] if cd["last_name"] else "null",
            cd = form.cleaned_data
            name = cd['first_name'] + " " + (cd['last_name'] if cd["last_name"] else "no surname")
            email = cd["email"]
            message = cd['text']
            # print(name, email, message)
            # sent = True
            # print(name, message, "it.nova@mail.ru", [email])
            try:
                send_mail(name, message, "sonikry.99@mail.ru", ["it.nova@mail.ru"])
            except:
                return redirect("contact")
            # logs = [name, email, message]
            # with open("logemail.txt", "a") as log:
            #     log.write(str(logs) + "\n\n\n################################################################\n\n\n")

            form.clean()
            return redirect("thanks")
    else:
        form = EmailSendForm()
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' row-form-errors'
    return render(request, "mainapp/contact.html", {"form": form})


def thanks(request):
    return render(request, "mainapp/thanks.html")


def blog(request):
    blogs = Testimonial.objects.all()
    return render(request, "mainapp/blog.html", {"blogs": blogs})

















# hello = (cd["first_name"],
#          cd["last_name"],
#          cd["email"],
#          cd["text"])

# send_mail("Name and Surname", "This is text of message", "sonikry.99@mail.ru", ["sonikry.99@gmail.com"], fail_silently=False)