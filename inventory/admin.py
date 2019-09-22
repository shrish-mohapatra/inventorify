"""
admin.py - Used to register database models to the admin backend
Shrish Mohapatra
"""

from django.contrib import admin
from .models import Laptop

admin.site.register(Laptop)
