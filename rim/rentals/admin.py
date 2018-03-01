# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Customer, Rental, Gear, Email, Phone, Address, PackageValue, PackageRental

# Register your models here.
admin.site.register(Gear)

class EmailInline(admin.StackedInline):
    model = Email

class AddressInline(admin.StackedInline):
    model = Address

class PhoneInline(admin.StackedInline):
    model = Phone

class CustomerAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'birthday', 'note'] 
    search_fields = ['first_name', 'last_name', 'birthday']
    inlines = [EmailInline, PhoneInline, AddressInline]

class GearInline(admin.StackedInline):
    model = Gear

class PackageRentalAdmin(admin.ModelAdmin):
    fields = ['package', 'quantity', 'rental']
    inlines = [GearInline]
    list_display = ('package', 'quantity', 'rental')

class PackageRentalInline(admin.StackedInline):
    model = PackageRental
    readonly_fields = ('changeform_link', )

class RentalAdmin(admin.ModelAdmin):
    fields = ['customer', 'rental_date', 'return_date', 'returned', 'agree_to_tc'] 
    inlines = [PackageRentalInline]
    search_fields = ['rental_date', 'return_date', 'customer__first_name', 'customer__last_name']
    list_display = ('customer', 'rental_date', 'return_date', 'returned')
    list_filter = ('returned', )

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Rental, RentalAdmin)
admin.site.register(PackageRental, PackageRentalAdmin)
admin.site.register(PackageValue)

