import kivy
kivy.require ('1.10.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.logger import Logger
from kivy.utils import get_color_from_hex


class OnBelay(App):
    pass

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#A4BAB7')
    #TODO TAKE THIS OUT!!!! (sets permanent window size!)
    Window.size = (320, 568)
    OnBelay().run()
