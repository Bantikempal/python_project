class Artists:
    def __init__(self, artistid: int, Name: str):
        self.artistid = artistid
        self.Name = Name
    
    def __repr__(self):
        return f"Artists(artistid={self.artistid}, Name='{self.Name}')"