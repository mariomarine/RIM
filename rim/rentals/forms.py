from django import forms
from django.forms import ModelForm, Form, DateTimeField
from .models import Customer, Email, Phone, Address, Rental, Gear, RentalGear, PackageValue

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
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.fields['address_1'].required = False
        self.fields['address_2'].required = False
        self.fields['city'].required = False
        self.fields['state'].required = False
        self.fields['zip_code'].required = False

class RentalForm(ModelForm):
    rental_date = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])
    return_date = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M'])
    class Meta:
        model = Rental
        exclude = ['returned']
    def __init__(self, *args, **kwargs):
        super(RentalForm, self).__init__(*args, **kwargs)
        # self.fields['customer'].disabled = True
        # self.fields['returned'].disabled = True
        # self.fields['returned'].required = False
        self.fields['note'].required = False

class GearForm(ModelForm):
    class Meta:
        model = Gear
        fields = '__all__'

class RentalGearForm(ModelForm):
    class Meta:
        model = RentalGear
        exclude = ['rental']

class PackageValueForm(ModelForm):
    class Meta:
        model = PackageValue
        exclude = []

class ChooseCustomerForm(Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email_address = forms.EmailField(label='Email Address')

