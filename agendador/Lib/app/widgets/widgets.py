import flet as ft

def animate_buttom(buttom: ft.Container):
    buttom.animate = ft.animation.Animation(300, ft.AnimationCurve.BOUNCE_OUT)
    buttom.height = buttom.height-5
    buttom.width = buttom.width-5
    print("oi")

def buttom_Action(page_width: int, page_height: int) -> ft.Container:
    return ft.Container(
            width=0.23 * page_width,
            height= 0.13 * page_height,
            bgcolor = "#C73C3C",
            margin=ft.Margin(0.09 * page_width,0,0,0),
            border_radius= ft.border_radius.all(19),
            shadow= ft.BoxShadow(
                spread_radius=0,
                blur_radius= 4,
                offset= ft.Offset(
                    x=0,
                    y=4
                    )
                ),
            )
        