from abc import ABC, abstractmethod
from flet import Page, View

class AbcPage(ABC):
    page: Page

    @abstractmethod
    def get_page(self) -> View:
        pass

    @abstractmethod
    def set_page(self, page: Page)  -> None:
        pass