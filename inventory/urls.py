"""
urls.py - Used to map url-links to methods from views.py
Shrish Mohapatra
"""

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', view_laptops, name='index'),

    url(r'^index$', view_laptops, name='index'),
    url(r'^about$', about, name='about'),
    url(r'^reports$', reports, name='reports'),

    url(r'^add_laptop$', add_laptop, name='add_laptop'),
    url(r'^edit_laptop/(?P<pk>\d+)$', edit_laptop, name='edit_laptop'),
    url(r'^delete_laptop/(?P<pk>\d+)$', delete_laptop, name='delete_laptop'),
]