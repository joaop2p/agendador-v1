import flet as ft

def animate_button(event: ft.ControlEvent, button: ft.Container) -> None:
    if event.data == "true":
        button.scale = 1.05
    else:
        button.scale = None
    button.update()

def button_Action(page_width: int, page_height: int, icon: str, text_value: str, color: str) -> ft.Container:
    '''
    Retorna um container clicável
    
    #### Parâmetros:
        - #### page_width:
        Largura da janela principal
        - #### page_height:
        Altura da janela principal
        - #### icon:
        Diretório do ícone desejado
        - #### text_value:
        Mensagem a ser exibida no interior do botão
        - #### color:
        Valor da cor desejada em hexadecimal
        
    '''
    return ft.Container(
            width=0.23 * page_width,
            height= 0.13 * page_height,
            alignment= ft.alignment.center,
            bgcolor = color,
            animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE_IN),
            border_radius= ft.border_radius.all(19),
            shadow= ft.BoxShadow(
                spread_radius=0,
                blur_radius= 4,
                offset= ft.Offset(
                    x=0,
                    y=4
                    )
                ),
            content=ft.Column(
                alignment= ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Image(
                            src= icon,
                            width=40,
                            height=40,
                            color= ft.colors.WHITE,
                            ),
                        ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            value=text_value,
                            text_align=ft.TextAlign.CENTER,
                            style=ft.TextStyle(
                                size=0.013 * page_width,
                                font_family=r"assets\sansation\Sansation_Regular.ttf",
                                weight=ft.FontWeight.BOLD
                                )
                            )
                        )
                    ]
                ),
            )

def Hole_Container(height: int, width: int, color: str, content: ft.Control) -> ft.Container:
    return ft.Container(
                height=height,
                width=width,
                padding=ft.padding.all(5),
                shadow=ft.BoxShadow(
                    blur_radius=20,
                    spread_radius=5,
                    color= ft.colors.BLACK26,
                    blur_style=ft.ShadowBlurStyle.INNER,
                    ),
                content=ft.Container(
                    height=height-10,
                    width=width-10,
                    bgcolor=color,
                    shadow=ft.BoxShadow( 
                        blur_radius=5,
                        spread_radius=5,
                        color=color,
                        ),
                    content=content
                )
            )