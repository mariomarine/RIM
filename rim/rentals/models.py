# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    note = models.CharField(max_length=200)

class Rental(models.Model):
    person = models.ForeignKey(Person)
    rental_date = models.DateField('start date')
    return_date = models.DateField('end date')

class Gear(models.Model):
    def __str__(self):
        return '{}'.format(self.description)

    description = models.CharField(max_length=200)
    rental = models.ForeignKey(Rental)

class Email(models.Model):
    def __str__(self):
        return '{}'.format(self.email_address)
    email_address = models.CharField(max_length=200)
    person = models.ForeignKey(Person)

class Phone(models.Model):
    phone_number = models.CharField(max_length=20)
    person = models.ForeignKey(Person)

class Relationship(models.Model):
    person = models.ForeignKey(Person, related_name='person')
    relation = models.ForeignKey(Person, related_name='relation')
    relationship = models.CharField(max_length=20)

class Address(models.Model):
    person = models.ForeignKey(Person)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=5)

