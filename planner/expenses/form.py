from django import forms
from .models import Expense


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'amount', 'description', 'date', 'category')