from datetime import datetime
from typing import Literal
from ...src.queue.queue_func import QUEUE_WORK as qw

from ..widgets.widgets import Hole_Container
from .page_model import AbcPage
import flet as ft

class Schedule(AbcPage):
    hour: ft.Text
    minute: ft.Text
    modify: bool
    
    def __init__(self):
        self.page = None
        self.hour = None
        self.minute = None
        self.modify = False

    def __str__(self) -> Literal['/schedule']:
        return "/schedule"

    def set_page(self, page: ft.Page) -> None:
        self.page = page

    def att_time(self) -> None:
        if not self.modify:
            self.hour.value = datetime.now().hour
            self.minute.value = datetime.now().minute

    def get_page(self) -> ft.View:
        # Inicializando os widgets
        self.hour = ft.Text(
            value= f"{datetime.now().hour}",
            text_align= ft.TextAlign.CENTER,
            style= ft.TextStyle(
                size= 0.1 * self.page.window.width,
                font_family= self.page.fonts["Sansation"]
            )
        )
        self.minute = ft.Text(
            value= f"{datetime.now().minute}",
            text_align= ft.TextAlign.CENTER,
            style= ft.TextStyle(
                size= 0.1 * self.page.window.width,
                font_family= self.page.fonts["Sansation"]
            )
        )
        # Adicionando a atualização de valores na fila de tarefas secundarias
        qw.insert_work(self.att_time)
        return ft.View(
            route=self,
            controls=[
                ft.Container(
                    bgcolor="#242424",
                    height=self.page.window.height,
                    width=self.page.window.width,
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content = ft.Container(
                                    width= 0.73 * self.page.window.width,
                                    height=0.09 * self.page.window.height,
                                    alignment=ft.alignment.center,
                                    bgcolor= "#8A8989",
                                    margin= ft.Margin(0, 0.03 * self.page.window.width, 0, 0),
                                    border_radius= ft.border_radius.all(19),
                                    content=ft.Text(
                                        value="Escolha um horário que funcione melhor pra você!",
                                        text_align=ft.TextAlign.CENTER,
                                        style=ft.TextStyle(
                                            size= 0.02 * self.page.window.width,
                                            weight=ft.FontWeight.BOLD,
                                            font_family= self.page.fonts["Sansation"],
                                            )
                                        )
                                    ),
                                ),
                            ft.Container(
                                height= 0.13 * self.page.window.height,
                                ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.Container(
                                    bgcolor="#303030",
                                    width=0.71 * self.page.window.width,
                                    height= 0.48 * self.page.window.height,
                                    alignment= ft.alignment.center,
                                    content=ft.Stack(
                                        alignment=ft.alignment.center,
                                        controls=[
                                            Hole_Container(
                                                width=0.37 * (self.page.window.width-30),
                                                height= 0.27 * (self.page.window.height-30),
                                                color= "#303030",
                                                content=ft.Row(
                                                    alignment= ft.MainAxisAlignment.CENTER,
                                                    spacing=0.03 * self.page.window.width,
                                                    controls=[
                                                        ft.Container(
                                                            width=0.15 * self.page.window.width,
                                                            height=0.23 * self.page.window.height,
                                                            alignment= ft.alignment.center,
                                                            content=self.hour
                                                            ),
                                                        ft.Container(
                                                            width=0.15 * self.page.window.width,
                                                            height=0.23 * self.page.window.height,
                                                            alignment= ft.alignment.center,
                                                            content=self.minute
                                                            ),
                                                        ]
                                                    )
                                                ),

                                            ft.Container(
                                                width=0.37 * self.page.window.width,
                                                height= 0.27 * self.page.window.height,
                                                # bgcolor=ft.colors.GREEN,
                                                # Sem o padding a largura do filho vai acabar sendo a mesma do pai, sendo assim a gente retira com o padding
                                                # O valor de 0.5 dos lados somados serão a largura do divisor
                                                padding=ft.Padding(((0.37 * self.page.window.width)-0.5)/2, 0,((0.37 * self.page.window.width)-0.5)/2,0),
                                                content=ft.Container(
                                                    width=10,
                                                    height=0.27 * self.page.window.height,
                                                    bgcolor=ft.colors.WHITE
                                                    )
                                                ),
                                            ]
                                        )
                                    )
                                )
                            ]
                        )
                    )
                ],
            padding=ft.padding.all(0)
            )