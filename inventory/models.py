"""
models.py - Used to define database tables.
Shrish Mohapatra
"""

from django.db import models

# [Dropdown Field Choices] #
# Status choices
ch_status = (
    ('STORED', 'In Storage'),
    ('REPAIR', 'To be Repaired'),
    ('ACTIVE', 'In Use')
)

# Department choices
ch_dept = (
    ('Admin', 'Admin'),
    ('CS', 'Customer Service'),
    ('Developer', 'Developer'),
    ('Sales', 'Sales'),
    ('TS', 'Tech Support')
)

# Office choices
ch_office = (
    ('Ottawa', 'Ottawa'),
    ('Toronto', 'Toronto'),
    ('Montreal', 'Montreal'),
    ('Vancouver', 'Vancouver')
)

# [Database Model Classes] #

class Laptop(models.Model):

    # Database Fields
    office = models.CharField(max_length=32, choices=ch_office, default="Ottawa")
    dept = models.CharField(verbose_name="Department", max_length=64, choices=ch_dept, default="Admin")
    username = models.CharField(max_length=64, default="Administrator")

    manufacturer = models.CharField(max_length=64, default="Apple")
    model = models.CharField(max_length=64)
    service_tag = models.CharField(verbose_name="Service Tag", max_length=12)

    issues = models.TextField(blank=True)
    status = models.CharField(max_length=32, choices=ch_status, default="STORED")

    def __str__(self):
        # How objects of this class will appear in the admin panel
        return "{0} {1} - {2}".format(self.manufacturer, self.model, self.username)
