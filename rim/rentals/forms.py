from django import forms
from django.forms import ModelForm
from .models import Customer, Email, Phone, Address, Rental, Gear, PackageRental, PackageValue

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['note']
        widgets = {'birthday': forms.DateInput(attrs={'type':'date'})}

class EmailForm(ModelForm):
    class Meta:
        model = Email
        exclude = ['customer']

class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        exclude = ['customer']

class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['customer']

class RentalForm(ModelForm):
    class Meta:
        model = Rental
        exclude = ['customer', 'returned']
        widgets = {
            'rental_date': forms.DateInput(attrs={'type':'date'}),
            'return_date': forms.DateInput(attrs={'type':'date'})
        }

class GearForm(ModelForm):
    class Meta:
        model = Gear
        exclude = ['package_rental']

class PackageRentalForm(ModelForm):
    class Meta:
        model = PackageRental
        exclude = ['rental']

class PackageValueForm(ModelForm):
    class Meta:
        model = PackageValue
        exclude = []

