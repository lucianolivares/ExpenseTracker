from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

Builder.load_string("""
<NavigationScreen>
    name: 'navigation_screen'

    NavigationLayout:
        id: nav_layout

        ScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: 'vertical'
    
                    MDToolbar:
                        id: tool_bar
                        title: "DashBoard"
                        elevation: 10
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
    
                    ScreenManager:
                        #Think about how many screen
                        id: screen_manager

        MDNavigationDrawer:
            id: nav_drawer
            
            MDBoxLayout:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"

                Image:
                    id: avatar
                    size_hint: (1,1)

                MDLabel:
                    text: "BudgetApp"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "An app to organize expenses and income"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]

                ScrollView:
                        
                    MDList:
                        # It is just an idea
                        OneLineIconListItem:
                            text: "Budget"
                        
                            IconLeftWidget:
                                icon: "cash-register"
                                                       
                        OneLineIconListItem:
                            text: "Expenses"
                            IconLeftWidget:
                                icon: "cash-minus"
                                
                        OneLineIconListItem:
                            text: "Income"
                            IconLeftWidget:
                                icon: "cash-plus"
""")

class NavigationScreen(MDScreen):
    pass