from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        return Builder.load_file('button.kv')

    def presser(self):
        self.root.ids.my_label.text = "You Pressed It!!"

MainApp().run()
