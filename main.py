from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel

from kivy.core.window import Window
Window.size = (360, 640)


class MyMDApp(MDApp):
    def build(self):

        return Builder.load_file("kvs\home.kv")

if __name__ == '__main__':
    MyMDApp().run()
