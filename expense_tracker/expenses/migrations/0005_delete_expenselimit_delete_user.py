# Generated by Django 5.1.4 on 2024-12-27 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0004_user_expenselimit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExpenseLimit',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
