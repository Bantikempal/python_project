from models.albums import Albums
from models.repos.a_albums import Aalbums
import sqlite3

class AlbumsRepo(Aalbums):
    def create_albums(self, model: Albums) -> None:
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO Albums (Title, ArtistId) VALUES (?, ?)', (model.title, model.artistid))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return None        


    def update_albums(self, aid: int, model: Albums) -> None:
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE Albums SET Title = ?, ArtistId = ? WHERE AlbumId = ?', (model.title, model.artistid, aid))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return None

    def delete_albums(self, aid: int) -> None:
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM Albums WHERE AlbumId = ?', (aid,))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return None

    def get_albums(self, aid: int) -> Albums:
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.execute('SELECT * FROM Albums WHERE AlbumId = ?', (aid,))
                row = cursor.fetchone()
                if row:
                    return Albums(albumid=row[0], title=row[1], artistid=row[2])
                else:
                    return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return None

    def get_all_albums(self) -> list[Albums]:
        data_list = []
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.execute('SELECT * FROM Albums')
                for row in cursor:
                    a = Albums(albumid=row[0], title=row[1], artistid=row[2])
                    data_list.append(a)
                    
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list