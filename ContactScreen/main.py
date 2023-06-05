import kivy
import webbrowser
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.image import Image
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.behaviors import CircularRippleBehavior

Builder.load_file("gui.kv")

class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.ripple_scale = 5
        super().__init__(**kwargs)

class Sc_Manager(MDScreenManager):
	pass

class Sc_Contact(MDScreen):	
	def __init__(self, **kwargs):
		super(Sc_Contact, self).__init__(**kwargs)
		self.current_app = MDApp.get_running_app()
		
class ContentNavigationDrawer(MDScrollView):	
	nav_drawer = ObjectProperty()
           

class ContentManager(MDScreen):
	pass

class ContactInfoApp(MDApp):
	MDApp.title = "My Contact Page"

	def open_link(self, link):
		webbrowser.open(link)

	def build(self):				
		self.cm = ContentManager()		
		return self.cm

if __name__ == "__main__":
	ContactInfoApp().run()