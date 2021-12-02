from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"

        # Create Database or connect to one
        conn = sqlite3.connect('first-db.db')

        # create a cursor
        c = conn.cursor()

        # create a table

        c.execute("""CREATE TABLE if not exists costumers(
            name text)        
        """)

        # commit the changes
        conn.commit()

        # close or conection
        conn.close()

        return Builder.load_file('first-db.kv')

    def submit(self):
        # Create Database or connect to one
        conn = sqlite3.connect('first-db.db')

        # create a cursor
        c = conn.cursor()

        # Add a record
        c.execute("INSERT INTO costumers VALUES (:first)",
                  {
                      'first': self.root.ids.word_input.text,
                  })

        # Add a little message

        self.root.ids.word_label.text = f"{self.root.ids.word_input.text} Added"

        # clear the imput box
        self.root.ids.word_input.text = ''

        # commit the changes
        conn.commit()

        # close or conection
        conn.close()

    def show_records(self):
        # Create Database or connect to one
        conn = sqlite3.connect('first-db.db')

        # create a cursor
        c = conn.cursor()

        # Grab records from database

        c.execute("SELECT * FROM costumers")
        records = c.fetchall()

        word = ''
        # loop thru records
        for record in records:
            word = f"{word}\n{record[0]}"
            self.root.ids.word_label.text = f'{word}'

        # commit the changes
        conn.commit()

        # close or conection
        conn.close()


MainApp().run()
