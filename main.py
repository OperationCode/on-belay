import kivy
kivy.require ('1.10.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


class OnBelay(App):
    pass      

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#89A894')
    OnBelay().run()