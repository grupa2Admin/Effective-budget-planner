from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils.timezone import now


class Income(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)  # DECIMAL
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    date = models.DateField(default=now)

    def __str__(self):
        return self.title
