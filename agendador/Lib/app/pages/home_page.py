import os
import random
from typing import Literal
import flet as ft

from ..widgets.widgets import animate_buttom, buttom_Action

from .page import AbcPage

class Home(AbcPage):
    page: ft.Page
    labels: list
    
    def __init__(self):
        self.page = None
        self.labels = [
            "O que faremos hoje? Escolha uma das opções abaixo",
            "Vamos começar! Selecione uma das operações disponíveis.", 
            "Pronto para agir? Escolha uma das opções e vamos lá!",
            "Qual será a sua escolha hoje? Selecione uma das operações.",
            "Vamos realizar algo incrível! Escolha uma das opções abaixo."
            ]
        # Escolhendo a frase aqui para não gerar outra ao modificar a resolução
        self.label = random.choice(self.labels)

    def __str__(self) -> Literal['/home']:
        return "/home"

    def set_page(self, page: ft.Page) -> None:
        # Trás a instancia da página principal para a classe
        self.page = page 

    def get_page(self) -> ft.View:
        turn_off_buttom = buttom_Action(self.page.window.width, self.page.window.height)
        turn_off_buttom.on_click = lambda e: animate_buttom(turn_off_buttom)
        # Retorna a visualização de uma nova tela
        return ft.View(
            route=self,
            controls=[
                ft.Container(
                    bgcolor="#242424",
                    height= self.page.window.height,
                    width= self.page.window.width,
                    alignment=ft.alignment.center,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.Container(
                                    height= 0.092 * self.page.window.height,
                                    width= 0.31 * self.page.window.width,
                                    bgcolor = "#474747",
                                    margin=ft.Margin(0, 0.03 * self.page.window.width, 0, 0.027 * self.page.window.width),
                                    border_radius=ft.border_radius.all(19),
                                    alignment= ft.alignment.center,
                                    shadow= ft.BoxShadow(
                                        spread_radius=0,
                                        blur_radius= 4,
                                        offset= ft.Offset(
                                            x=0,
                                            y=4
                                            )
                                        ),
                                    content=ft.Text(
                                        value = f"Olá, {os.getlogin().capitalize()}. Bom dia!",
                                        text_align=ft.TextAlign.CENTER,
                                        style=ft.TextStyle(
                                            size=int(0.025*self.page.window.height),
                                            font_family=self.page.fonts["Sansation"],
                                            weight=ft.FontWeight.BOLD,
                                            color= "#B3B3B3"
                                            )
                                        )
                                    ),
                                ),
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    content=ft.Container(
                                        height=0.092 * self.page.window.height,
                                        width= 0.7 * self.page.window.width,
                                        bgcolor = "#474747",
                                        alignment= ft.alignment.center,
                                        border_radius=ft.border_radius.all(19),
                                        margin=ft.Margin(0,0,0, 0.05 * self.page.window.height),
                                        shadow= ft.BoxShadow(
                                            spread_radius=0,
                                            blur_radius= 4,
                                            offset= ft.Offset(
                                                x=0,
                                                y=4
                                                )
                                            ),
                                        content=ft.Text(
                                            value=self.label,
                                            style=ft.TextStyle(
                                                size=int(0.025*self.page.window.height),
                                                font_family=self.page.fonts["Sansation"],
                                                weight=ft.FontWeight.BOLD,
                                                color= "#B3B3B3"
                                                )
                                            )
                                        )
                                    ),
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    content=ft.Container(
                                        width=0.87 * self.page.window.width,
                                        height= 0.31 * self.page.window.height,
                                        content=ft.Row(
                                            controls=[
                                                turn_off_buttom
                                                ]
                                            )
                                        )
                                    )
                            ]
                        )
                    )
                ],
            # Retirando o espaçamento interno da view
            padding=ft.padding.all(0),
            spacing=0
            )