from django import forms


class EmailSendForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'class': "form-control"}))
    text = forms.CharField(label="Text")
    # "Write your notes or questions here..."

# class EmailSendForm(forms.ModelForm):


# print(EmailSendForm(auto_id=False))
