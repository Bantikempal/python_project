from models.tracks import Tracks
from models.repos.a_tracks import ATracks
import sqlite3

class TracksRepo(ATracks):
    def create_tracks(self, model: Tracks) -> None:
        pass

    def upadte_tracks(self, tid: int, model: Tracks) -> None:
        pass    

    def delete_tracks(self, tid: int ) -> None:
        pass

    def get_tracks(self, tid: int) -> Tracks:
        pass

    def get_all_tracks(self) -> list[Tracks]:
        data_list = []
        try:
            with sqlite3.connect('chinook.db') as conn:
                cursor = conn.execute('SELECT * FROM Tracks')
                for row in cursor:
                    t =Tracks(Tracksid=row[0], Tracksname=row[1])
                    data_list.append(t)
                    
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return data_list   
        
        
