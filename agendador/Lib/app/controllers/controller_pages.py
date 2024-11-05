from ..pages.schedule_page import Schedule
from ..pages.home_page import Home
from flet import RouteChangeEvent, Page


class Controller():
    pages: dict
    actual_page: object
    
    def __init__(self):
        super().__init__()
        self.pages = {
            "/home": Home,
            "/schedule": Schedule
            }
        self.actual_page = None
    
    def startPage(self, page_instance: Page):
        self.page = page_instance

    def update_widgets(self, event):
        # Recarrega a view existente para traze-la com os novos valores de tamanho
        # Sim, foi a melhor alternativa que encontrei para isso. Eu: 1 x IA: 0
        self.page.views.clear()
        self.page.views.append(self.actual_page.get_page())
        self.page.update()

    def run_page(self, instance: object):
        self.actual_page = instance()
        self.actual_page.set_page(self.page)
        self.page.views.append(self.actual_page.get_page())

    def on_change(self, event: RouteChangeEvent) -> None:
        self.page.views.clear() # -> Retirar a View atual da lista para evitar sobreposição
        self.run_page(self.pages[event.route])
        self.page.update()
        
    
        