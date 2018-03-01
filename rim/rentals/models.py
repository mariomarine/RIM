# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core import urlresolvers
from django.contrib.admin import widgets
from django import forms

# Create your models here.
class Customer(models.Model):
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    note = models.CharField(max_length=200)

class Email(models.Model):
    def __str__(self):
        return '{}'.format(self.email_address)
    email_address = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer)

class Phone(models.Model):
    phone_number = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer)

class Relationship(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer')
    relation = models.ForeignKey(Customer, related_name='relation')
    relationship = models.CharField(max_length=20)

class Address(models.Model):
    customer = models.ForeignKey(Customer)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=5)

class Rental(models.Model):
    def __str__(self):
        return '{} - {}'.format(self.rental_date, self.return_date)
    customer = models.ForeignKey(Customer)
    rental_date = models.DateField('start date')
    return_date = models.DateField('end date')
    returned = models.BooleanField(default=False)
    agree_to_tc = models.BooleanField(default=False)
    note = models.CharField(max_length=200)

class PackageValue(models.Model):
    def __str__(self):
        return '{}'.format(self.package)
    package = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class PackageRental(models.Model):
    package = models.ForeignKey(PackageValue)
    quantity = models.IntegerField()
    rental = models.ForeignKey(Rental)
    def changeform_link(self):
        if self.id:
            changeform_url = urlresolvers.reverse(
                'admin:rentals_packagerental_change', args=(self.id,)
            )
            return u'<a href="%s" target="_blank">Rental Package</a>' % changeform_url
        return u''
    changeform_link.allow_tags = True
    changeform_link.short_description = 'Link'

class Gear(models.Model):
    def __str__(self):
        return '{}'.format(self.description)
    package_rental = models.ForeignKey(PackageRental)
    gear_type = models.CharField(max_length=10)
    brand = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    size = models.CharField(max_length=10)
    note = models.CharField(max_length=200)

