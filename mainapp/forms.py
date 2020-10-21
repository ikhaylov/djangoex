from django import forms


class EmailSendForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50)
    last_name = forms.CharField(label="Last Name", max_length=50)
    email = forms.EmailField(label="E-mail")
    text = forms.Textarea("Write your notes or questions here...")
