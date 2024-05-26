from typing import Union
import flet as ft
from views.Router import Router
# from State import global_state, State
import threading
import math

def Screen_lock(router_data: Union[Router, str, None] = None):
    # def animate(e):
    #     c.content = c2 if c.content == c1 else c1
    #     c.update()
    
    # El cambio en la funcion, lo que hara es re dirigir teniendo en cuenta la informacion guardada en el archivo.
    def change_page():
    
        with open("./views/data.csv", "r") as reader:
            for line in reader:    
                data = line.split(",")
                if data[0] == "0":
                    router_data.page.go("/register")
                else:
                    router_data.page.go("/")
    ## Cuando creemos el Home, tenemos que cambiar eso.
    
    timer = threading.Timer(2, change_page)
    
# Inicia el temporizador
    timer.start()

    
    container = ft.Container(
            content=ft.Text(
                "newTab",
                color="gray",
                size=30,
                weight="bold",
            ),
            alignment=ft.alignment.center,
            bgcolor="black",
            expand=True,
        )
    
    second_container = ft.Container(
        content=container,
        width=375,  
        height=812,
        bgcolor="black",
        alignment=ft.alignment.center,
    )

  
    router_data.page.title = "screen_lock"
    #router_data.page.vertical_alignment = ft.MainAxisAlignment.CENTER
    router_data.page.add(second_container)
    return second_container
