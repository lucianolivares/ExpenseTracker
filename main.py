from kivymd.app import MDApp
from navigation_screen import NavigationScreen

class BudgetApp(MDApp):
    def build(self):
        nav_screen = NavigationScreen()
        return nav_screen

BudgetApp().run()