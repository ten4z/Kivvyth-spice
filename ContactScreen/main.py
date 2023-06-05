import kivy
import sqlite3
import webbrowser
from plyer import tts
from kivymd.app import MDApp
from kivy.lang import Builder
from datetime import datetime
from kivymd.toast import toast
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsBase
from kivymd.theming import ThemeManager
from kivy.uix.behaviors import FocusBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.properties import ListProperty, NumericProperty, ObjectProperty, BooleanProperty
from kivmob import KivMob,TestIds,RewardedListenerInterface
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton, MDRectangleFlatButton

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image


from kivymd.uix.behaviors import CircularRippleBehavior


from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen
import webbrowser
import sqlite3

Builder.load_file("gui.kv")



class CircularRippleButton(CircularRippleBehavior, ButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.ripple_scale = 5
        super().__init__(**kwargs)

class Sc_Manager(MDScreenManager):
	pass

class Sc_Menu(MDScreen):	
	def __init__(self, **kwargs):
		super(Sc_Menu, self).__init__(**kwargs)
		self.current_app = MDApp.get_running_app()
		
class ContentNavigationDrawer(MDScrollView):
	
	nav_drawer = ObjectProperty()
           
class Sc_About(MDScreen):
	pass  

class Sc_Info(MDScreen):
	pass  

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