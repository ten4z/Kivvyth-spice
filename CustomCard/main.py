from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivymd.app import MDApp
import webbrowser
Builder.load_file("gui.kv")
class Sc_Manager(MDScreenManager):
    pass
class ImagePopup(Popup):
    image = StringProperty("")
    def __init__(self, obj, img,  **kwargs):
        super(ImagePopup, self).__init__(**kwargs)
        self.image = "images/" + img + ".jpg"
class Sc_Image(MDScreen):
    image = StringProperty("")
    def show_popup(self, img):
        self.image = str(img)
        pop_img = ImagePopup(self, img)
        pop_img.open()
    def open_link(self, link):
        webbrowser.open(link)
class ContentManager(MDScreen):
    pass
class CustomCardApp(MDApp):
    dialog = None
    MDApp.title = "Custom Card by Ten4z"
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light" 
        self.sm = Sc_Manager()
        return self.sm
if __name__ == '__main__':
    CustomCardApp().run()