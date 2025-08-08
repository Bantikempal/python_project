class Tracks:
    def __init__(self,Tracksid: int, Tracksname: str,albumid: int, Mediatypeid: int, genreid: int):
        self.Tracksid = Tracksid
        self.Tracksname = Tracksname
        self.albumid = albumid
        self.Mediatypeid = Mediatypeid
        self.genreid = genreid

    def __repr__(self):
        return f"Tracks(Tracksid={self.Tracksid}, Tracksname='{self.Tracksname}', albumid={self.albumid}, Mediatypeid={self.Mediatypeid}, genreid={self.genreid})"
        