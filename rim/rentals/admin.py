# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Person, Rental, Gear, Email, Phone, Address

# Register your models here.
admin.site.register(Gear)

class EmailInline(admin.StackedInline):
    model = Email

class AddressInline(admin.StackedInline):
    model = Address

class PhoneInline(admin.StackedInline):
    model = Phone

class PersonAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name'] 
    search_fields = ['first_name', 'last_name']
    inlines = [EmailInline, PhoneInline, AddressInline]

class GearInline(admin.StackedInline):
    model = Gear

class RentalAdmin(admin.ModelAdmin):
    fields = ['person', 'rental_date', 'return_date'] 
    search_fields = ['rental_date', 'return_date', 'person__first_name', 'person__last_name', 'gear__description']
    inlines = [GearInline]

admin.site.register(Person, PersonAdmin)
admin.site.register(Rental, RentalAdmin)

