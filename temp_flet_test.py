import flet as ft
from flet import Page

def main(page: Page):
    fp = ft.FilePicker()
    page.overlay.append(fp)
    page.add(ft.Text('test'))

if __name__ == '__main__':
    ft.run(main)
