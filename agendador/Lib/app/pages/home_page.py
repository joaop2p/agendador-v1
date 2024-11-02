import flet as ft

from .page import AbcPage

class Home(AbcPage):
    def __init__(self):
        self.page = None

    def set_page(self, page: ft.Page) -> None:
        # Tras a instancia da página principal para a classe
        self.page = page 

    def get_page(self) -> ft.View:
        # Retorna a visualização de uma nova tela/
        return ft.View(
            route="/home",
            controls=[

                ]
            )