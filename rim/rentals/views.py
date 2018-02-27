# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

from .forms import RentalForm, NewPersonForm, PersonForm, EmailForm, PhoneForm, AddressForm

from .models import Person

# Create your views here.
def index(request):
    context = {}
    return render(request, 'rentals/index.html', context)

def rent(request):
    if request.method == 'POST':
        rental_form = RentalForm(request.POST)

        if rental_form.is_valid():
            rental_form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        personid = request.session['person']
        rental_form = RentalForm(initial={'person': Person.objects.get(pk = personid)})
    return render(request, 'rentals/rent.html', {'rental_form': rental_form})

def new_person(request):
    if request.method == 'POST':
        person_form = PersonForm(request.POST)
        email_form = EmailForm(request.POST)
        phone_form = PhoneForm(request.POST)
        address_form = AddressForm(request.POST)

        if person_form.is_valid() and email_form.is_valid() and phone_form.is_valid() and address_form.is_valid():
            email_form = email_form.save(commit=False)
            phone_form = phone_form.save(commit=False)
            address_form = address_form.save(commit=False)
            person = person_form.save()
            email_form.person = person
            phone_form.person = person
            address_form.person = person
            email_form.save()
            phone_form.save()
            address_form.save()
            request.session['person'] = person.id
            return HttpResponseRedirect('rent.html')
    else:
        person_form = PersonForm()
        email_form = EmailForm()
        phone_form = PhoneForm()
        address_form = AddressForm()
    return render(request, 'rentals/new_person.html', {'person_form': person_form, 'email_form': email_form, 'phone_form': phone_form, 'address_form': address_form})

