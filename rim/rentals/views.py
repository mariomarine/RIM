# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import RentalForm, CustomerForm, EmailForm, PhoneForm, AddressForm, GearForm, RentalGearForm, ChooseCustomerForm
from .models import Customer, Email

# Create your views here.
def index(request):
    context = {}
    return render(request, 'rentals/index.html', context)

def thanks(request):
    return render(request, 'rentals/thanks.html', {'rental_id': request.session['rental_id']})

def choose_customer(request):
    if request.method == 'POST':
        chose_cust = ChooseCustomerForm(request.POST)
        errored = chose_cust.is_valid()
        email = Email.objects.get(
            email_address = chose_cust.cleaned_data['email_address'],
            customer__in = Customer.objects.filter(
                first_name = chose_cust.cleaned_data['first_name'],
                last_name = chose_cust.cleaned_data['last_name']
            )
        )
        request.session['customer'] = email.customer_id
        return HttpResponseRedirect('rent.html')

    choose_customer_form = ChooseCustomerForm()
    return render(request, 'rentals/choose_customer.html', {'choose_customer_form': choose_customer_form})

def rent(request):
    if request.method == 'POST':
        rental_form = RentalForm(request.POST)

        if rental_form.is_valid():
            rental = rental_form.save()
            request.session['rental_id'] = rental.id
            return HttpResponseRedirect('thanks.html')
    else:
        customerid = request.session['customer']
        rental_form = RentalForm(initial={'customer': Customer.objects.get(pk = customerid)})
    return render(request, 'rentals/rent.html', {'rental_form': rental_form})

def new_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        email_form = EmailForm(request.POST)
        phone_form = PhoneForm(request.POST)
        # address_form = AddressForm(request.POST)

        if customer_form.is_valid() and email_form.is_valid() and phone_form.is_valid(): # and address_form.is_valid():
            email_form = email_form.save(commit=False)
            phone_form = phone_form.save(commit=False)
            # address_form = address_form.save(commit=False)
            customer = customer_form.save()
            email_form.customer = customer
            phone_form.customer = customer
            # address_form.customer = customer
            email_form.save()
            phone_form.save()
            # address_form.save()
            request.session['customer'] = customer.id
            return HttpResponseRedirect('rent.html')
    else:
        customer_form = CustomerForm()
        email_form = EmailForm()
        phone_form = PhoneForm()
        # address_form = AddressForm()
    return render(request, 'rentals/new_customer.html', {'customer_form': customer_form, 'email_form': email_form, 'phone_form': phone_form}) #, 'address_form': address_form})

