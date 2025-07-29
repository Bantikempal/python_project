class Tracks:
    def __init__(self,Tracksid: int, Tracksname: str):
        self.Tracksid = Tracksid
        self.Tracksname = Tracksname

    def __repr__(self):
        return f"Tracks(Tracksid={self.Tracksid}, Tracksname='{self.Tracksname}')"
        