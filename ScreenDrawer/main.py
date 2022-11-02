from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
Builder.load_file("gui.kv")
class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
class Sc_Manager(MDScreenManager):
    pass
class Sc_Info(MDScreen):
    pass
class Sc_Profile(MDScreen):
    pass
class Sc_About(MDScreen):
    pass
class ContentManager(MDScreen):
    pass
class ScDrawer(MDApp):
    dialog = None
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light" 
        self.cm = ContentManager()
        return self.cm
ScDrawer().run()