# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Customer, Rental, Gear, Email, Phone, Address, PackageValue, RentalGear

# Register your models here.
admin.site.register(Gear)

class EmailInline(admin.StackedInline):
    model = Email

class AddressInline(admin.StackedInline):
    model = Address

class PhoneInline(admin.StackedInline):
    model = Phone

class CustomerAdmin(admin.ModelAdmin):
    def get_email(self, obj):
        return Email.objects.get(pk=obj.id)
    fields = ['first_name', 'last_name', 'birthday', 'note'] 
    search_fields = ['first_name', 'last_name', 'birthday']
    list_display = ('first_name', 'last_name', 'get_email')
    inlines = [EmailInline, PhoneInline, AddressInline]

class RentalGearAdmin(admin.ModelAdmin):
    fields = ['quantity', 'rental', 'gear']
    list_display = ('gear', 'quantity', 'rental')

class RentalGearInline(admin.StackedInline):
    model = RentalGear
    readonly_fields = ('changeform_link', )

class RentalAdmin(admin.ModelAdmin):
    fields = ['customer', 'package', 'rental_date', 'return_date', 'returned'] 
    inlines = [RentalGearInline]
    search_fields = ['rental_date', 'return_date', 'customer__first_name', 'customer__last_name']
    list_display = ('customer', 'rental_date', 'return_date', 'returned')
    list_filter = ('returned', )

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Rental, RentalAdmin)
admin.site.register(RentalGear, RentalGearAdmin)
admin.site.register(PackageValue)

