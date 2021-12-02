from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivymd.app import MDApp

Builder.load_file('testing.kv')


class MyLayout(Widget):
    pass


class AwesomeApp(MDApp):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
