from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen


class MainApp(MDApp):

    def build(self):
        screen = Screen()

        # Define Table
        table = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.9, 0.6),
            check=True,
            use_pagination=True,
            rows_num=3,
            pagination_menu_height='240dp',
            pagination_menu_pos="auto",
            column_data=[
                ('First Name', dp(30)),
                ('Last Name', dp(30)),
                ('Email Address', dp(30)),
                ('Phone Number', dp(30))
            ],
            row_data=[
                ("Airon", "Miranda", "airon@email.com", "(00) 0 0000-0000"),
                ("Davi", "Miranda", "davi@email.com", "(11) 1 1111-1111"),
                ("Liu", "Miranda", "liu@email.com", "(22) 2 2222-2222"),
                ("Airon", "Miranda", "airon@email.com", "(00) 0 0000-0000"),
                ("Davi", "Miranda", "davi@email.com", "(11) 1 1111-1111"),
                ("Liu", "Miranda", "liu@email.com", "(22) 2 2222-2222"),
                ("Airon", "Miranda", "airon@email.com", "(00) 0 0000-0000"),
                ("Davi", "Miranda", "davi@email.com", "(11) 1 1111-1111"),
                ("Liu", "Miranda", "liu@email.com", "(22) 2 2222-2222"),
                ("Airon", "Miranda", "airon@email.com", "(00) 0 0000-0000"),
                ("Davi", "Miranda", "davi@email.com", "(11) 1 1111-1111"),
                ("Liu", "Miranda", "liu@email.com", "(22) 2 2222-2222"),
                ("Airon", "Miranda", "airon@email.com", "(00) 0 0000-0000"),
                ("Davi", "Miranda", "davi@email.com", "(11) 1 1111-1111"),
                ("Liu", "Miranda", "liu@email.com", "(22) 2 2222-2222"),
                ("Airon", "Miranda", "airon@email.com", "(00) 0 0000-0000"),
                ("Davi", "Miranda", "davi@email.com", "(11) 1 1111-1111"),
                ("Liu", "Miranda", "liu@email.com", "(22) 2 2222-2222")
            ]

        )

        # bind the table
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_checked)

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        # return Builder.load_file('data-table.kv')

        # Add table widget to screen

        screen.add_widget(table)
        return screen

    # functions for check presses
    def checked(self, instance_table, current_row):
        print(instance_table, current_row)

    # functions for row presses
    def row_checked(self, instance_table, instance_row):
        print(instance_table, instance_row)


MainApp().run()
