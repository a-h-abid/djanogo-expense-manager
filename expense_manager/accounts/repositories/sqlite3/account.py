from django.db import connection

class Account:
    
    def get(self, id):
        cursor = connection.cursor()
        sql = "SELECT * FROM accounts_account WHERE id = %s"
    
        cursor.execute(sql, [id])
        columns = [col[0] for col in cursor.description]
        data = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
        
        return data[0]
