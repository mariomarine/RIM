# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import RentalForm, CustomerForm, EmailForm, PhoneForm, AddressForm, GearForm, PackageRentalForm
from .models import Customer

# Create your views here.
def index(request):
    context = {}
    return render(request, 'rentals/index.html', context)

def thanks(request):
    return render(request, 'rentals/thanks.html', {})

def rent(request):
    if request.method == 'POST':
        rental_form = RentalForm(request.POST)
        gear_form = GearForm(request.POST)
        package_form = PackageRentalForm(request.POST)

        if rental_form.is_valid() and gear_form.is_valid():
            gear_form.save(commit=False)
            package = package_form.save(commit=False)
            gear_form.package = package
            gear_form.save()
            rental = rental_form.save()
            package.rental = rental
            package_form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        customerid = request.session['customer']
        rental_form = RentalForm(initial={'customer': Customer.objects.get(pk = customerid)})
        gear_form = GearForm()
        package_form = PackageRentalForm()
    return render(request, 'rentals/rent.html', {'rental_form': rental_form, 'gear_form': gear_form, 'package_form': package_form})

def new_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        email_form = EmailForm(request.POST)
        phone_form = PhoneForm(request.POST)
        address_form = AddressForm(request.POST)

        if customer_form.is_valid() and email_form.is_valid() and phone_form.is_valid() and address_form.is_valid():
            email_form = email_form.save(commit=False)
            phone_form = phone_form.save(commit=False)
            address_form = address_form.save(commit=False)
            customer = customer_form.save()
            email_form.customer = customer
            phone_form.customer = customer
            address_form.customer = customer
            email_form.save()
            phone_form.save()
            address_form.save()
            request.session['customer'] = customer.id
            return HttpResponseRedirect('thanks.html')
    else:
        customer_form = CustomerForm()
        email_form = EmailForm()
        phone_form = PhoneForm()
        address_form = AddressForm()
    return render(request, 'rentals/new_customer.html', {'customer_form': customer_form, 'email_form': email_form, 'phone_form': phone_form, 'address_form': address_form})

def choose_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)

        if customer_form.is_valid():
            customer = Customer.objects.filter(first_name=customer_form.cleaned_data['first_name'], last_name=customer_form.cleaned_data['last_name'], birthday=customer_form.cleaned_data['birthday'])
            request.session['customer'] = customer.get().id
            return HttpResponseRedirect('rent.html')
    else:
        customer_form = CustomerForm()
    return render(request, 'rentals/choose_customer.html', {'customer_form': customer_form})

