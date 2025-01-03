# Generated by Django 5.1.4 on 2025-01-02 16:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0007_alter_expense_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlylimit',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='monthlylimit',
            name='limit',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]