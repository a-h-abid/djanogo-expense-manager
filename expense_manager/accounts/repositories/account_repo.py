from django.shortcuts import get_object_or_404
from expense_manager import settings
from ..models import Account, Transaction

class AccountRepo:
    
    def get(self, **kwargs):
        account = get_object_or_404(Account, **kwargs)
        account.balance = account.starting_amount
        
        account.transactions = Transaction.objects.filter(account_id=account.id)
        
        for transaction in account.transactions :
            if transaction.type == "I" : 
                account.balance = account.balance + transaction.amount
                transaction.type_format = "Income"
            elif transaction.type == "E" :
                account.balance = account.balance - transaction.amount
                transaction.type_format = "Expense"
            
        return account 
    