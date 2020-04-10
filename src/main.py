import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

import sqlite3
import regex
from argon2 import PasswordHasher

# escapes all single quotes to prevent SQL injections. (sqlite)
# assumes that strings are wrapped around in single quotes
def escapeSingleQuotes(string):
    escape_re = regex.compile(r'(?=\')')

    return regex.sub(escape_re, r'\'', string)

class UserSignUp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()

    def user_sign_up(self, username, password):
        table_name = 'users'
        ph = PasswordHasher()

        # prevent SQL injection
        username = escapeSingleQuotes(username)

        hashed_password = ph.hash(password)

        query = '''
            INSERT INTO %s(username, password)
            VALUES('%s', '%s')
        ''' % (table_name, username, hashed_password)

        # save the user credentials
        self.cursor.execute(query)

        self.conn.commit()

class UserLogin(GridLayout):
    pass

class Auth(AnchorLayout):
    pass

class AuthApp(App):
    def build(self):
        auth = Auth()

        return auth

if __name__ == '__main__':
    AuthApp().run()
