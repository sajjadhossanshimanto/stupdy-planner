from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.label import MDLabel

from kivy.core.window import Window
Window.size = (360, 640)


class MyMDApp(MDApp):
    def build(self):
        screen = Screen()
        
        # Bottom navigation widget
        bottom_nav = MDBottomNavigation()
        
        # Home tab
        home_tab = MDBottomNavigationItem(name='home', text='Home', icon='home')
        home_tab.add_widget(MDLabel(text="Home Screen", halign="center"))
        
        # Settings tab
        settings_tab = MDBottomNavigationItem(name='settings', text='Settings', icon='cog')
        settings_tab.add_widget(MDLabel(text="Settings Screen", halign="center"))
        
        # Profile tab
        profile_tab = MDBottomNavigationItem(name='profile', text='Profile', icon='account')
        profile_tab.add_widget(MDLabel(text="Profile Screen", halign="center"))
        
        # Add tabs to bottom navigation
        bottom_nav.add_widget(home_tab)
        bottom_nav.add_widget(settings_tab)
        bottom_nav.add_widget(profile_tab)
        
        # Add bottom navigation to screen
        screen.add_widget(bottom_nav)
        
        return screen

if __name__ == '__main__':
    MyMDApp().run()
