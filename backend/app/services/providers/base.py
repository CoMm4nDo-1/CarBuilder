from abc import ABC, abstractmethod

class BaseProvider(ABC):
    source_name: str
    @abstractmethod
    def fetch_products(self): ...
    @abstractmethod
    def normalize(self, raw_product): ...
