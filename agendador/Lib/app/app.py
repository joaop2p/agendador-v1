from .controlers.controler_pages import Controler


class App(Controler):
    def __init__(self):
        super().__init__()

    @property
    def settings(self):
        self.page.title = "Teste"
        self.page.on_route_change = self.on_change

    def run(self, e):
        self.startPage(e)
        self.settings
        self.page.go("/home")