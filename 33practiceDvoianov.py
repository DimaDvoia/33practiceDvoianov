import kivy

kivy.require('1.0.7')
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class TestApp(App):

    def animate_button(self, instance):
        animation = Animation(pos=(100, 100), t='out_bounce', duration=3)
        animation += Animation(pos=(200, 100), t='out_bounce', duration=3)
        animation &= Animation(size=(500, 500), duration=3)
        animation += Animation(size=(100, 50), duration=3)
        animation.start(instance)

    def build(self):
        layout = BoxLayout(orientation='vertical')

        button1 = Button(text='Нажимай', on_press=self.animate_button)
        layout.add_widget(button1)

        button2 = Button(text='Анимация', on_press=self.animate_button)
        layout.add_widget(button2)

        return layout


if __name__ == '__main__':
    TestApp().run()