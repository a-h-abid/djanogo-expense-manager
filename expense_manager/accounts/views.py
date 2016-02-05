from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse 
from .models import Account, Transaction
from .repositories.account_repo import AccountRepo 

@login_required
def index(request):
    accounts = Account.objects.filter(user_id= request.user.id)
    context = {'accounts' : accounts}
    return render(request, 'accounts/accounts/list.html', context)

@login_required
def create(request):
    context = {
        'form_mode' : 'add',
        'post_url' : reverse('accounts:create')
    }
    #if request.POST :
        
    return render(request, 'accounts/accounts/form.html', context)
    
@login_required
def edit(request, account_id):
    account = Account.objects.get(id=account_id)
    context = {
        'account' : account,
        'form_mode' : 'edit',
        'post_url' : reverse('accounts:edit', args=[account_id])
    }
    return render(request, 'accounts/accounts/form.html', context)
    
@login_required
def detail(request, account_id):
    account = AccountRepo().get( id=account_id, user_id=request.user.id )
    context = {
        'account' : account,
        'starting_amount_format' : account.currency + ' ' + str(account.starting_amount),
        'balance_format' : account.currency + ' ' + str(account.balance),
    }
    return render(request, 'accounts/accounts/detail.html', context)
    
@login_required
def list_transaction(request, account_id):
    account = AccountRepo().get( id=account_id, user_id=request.user.id )
    transactions = Transaction.objects.filter(account_id=account.id)
    context = {
        'account' : account,
        'transactions' : account.transactions
    }
    return render(request, 'accounts/transactions/list.html', context)
    
@login_required
def add_transaction(request, account_id):
    account = AccountRepo().get( id=account_id, user_id=request.user.id )
    context = {
        'account' : account, 
        'form_mode' : 'add'
    }
    return render(request, 'accounts/transactions/form.html', context)

@login_required
def edit_transaction(request, account_id, transaction_id):
    account = AccountRepo().get( id=account_id, user_id=request.user.id )
    transaction = Transaction.objects.get(id=transaction_id)
    context = {
        'account' : account, 
        'transaction' : transaction, 
        'form_mode' : 'edit'
    }
    return render(request, 'accounts/transactions/form.html', context)


