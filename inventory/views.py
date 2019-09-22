"""
views.py - Used to provide database information from GET & POST requests
Shrish Mohapatra
"""

from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop, ch_office, ch_status
from .forms import LaptopForm

# [Page View Methods] #
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def reports(request):
    return render(request, 'reports.html', {'reports': report_data()})

def view_laptops(request):
    laptops = Laptop.objects.all()

    context = {
        'header': 'laptops',
        'items': laptops,
        'count': laptops.count()
    }

    return render(request, 'index.html', context)

# [Laptop Methods] #
def add_laptop(request):
    if request.method == "POST":
        form = LaptopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/index')

    else:
        form = LaptopForm()
        return render(request, 'laptop_form.html', {'form': form, 'header': 'New Laptop'})

def edit_laptop(request, pk):
    item = get_object_or_404(Laptop, pk=pk)

    if request.method == "POST":
        form = LaptopForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
        form = LaptopForm(instance=item)
        return render(request, 'laptop_form.html', {'form': form, 'header': 'Edit Laptop', 'item': item})

def delete_laptop(request, pk):
    item = get_object_or_404(Laptop, pk=pk)
    item.delete()

    return redirect('/index')

# [Helper Methods] #
def report_data():
    data = []

    for office in ch_office:
        items = Laptop.objects.all().filter(office=office[0])
        count = items.count()

        storage = items.filter(status=ch_status[0][0]).count()
        repair = items.filter(status=ch_status[1][0]).count()
        active = items.filter(status=ch_status[2][0]).count()

        info = {
            'name': office[0],
            'count': count,
            'storage': storage,
            'repair': repair,
            'active': active
        }

        data.append(info)

    return data