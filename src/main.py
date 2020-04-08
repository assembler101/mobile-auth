import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

import sqlite3

class AuthDisplay(AnchorLayout):
    pass

class AuthApp(App):
    def build(self):
        authDisplay = AuthDisplay()

        return authDisplay

if __name__ == '__main__':
    AuthApp().run()
