# myapp/admin.py
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.index_title = ""
admin.site.unregister(Group)
admin.site.register([Kino, Aktyor, KinoAktyor, Izoh])
