"""
urls.py - Used for mapping site-wide url-links to various apps
Shrish Mohapatra
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls'))
]
