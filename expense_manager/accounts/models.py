from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    starting_amount = models.DecimalField(max_digits=10,decimal_places=2)
    currency = models.CharField(max_length=3)
    created_on = models.DateTimeField(auto_now_add=True)
    
class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('I','Income'),   
        ('E','Expense'),   
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


