# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Person
from .models import Rental
from .models import Gear
from .models import PersonName
from .models import Email
from .models import Phone
from .models import Relationship

# Register your models here.
admin.site.register(Person)
admin.site.register(Rental)
admin.site.register(Gear)
admin.site.register(PersonName)
admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Relationship)

