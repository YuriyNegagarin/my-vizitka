from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class VizitkaWidget(BoxLayout):
    pressed = False


    def on_greeting(self):
        if not self.pressed:
            self.ids.greeting_btn.text = 'Рад знакомству!'
            self.pressed = True
        else:
            self.ids.greeting_btn.text = 'Привет!'
            self.pressed = False

    pass


class VizitkaApp(App):
    def build(self):
        return VizitkaWidget()


VizitkaApp().run()