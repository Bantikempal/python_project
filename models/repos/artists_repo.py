from models.artists import Artists
from models.repos.a_artists import Aartists 
import sqlite3

class ArtistsRepo(Aartists):
    def create_artists(self, model: Artists) -> None:
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO Artists (Name,artistid) VALUES (?)', (model.Name, model.artistid))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return None

    def update_artists(self, aid: int, model: Artists) -> None:
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.cursor()  
                cursor.execute('UPDATE Artists SET Name = ? WHERE ArtistId = ?', (model.Name, aid))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return None

    def delete_artists(self, aid: int) -> None:
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM Artists WHERE ArtistId = ?', (aid,))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return None

    def get_artists(self, aid: int) -> Artists:
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.execute('SELECT * FROM Artists WHERE ArtistId = ?', (aid,))
                row = cursor.fetchone()
                if row:
                    return Artists(artistid=row[0], Name=row[1])
                else:
                    return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return None

    def get_all_artists(self):
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.execute('SELECT * FROM Artists')
                data_list = []
                for row in cursor:
                    a = Artists(artistid=row[0], Name=row[1])
                    data_list.append(a)

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list       
            