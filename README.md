# inventorify
> **Inventorify** is an inventory manager web application developed by **Shrish Mohapatra** using the **Django** framework. The main objective of application is to allow users to **manage laptop inventory**, view **reports** for various offices, and to take advantage of Django's **administrative backend**.

![alt text](https://github.com/theRealShrishM/inventorify/blob/master/img/inventorify_view_laptops.PNG "View Laptops")

## Running Project
You will first need to clone the repository to your local machine:
```
git clone https://github.com/theRealShrishM/inventorify.git
```

Then you will need to install the following via pip (ensure you have Python 3.7.X installed):
```
pip install django
pip install django-crispy-forms
```

After, you will need to navigate to the repository via command line/terminal:
```
cd inventorify-master
```

Here, you will run the server:

Windows: `python manage.py runserver`

Linux/Mac: `python3 manage.py runserver`

Go to your browser and type the following: **127.0.0.1:8000**

## Main Features
Key features of the web application include the ability to manage laptops, view reports, and use Django's admin backend.

### Manage
Users can add or edit laptop entries, specifying important information such as office location, username, model, service tag, status, potential issues, and more.

![alt text](https://github.com/theRealShrishM/inventorify/blob/master/img/inventorify_edit_laptops.PNG "Edit Laptops")

### Reports
Users can view "report cards" for various office locations regarding laptop status. One can view a breakdown of stored, repaired, and active devices.

![alt text](https://github.com/theRealShrishM/inventorify/blob/master/img/inventorify_reports.PNG "View Reports")

### Admin
Inventorify takes advantage of Django's admin backend. Admins can login to the' backend to view all database entries, create/edit account info, and more.

![alt text](https://github.com/theRealShrishM/inventorify/blob/master/img/inventorify_admin.PNG "Admin")

### About
Inventorify includes a detailed **About** page which explains how to use the application.

![alt text](https://github.com/theRealShrishM/inventorify/blob/master/img/inventorify_about.PNG "Admin")
