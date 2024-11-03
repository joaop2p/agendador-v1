from ..src.queue.queue_func import Queue
from .controlers.controler_pages import Controler
from pyautogui import size

class App(Controler, Queue):
    def __init__(self):
        super().__init__()
        
    def settings(self):
        self.page.title = "Teste"
        # Definindo on_change para ser executado quando a self.page.go for executado
        self.page.on_route_change = self.on_change 
        # Definindo resolução inicial como a resolução nativa do monitor
        x, y = size()
        self.page.window.height = y
        self.page.window.width = x
        # Limitando a resolução do APP
        self.page.window.min_height = 766
        self.page.window.min_width = 1024
        # Definindo Tema escuro independente do sistema
        self.page.theme_mode = "DARK"
        # Definindo novas fonts para o aplicativo
        self.page.fonts = {"Sansation": "Sansations/Sansation_Regular.ttf"}
        # Atualiza os widgets quando a página for redimensionada
        self.page.on_resized = self.update_widgets
        # Abrir o aplicativo com a tela maximizada
        self.page.window.maximized = True

    def run_queue(self, *works):
        for work in works:
            self.insert_work(work)
        self.execute()

    def run(self, e):
        # Repassando a instancia de page que vem de "ft.app"
        self.startPage(e)
        # Direcionando a página inicial sendo a home
        self.settings()
        # Iniciando fila de tarefas paralelas
        self.run_queue([self.page.update])
        self.page.go("/home")