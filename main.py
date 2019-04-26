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
from course import *
from user import *


date_dic = dict()
date_dic['monday'] = 0.2
date_dic['tuesday'] = 0.3
date_dic['wednesday'] = 0.4
date_dic['thursday'] = 0.5
date_dic['friday'] = 0.6
date_dic['saturday'] = 0.7
date_dic['sunday'] = 0.8


u = 0
course_dict = dict()


class CalendarScreen(Screen):
    def create_block(self, sub, num, start, end, day):
        global date_dic
        course_info = str(sub) + ' ' + str(num)
        pos_y = 0.5 - 0.1 * ((float(start) + float(end))/2 - 12)
        pos_x = date_dic[day.lower()]
        block = Button(size_hint=(0.12, 0.09), pos_hint={'center_x': pos_x, 'center_y': pos_y}, text=course_info)
        self.add_widget(block)


class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        self.subject = TextInput(size_hint=(0.4, 0.08), pos_hint={'center_x': .6, 'center_y': .8},
                                 font_size=25, multiline=False)
        self.add_widget(self.subject)

        self.course_num = TextInput(size_hint=(0.4, 0.08), pos_hint={'center_x': .6, 'center_y': .7},
                                    font_size=25, multiline=False)
        self.add_widget(self.course_num)

        self.start_time = TextInput(size_hint=(0.4, 0.08), pos_hint={'center_x': .6, 'center_y': .6},
                                    font_size=25, multiline=False)
        self.add_widget(self.start_time)

        self.end_time = TextInput(size_hint=(0.4, 0.08), pos_hint={'center_x': .6, 'center_y': .5},
                                  font_size=25, multiline=False)
        self.add_widget(self.end_time)

        self.day = TextInput(size_hint=(0.4, 0.08), pos_hint={'center_x': .6, 'center_y': .4},
                             font_size=25, multiline=False)
        self.add_widget(self.day)

    def send_data(self):
        global course_dict
        global u
        num = self.course_num.text
        sub = self.subject.text
        start = self.start_time.text
        end = self.end_time.text
        day = self.day.text
        c = Course(num, sub)
        lab = "{} {}".format(sub, num)
        c.add_student(u)
        u.add_course(c)
        course_dict[lab] = c
        self.manager.get_screen('user').print_user_info(u)
        self.manager.get_screen('calendar').create_block(sub, num, start, end, day)


class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.search_box = TextInput(size_hint=(0.4, 0.08), pos_hint={'center_x': .5, 'center_y': .8},
                                    font_size=25, multiline=False)
        self.add_widget(self.search_box)
        self.course_id = Label(text='', font_size=30, pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.course_id)
        self.num_students = Label(text='', font_size=30, pos_hint={'center_x': .5, 'center_y': .4})
        self.add_widget(self.num_students)

    def course_search(self):
        global course_dict
        if self.search_box.text != '':
            c = course_dict[self.search_box.text]
            temp = c.get_name()
            self.course_id.text = temp
            self.num_students.text = 'There are {} students taking this class'.format(len(c.get_student()))


class UserScreen(Screen):
    def __init__(self, **kwargs):
        super(UserScreen, self).__init__(**kwargs)
        self.user_name = Label(text='', font_size=30, pos_hint={'center_x': .5, 'center_y': .8})
        self.user_id = Label(text='', font_size=30, pos_hint={'center_x': .5, 'center_y': .7})
        self.user_school = Label(text='', font_size=30, pos_hint={'center_x': .5, 'center_y': .6})
        self.user_courses = Label(text='', font_size=30, pos_hint={'center_x': .5, 'center_y': .5})
        self.add_widget(self.user_name)
        self.add_widget(self.user_id)
        self.add_widget(self.user_school)
        self.add_widget(self.user_courses)

    def print_user_info(self, user):
        self.user_name.text = user.get_name()
        self.user_id.text = user.get_id()
        self.user_school.text = user.get_school()
        self.user_courses.text = user.course_info()


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.user_name = TextInput(size_hint=(0.4, 0.08), pos_hint={'center_x': .5, 'center_y': .7},
                                   font_size=25, multiline=False)
        self.add_widget(self.user_name)
        self.user_id = TextInput(size_hint=(0.4, 0.08), pos_hint={'center_x': .5, 'center_y': .6},
                                 font_size=25, multiline=False)
        self.add_widget(self.user_id)

    def check_login(self):
        if self.user_name.text != '' and self.user_id.text != '':
            global u
            u = User(self.user_name.text, self.user_id.text)
            self.manager.get_screen('user').print_user_info(u)
            self.manager.current = 'user'


class RootScreen(ScreenManager):
    pass


class Demo(App):
    def build(self):
        return RootScreen()


if __name__ == "__main__":
    Demo().run()
