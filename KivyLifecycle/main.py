from kivymd.app import MDApp 
from kivy.lang.builder import Builder 
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
import webbrowser

KV = """
MDBoxLayout:
	orientation: "vertical"
	margin: "5dp"
	padding: "5dp"
	spacing: "5dp"
	MDLabel:
		text: "Aplicação Reiniciar Fechar"
	MDLabel:
		text: "http://josielsoares.com"
	MDLabel:
		text: "Autor: Josiel Soares"
	MDRaisedButton:
		text: "Visitar Home Page"
		size_hint: 1, .1
		on_release: app.abrir_link()	
	MDRaisedButton:
		text: "Reiniciar"
		size_hint: 1, .1
		on_release: app.reiniciar()
	MDRaisedButton:
		text: "Fechar"
		size_hint: 1, .1
		on_release: app.sair()
"""

class helloKivy(MDApp):
	def __init__(self, **kwargs):
		super(helloKivy, self).__init__(**kwargs)
		self.current_app = MDApp.get_running_app()
		self.current_app.title = "Kivy Lifecycle"
	def abrir_link(self):
		webbrowser.open("http://josielsoares.com")
	def reiniciar(self):
		self.current_app.reset()

	def sair(self):
		self.current_app.stop()

	def reset(self, *largs):		
		Window.remove_widget(self.root)
		new_root = Builder.load_string(KV)
		Window.add_widget(new_root)
		self.root = new_root
	
	def build(self):	
		Window.size = (320, 460)	
		return Builder.load_string(KV)

if __name__ == "__main__":
	helloKivy().run()