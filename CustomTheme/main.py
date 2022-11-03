from kivy.properties import ObjectProperty, BooleanProperty
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.app import MDApp
import webbrowser
import sqlite3
Builder.load_file("gui.kv")
class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
class Sc_Manager(MDScreenManager):
    pass
class Sc_Theme(MDScreen):
    def __init__(self, **kwargs):
        super(Sc_Theme, self).__init__(**kwargs)  
        self.current_app = MDApp.get_running_app()      
        self.create_themes_table()
        self.apply_theme()     
    def set_theme(self, pl, color):
        sql_update = "UPDATE tb_themes SET  palette = ? WHERE id = ?;"
        self.current_app.cursor.execute(sql_update, (pl,'1'))
        self.current_app.connection.commit()
        self.current_app.theme_cls.primary_palette = pl 
        self.current_app.root.ids.bottombar.icon_color = color
    def apply_theme(self):
        sql_theme = "SELECT theme, palette  FROM tb_themes WHERE id = '1';"
        self.current_app.cursor.execute(sql_theme)
        data =  self.current_app.cursor.fetchall()
        if len(data)==0 or data==None:
            self.insert_theme()        
        else:
            for dt in data:
                theme = dt[0]
                palette = dt[1] 
            self.current_app.theme_cls.theme_style = theme
            self.current_app.theme_cls.primary_palette = palette   
    def on_pre_enter(self, *args):        
        sql_theme = "SELECT theme, palette FROM tb_themes WHERE id = '1';"
        self.current_app.cursor.execute(sql_theme)             
    def insert_theme(self):
        sql_default = "INSERT INTO tb_themes(id, theme, palette) VALUES ('1', 'Dark', 'Blue');"
        self.current_app.cursor.execute(sql_default)
        self.current_app.connection.commit()
    def create_themes_table(self):
        sql_table = """CREATE TABLE IF NOT EXISTS tb_themes(
        id integer PRIMARY KEY,
        theme text NOT NULL,
        palette text NOT NULL)"""
        self.current_app.connection.execute(sql_table)
        self.current_app.cursor.execute("SELECT * FROM tb_themes")
        data = self.current_app.cursor.fetchall()
        if len(data)==0 or data==None:
            self.insert_theme()    
    def ChangeLuminosity(self):  
        sql = "SELECT theme, palette FROM tb_themes WHERE id = '1';"
        self.current_app.cursor.execute(sql)
        result =  self.current_app.cursor.fetchone()        
        if result[0]== "Light":                        
            sql_update = """UPDATE tb_themes SET theme = 'Dark' WHERE id = 1;"""
            self.current_app.cursor.execute(sql_update)
            self.current_app.connection.commit() 
            self.current_app.theme_cls.theme_style = "Dark"
            self.current_app.theme_cls.primary_palette = result[1]            
        if result[0] == "Dark":                        
            sql_update = "UPDATE tb_themes SET  theme = 'Light'  WHERE id = '1';"
            self.current_app.cursor.execute(sql_update)
            self.current_app.connection.commit()     
            self.current_app.theme_cls.theme_style = "Light"
            self.current_app.theme_cls.primary_palette = result[1]            
class Sc_About(MDScreen):
    pass  
class Sc_Info(MDScreen):
    pass              
class ContentManager(MDScreen):
    pass
class CustomTheme(MDApp):
    MDApp.title = "My Custom Theme"
    light = BooleanProperty("")
    connection =  sqlite3.connect("data.db")
    cursor = connection.cursor()
    dialog = None
    def open_link(self):
        webbrowser.open("https://github.com/ten4z/Kivvyth-Spice")
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light" 
        light = True
        self.cm = ContentManager()
        return self.cm
CustomTheme().run()