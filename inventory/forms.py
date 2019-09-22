"""
forms.py - Used for adding/editing data model entries
Shrish Mohapatra
"""

from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):

    class Meta:
        model = Laptop
        fields = "__all__"
