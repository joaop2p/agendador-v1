import flet as ft
from Lib.app.app import App


class Main:
    app: App
    
    def __init__(self):
        self.app = App()

    def run_app(self) -> None:
        """ 
        Inicia a parte gráfica do programa
        """
        ft.app(self.app.run)
        
if __name__ == "__main__":
    main = Main()
    main.run_app()
