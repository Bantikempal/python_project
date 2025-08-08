from models.customers import Customers
from models.repos.a_customers import Acustomers 
import sqlite3

class CustomersRepo(Acustomers):    

    def create_customers(self, model: Customers) -> None:
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO Customers (FirstName, LastName, Email) VALUES (?, ?, ?)', 
                               (model.FirstName, model.LastName, model.Email))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return None

    def update_customers(self, cid: int, model: Customers) -> None:
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.cursor()  
                cursor.execute('UPDATE Customers SET FirstName = ?, LastName = ?, Email = ? WHERE CustomerId = ?', 
                               (model.FirstName, model.LastName, model.Email, cid))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return None

    def delete_customers(self, cid: int) -> None:
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM Customers WHERE CustomerId = ?', (cid,))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return None

    def get_customers(self, cid: int) -> Customers:
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.execute('SELECT * FROM Customers WHERE CustomerId = ?', (cid,))
                row = cursor.fetchone()
                if row:
                    return Customers(CustomerId=row[0], FirstName=row[1], LastName=row[2], Email=row[3])
                else:
                    return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return None

    def get_all_customers(self):
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.execute('SELECT * FROM Customers')
                data_list = []
                for row in cursor:
                    c = Customers(CustomerId=row[0], FirstName=row[1], LastName=row[2], Email=row[3])
                    data_list.append(c)
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list