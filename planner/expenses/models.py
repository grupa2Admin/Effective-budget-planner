from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Expense(models.Model):
    CATEGORIES = (
        ('H', 'Housing'),
        ('T', 'Transportation'),
        ('F', 'Food'),
        ('U', 'Utilities'),
        ('TR', 'Travel'),
        ('M', 'Medical & Healthcare'),
        ('S', 'Saving, Investing'),
        ('C', 'Clothes'),
        ('E', 'Entertainment'),
        ('MI', 'Miscellaneous'),
        ('FD', 'Food'),
        ('O', 'other')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=230, null=True, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(default=now)
    category = models.CharField(max_length=30, choices=CATEGORIES)

    def __str__(self):
        return self.title

    class Meta:
        ordering: ['-date']
