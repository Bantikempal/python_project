from abc import ABC, abstractmethod
from models.tracks import Tracks

class ATracks(ABC):
    @abstractmethod
    def create_tracks(self, model: Tracks) -> None:
        pass
    @abstractmethod
    def upadte_tracks(self, tid: int, model: Tracks) -> None:
        pass    
    @abstractmethod
    def delete_tracks(self, tid: int ) -> None:
        pass
    @abstractmethod
    def get_tracks(self, tid: int) -> Tracks:
        pass

    @abstractmethod
    def get_all_tracks(self) -> list[Tracks]:
        pass
    