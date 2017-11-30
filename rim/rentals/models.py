# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
    note = models.CharField(max_length=200)

class Gear(models.Model):
    description = models.CharField(max_length=200)

class Rental(models.Model):
    person = models.ForeignKey(Person)
    gear = models.ForeignKey(Gear)
    rental_date = models.DateTimeField('start date')
    return_date = models.DateTimeField('end date')

class PersonName(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    person = models.ForeignKey(Person)

class Email(models.Model):
    email_address = models.CharField(max_length=200)
    person = models.ForeignKey(Person)

class Phone(models.Model):
    phone_number = models.CharField(max_length=20)
    person = models.ForeignKey(Person)

class Relationship(models.Model):
    person = models.ForeignKey(Person, related_name='person')
    relation = models.ForeignKey(Person, related_name='relation')
    relationship = models.CharField(max_length=20)

