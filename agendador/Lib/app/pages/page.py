from abc import ABC, abstractmethod
from flet import Page

class AbcPage(ABC):

    @abstractmethod
    def get_page(self) -> None:
        pass

    @abstractmethod
    def set_page(self, page: Page) -> None:
        pass