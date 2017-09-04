from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader



class TestApp(App):
    def build(self):
        ptsd_button = Button(text='PTSD')
        ptsd_button.bind(on_press=self.callback)
        return ptsd_button
    
    def callback(self, instance):
        sound = SoundLoader.load('resources/sound/ptsd.mp3')
        sound.play()
        
TestApp().run()