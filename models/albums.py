class Albums:
    def __init__(self, title: str, artistid: int, albumid: int = None):
        self.albumid = albumid
        self.title = title
        self.artistid = artistid

    def __repr__(self):
        return f"Albums(title='{self.title}', artistid={self.artistid}, albumid={self.albumid})"
