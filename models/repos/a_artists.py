from abc import ABC, abstractmethod
from models.artists import Artists

class Aartists(ABC):
    @abstractmethod
    def create_artists(self, model: Artists) -> None:
        pass

    @abstractmethod
    def update_artists(self, aid: int, model: Artists) -> None:
        pass

    @abstractmethod
    def delete_artists(self, aid: int) -> None:
        pass

    @abstractmethod
    def get_artists(self, aid: int) -> Artists:
        pass

    @abstractmethod
    def get_all_artists(self) -> list[Artists]:
        pass