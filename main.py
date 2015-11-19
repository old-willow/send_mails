#!/usr/bin/env python

from kivy.app import App
#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.widget import Widget
#from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
#from kivy.uix.button import Button

import os


#class MainButtons(Button):
#    padding = ReferenceListProperty(None)

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Box(BoxLayout):
    #layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
    #btn_cancel = Button(text='Cancel')
    #btn_send = Button(text='Send')

    #layout.add_widget(btn_cancel)
    #layout.add_widget(btn_send)

    loadfile = ObjectProperty(None)
    file_path_label = ObjectProperty(None)
    #button_cancel = ObjectProperty(None)
    #button_send = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        print("hello I'm firing!")
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load attachement", content=content,
                            size_hint=(0.9, 0.9))

        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.file_path_label.text = stream.read()

        self.dismiss_popup()

    #def select(self, *args):
    #    """
    #    This will be called from kv file when user selects a file.
    #    """
    #    try:
    #        self.file_path_label.text = args[1][0]
    #    except:
    #        pass

    def exit(self):
        App.get_running_app().stop()


class SendEmailsApp(App):

    def build(self):
        #grid = Grid()
        return Box()


#class ScreenOne(Screen):
#    pass
#
#
#class ScreenTwo(Screen):
#    pass
#
#
#class ScreenThree(Screen):
#    pass
#
#
#class Manager(ScreenManager):
#    screen_one = ObjectProperty(None)
#    screen_two = ObjectProperty(None)
#    screen_three = ObjectProperty(None)


#class SendEmailsApp(App):
#
#    def build(self):
#        manager = Manager(transition=WipeTransition())
#        return manager

Factory.register('Box', cls=Box)
Factory.register('LoadDialog', cls=LoadDialog)

if __name__ == '__main__':
    SendEmailsApp().run()
