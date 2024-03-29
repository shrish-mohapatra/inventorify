# Generated by Django 2.2.4 on 2019-09-21 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office', models.CharField(choices=[('Ottawa', 'Ottawa'), ('Toronto', 'Toronto'), ('Montreal', 'Montreal'), ('Vancouver', 'Vancouver')], default='Ottawa', max_length=32)),
                ('dept', models.CharField(choices=[('Admin', 'Admin'), ('CS', 'Customer Service'), ('Developer', 'Developer'), ('Sales', 'Sales'), ('TS', 'Tech Support')], default='Admin', max_length=64, verbose_name='Department')),
                ('username', models.CharField(default='Administrator', max_length=64)),
                ('manufacturer', models.CharField(default='Apple', max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('service_tag', models.CharField(max_length=12, verbose_name='Service Tag')),
                ('issues', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('STORED', 'In Storage'), ('REPAIR', 'To be Repaired'), ('ACTIVE', 'In Use')], default='STORED', max_length=32)),
            ],
        ),
    ]
