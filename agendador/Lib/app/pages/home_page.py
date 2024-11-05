import os
import random
from typing import Literal
import flet as ft
from ..widgets.widgets import animate_button, button_Action
from .page_model import AbcPage

class Home(AbcPage):
    label: str
    
    def __init__(self):
        self.page = None
        # Escolhendo a frase aqui para não gerar outra ao modificar a resolução
        self.label = random.choice([
            "O que faremos hoje? Escolha uma das opções abaixo:",
            "Vamos começar! Selecione uma das operações disponíveis:", 
            "Pronto para agir? Escolha uma das opções e vamos lá!",
            "Qual será a sua escolha hoje? Selecione uma das operações:",
            "Vamos realizar algo incrível! Escolha uma das opções abaixo:"
            ])

    def __str__(self) -> Literal['/home']:
        return "/home"

    def set_page(self, page: ft.Page) -> None:
        # Trás a instancia da página principal para a classe
        self.page = page 

    def get_page(self) -> ft.View:
        # Carregando o botão de desligamento
        turn_off_button = button_Action(
            page_width=self.page.window.width,
            page_height=self.page.window.height,
            icon= "assets/icons/power-switch.png",
            text_value="Agendar desligamento",
            color="#A33131"
            )
        turn_off_button.on_click = lambda e: self.page.go("/schedule")
        turn_off_button.on_hover = lambda e: animate_button(e, turn_off_button)
        # Carregando botão de reinicialização
        restart_button = button_Action(
            page_width=self.page.window.width,
            page_height=self.page.window.height,
            icon= "assets/icons/restart.png",
            text_value="Agendar reinicialização",
            color="#C4803B"
            )
        restart_button.on_click = lambda e: print(True)
        restart_button.on_hover = lambda e: animate_button(e, restart_button)
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
                                        bgcolor= "#363636",
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                turn_off_button,
                                                # Adicionando divisor
                                                ft.Container(
                                                    width=0.21 * self.page.window.width
                                                    ),
                                                restart_button
                                                ],
                                            spacing=0
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