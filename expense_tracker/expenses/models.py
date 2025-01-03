# models.py
from django.db import models
from django.contrib.auth.models import User

# models.py
from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link each expense to a user
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)  # Add description field
    date = models.DateField()

    def _str_(self):
        return f"{self.category} - {self.amount} on {self.date}"

class MonthlyLimit(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One limit per user
    limit = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"Monthly limit for {self.user.username} - ${self.limit}"