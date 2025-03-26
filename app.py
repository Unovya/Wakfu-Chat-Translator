import flet as ft
from flet_core import ScrollMode, FontWeight
from wakfuChatTranslate import watchChat




def app(page: ft.Page):
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


   topRow = ft.Row(
       [
           ft.Text('Wakfu Auto-Translator', size=18, weight=FontWeight.BOLD)


       ],
       alignment = ft.MainAxisAlignment.CENTER
   )




   card = ft.Card(
           content=ft.Column(
               [


               ],
               auto_scroll=True, scroll=ScrollMode.ALWAYS, height=page.height - 50
           )
   )
   page.add(topRow,card)


   while True:
       pageUpdate(page=page, card=card, cContent=watchChat())


def pageUpdate(page, card, cContent):
       card.content.controls.append(ft.ListTile(title=ft.Text(f'{cContent}')))
       page.update()




ft.app(app)
