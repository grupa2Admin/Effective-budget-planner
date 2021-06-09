from django.db import models
from django.contrib.auth.models import User


class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateField()
    image = models.ImageField(upload_to="img/%y")
    type = 'receipt'

    def __str__(self):
        return self.title
