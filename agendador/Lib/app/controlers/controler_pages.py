from ..pages.home_page import Home
from flet import RouteChangeEvent, Page


class Controler():
    pages: dict
    
    def __init__(self):
        super().__init__()
        self.pages = {"/home": Home}
    
    def startPage(self, page_instance: Page):
        self.page = page_instance

    def run_page(self, instance: object):
        view = instance()
        view.set_page(self.page)
        self.page.views.append(view.get_page())

    def on_change(self, event: RouteChangeEvent) -> None:
        self.page.views.clear() # -> Retirar a View atual da lista para evitar sobreposição
        self.run_page(self.pages[event.route])
        
    
        