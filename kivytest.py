from kivy.app import App
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader


# Defines the test app class: inherits the App class "from kivy.app import App"
class TestApp(App):
    # When kivy class is created we have a function called build. In this function we define a single button called 'PTSD' 
    # assign a callback to the button (what it does when clicked). 
    def build(self):
        ptsd_button = Button(text='PTSD')
        ptsd_button.bind(on_press=self.callback)
        return ptsd_button
        
    # define the callback, we load a sound using our resources sound file, and plays it. 
    def callback(self, instance):
        sound = SoundLoader.load('resources/sound/ptsd.mp3')
        sound.play()
        
        
if __name__ == '__main__':        
    # call Instantiate TestApp class, then access the method 'run()' that is defined in the parent class 'App'
    TestApp().run()
    
    