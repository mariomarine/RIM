from django import forms
from django.forms import ModelForm
from .models import Person, Email, Phone, Address, Rental

# class RentalForm(forms.Form):
    # first_name = forms.CharField(label='First Name')
    # last_name = forms.CharField(label='Last Name')
    # email_address = forms.CharField(label='Email Address')

class NewPersonForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email_address = forms.CharField(label='Email Address')

class PersonForm(ModelForm):
    class Meta:
        model = Person
        exclude = ['note']

class EmailForm(ModelForm):
    class Meta:
        model = Email
        exclude = ['person']

class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        exclude = ['person']

class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['person']

class RentalForm(ModelForm):
    class Meta:
        model = Rental
        exclude = []

