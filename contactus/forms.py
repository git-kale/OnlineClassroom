from django import forms

class ContactForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    city = forms.CharField()
    subject = forms.CharField()
    zip_code = forms.CharField(label='Zip')
    message = forms.CharField(max_length=100);
    check_me_out = forms.BooleanField(required=False)