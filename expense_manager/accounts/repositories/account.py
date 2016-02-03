from expense_manager import settings
from .sqlite3.account import Account as AccountDb_sqlite3

class Account:
    
    def __init__(self):
        self.default_db = settings.DATABASES['default']['ENGINE'].replace('django.db.backends.','')
        self.db_obj = AccountDb_sqlite3()
        
    def get(self, id):
        return self.db_obj.get(id) 
    