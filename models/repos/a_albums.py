from abc import ABC, abstractmethod
from models.albums import Albums

class Aalbums(ABC):
    @abstractmethod
    def create_albums(self, model: Albums) -> None:
        pass

    @abstractmethod
    def update_albums(self, aid: int, model: Albums) -> None:
        pass

    @abstractmethod
    def delete_albums(self, aid: int) -> None:
        pass

    @abstractmethod
    def get_albums(self, aid: int) -> Albums:
        pass

    @abstractmethod
    def get_all_albums(self) -> list[Albums]:
        pass