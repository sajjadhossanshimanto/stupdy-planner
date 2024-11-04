from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel

from kivy.core.window import Window
Window.size = (360, 640)


class MyMDApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        # Optionally set the primary color
        self.theme_cls.primary_palette = "BlueGray"
        
        return Builder.load_file("kvs\home.kv")

if __name__ == '__main__':
    MyMDApp().run()
