from django.shortcuts import render
from django.http import HttpResponse
from .models import Account, Transaction
from .repositories.account import Account as AccountRepo 

def index(request):
    accounts = Account.objects.filter(id=1)
    context = {'accounts': accounts}
    return render(request, 'accounts/accounts/list.html', context)
    
def create(request):
    context = {'form_mode' : 'add'}
    return render(request, 'accounts/accounts/form.html', context)
    
def edit(request, account_id):
    account = Account.objects.get(id=account_id)
    context = {
        'account': account,
        'form_mode' : 'edit'
    }
    return render(request, 'accounts/accounts/form.html', context)
    
def detail(request, account_id):
    account = Account.objects.get(id=account_id)
    #acc = AccountRepo()
    #account = acc.get(id=account_id)
    account.balance = 30000
    context = {
        'account': account,
        'balance_format' : account.currency + ' ' + str(account.balance)
    }
    return render(request, 'accounts/accounts/detail.html', context)
    
def list_transaction(request, account_id):
    account = Account.objects.get(id=account_id)
    transactions = Transaction.objects.filter(account_id=account.id)
    context = {
        'account': account,
        'transactions' : transactions
    }
    return render(request, 'accounts/transactions/list.html', context)
    
def add_transaction(request, account_id):
    account = Account.objects.get(id=account_id)
    context = {
        'account': account, 
        'form_mode' : 'add'
    }
    return render(request, 'accounts/transactions/form.html', context)

def edit_transaction(request, account_id, transaction_id):
    account = Account.objects.get(id=account_id)
    transaction = Transaction.objects.get(id=transaction_id)
    context = {
        'account': account, 
        'transaction' : transaction, 
        'form_mode' : 'edit'
    }
    return render(request, 'accounts/transactions/form.html', context)
