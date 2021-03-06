'''
This project is still under development, and is intended for SBNCHS (Sta. Barbara Nat. Comp. High School), Iloilo, PH. 
You'll be needing Kivy 1.8.0 to run this app.
Cheers! If you want to contribute, please feel free to contact the developer. Thanks!
markjoseph.solidarios@outlook.com
'''

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView


import os

class OpenFileDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveFileDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)	

class ReportCardForm(Widget):
	pass

class RecordView(Widget):
	pass

class StudBasicDetails(Widget):
	pass
	
class GradingReportScreen(Widget):
	pass

class FirstGradingWidget(Widget):
	pass

class SecondGradingWidget(Widget):
	pass


class ReportCardApp(App):

	def dismiss_popup(self):
		self._popup.dismiss()

	#for file validation
	def CheckFile():
		return True

	#yadd app settings here
	def build(self):

		self.title = 'High School Report Card System'

		return ReportCardForm()

	#handles the open button
	def OpenRecord(self):
		msm = self.root.ids.MainScreenManager
		wt = self.root.ids.WidgetTitle
		msm.current = 'studentlist'
		wt.text = '[font=data/fonts/OpenSans-Light.ttf]Dashboard[/font]'
		msm.transition = SlideTransition()			
		self.dismiss_popup()

	def SaveRecord(self):
		self.dismiss_popup()

	def UpdateRecord(self):
		pass

	def SwitchToStudList(self):
		msm = self.root.ids.MainScreenManager
		wt = self.root.ids.WidgetTitle							
		msm.current = 'studlist'
		wt.text = '[font=data/fonts/OpenSans-Light.ttf]Select a Student[/font]'
		msm.transition = SlideTransition()

	def SwitchToEditor(self):
		msm = self.root.ids.MainScreenManager
		wt = self.root.ids.WidgetTitle			
		msm.current = 'editor'
		wt.text = '[font=data/fonts/OpenSans-Light.ttf]Student Record Editor[/font]'
		msm.transition = SlideTransition()		

	#handles the dash
	def SwitchToDash(self):
		msm = self.root.ids.MainScreenManager
		wt = self.root.ids.WidgetTitle			
		msm.current = 'dashboard'
		wt.text = '[font=data/fonts/OpenSans-Light.ttf]Dashboard[/font]'
		msm.transition = SlideTransition()

	def ShowHelp(self):
		msm = self.root.ids.MainScreenManager
		wt = self.root.ids.WidgetTitle			
		msm.current = 'help'
		wt.text = '[font=data/fonts/OpenSans-Light.ttf]Help[/font]'
		msm.transition = SlideTransition()		

	def ShowOpenFileDialog(self):
		content = OpenFileDialog(load=self.OpenRecord, cancel=self.dismiss_popup)
		self._popup = Popup(title="Open a Record", content=content, size_hint=(0.8, 0.8), title_size='20sp')
		self._popup.open()

	def ShowSaveFileDialog(self):
		content = SaveFileDialog(save=self.SaveRecord, cancel=self.dismiss_popup)
		self._popup = Popup(title="Save as", content=content, size_hint=(0.8, 0.8), title_size='20sp')
		self._popup.open()

if __name__ == '__main__':
	ReportCardApp().run()