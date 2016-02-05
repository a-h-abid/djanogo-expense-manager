from django.conf.urls import url

from . import views

app_name = 'accounts'
urlpatterns = [
    # List Accounts of Current Logged-in User
    url(r'^$', views.index, name='index'),
    
    # Create New Account
    url(r'^create/$', views.create, name='create'),
    
    # Show Account Detail
    url(r'^(?P<account_id>[0-9]+)/$', views.detail, name='detail'),
    
    # Edit Existing Account
    url(r'^(?P<account_id>[0-9]+)/edit/$', views.edit, name='edit'),
    
    # List Transactions
    url(r'^(?P<account_id>[0-9]+)/transaction/$', views.list_transaction, name='list_transaction'),
    
    # Add Transaction
    url(r'^(?P<account_id>[0-9]+)/transaction/add/$', views.add_transaction, name='add_transaction'),
    
    # Edit Transaction
    url(r'^(?P<account_id>[0-9]+)/transaction/(?P<transaction_id>[0-9]+)/edit/$', views.edit_transaction, name='edit_transaction'),
    
]