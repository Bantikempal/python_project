from abc import ABC, abstractmethod
from models.customers import Customers     

class Acustomers(ABC):
    @abstractmethod
    def create_customers(self, model: Customers) -> None:
        pass

    @abstractmethod
    def update_customers(self, cid: int, model: Customers) -> None:
        pass

    @abstractmethod
    def delete_customers(self, cid: int) -> None:
        pass

    @abstractmethod
    def get_customers(self, cid: int) -> Customers:
        pass

    @abstractmethod
    def get_all_customers(self) -> list[Customers]:
        pass
