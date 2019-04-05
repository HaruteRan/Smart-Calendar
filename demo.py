from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.image import Image
#from kivy.graphics import BorderImage
from kivy.graphics import Color, Rectangle
# from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput


class CalendarScreen(Screen):
    def create_block(self, sub, num, start, end):
        print_label = Label(text="{},{},{},{}".format(sub, num, start, end), font_size="20sp")
        self.add_widget(print_label)
    pass


class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        self.subject = TextInput(size_hint=(0.4, 0.06), pos_hint={'center_x': .6, 'center_y': .8},
                                 font_size=25, multiline=False)
        self.add_widget(self.subject)

        self.course_num = TextInput(size_hint=(0.4, 0.06), pos_hint={'center_x': .6, 'center_y': .7},
                                    font_size=25, multiline=False)
        self.add_widget(self.course_num)

        self.start_time = TextInput(size_hint=(0.4, 0.06), pos_hint={'center_x': .6, 'center_y': .6},
                                    font_size=25, multiline=False)
        self.add_widget(self.start_time)

        self.end_time = TextInput(size_hint=(0.4, 0.06), pos_hint={'center_x': .6, 'center_y': .5},
                                  font_size=25, multiline=False)
        self.add_widget(self.end_time)

    def send_data(self):
        num = self.course_num.text
        sub = self.subject.text
        start = self.start_time.text
        end = self.end_time.text
        self.manager.get_screen('calendar').create_block(sub, num, start, end)
    pass


class SearchScreen(Screen):
    pass


class UserScreen(Screen):
    pass


class RootScreen(ScreenManager):
    pass


class Demo(App):
    def build(self):
        return RootScreen()


if __name__ == "__main__":
    Demo().run()
