from django import forms
from .models import Contact


class EmailSendForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "email", "text")
        # error_messages = {"first_name": "Это опасная ошибка, будь внимательней"}
        # widgets = {'name': Textarea(attrs={'cols': 80, 'rows': 20})})















# class EmailSendForm(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={'class': "form-control"}))
#     last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={'class': "form-control"}))
#     email = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'class': "form-control"}))
#     text = forms.Textarea()






