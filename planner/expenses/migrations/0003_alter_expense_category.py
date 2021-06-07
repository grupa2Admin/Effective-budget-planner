# Generated by Django 3.2.3 on 2021-06-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_expense_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Housing', 'Housing'), ('Transport', 'Transport'), ('Food', 'Food'), ('Utilities', 'Utilities'), ('Travel', 'Travel'), ('Medical', 'Medical & Healthcare'), ('Savings', 'Saving, Investing'), ('Clothes', 'Clothes'), ('Entertainment', 'Entertainment'), ('Other', 'Other')], max_length=30),
        ),
    ]