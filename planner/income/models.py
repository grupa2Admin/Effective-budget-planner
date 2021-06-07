from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Income(models.Model):
    amount = models.FloatField()  # DECIMAL
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title
