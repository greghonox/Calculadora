import kivy

#metodo que converte hexadecimal
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
kivy.require("1.9.1")
#definido cor de fundo
Window.clearcolor = get_color_from_hex("#FFFFFF")
from kivy.app import App



class Calculadora(App):
    pass

Calculadora().run()

