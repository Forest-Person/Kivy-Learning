import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder



class MyLayout(BoxLayout):
	b1 = ObjectProperty(None)
	b2 = ObjectProperty(None)
	l1 = ObjectProperty(None)
	l2 = ObjectProperty(None)
	boxy = ObjectProperty(None)
	
	def __init__(self,**kwargs):
		super(MyLayout,self).__init__(**kwargs)
	
	def addBtn(self):
		
		self.btn2 = Button()
		self.add_widget(self.btn2)
		
	def removeBtn(self):
		
		self.clear_widgets([self.btn2])
			
				
			
		
		


builder = Builder.load_string(
'''
#:import threading threading



MyLayout:
    
    id:boxy
    orientation:'vertical'

    b1:b1
    l1:l1
    b2:b2
    l2:l2
    
    Label:
        id:l1
        text_size: self.width, None
        size_hint: 1, 2
        text:''
    
    Button:
        id:b1
        text:'add button'
        on_release: threading.Thread(target=root.addBtn).start()
        
    Label:
        id:l2
        text_size: self.width, None
        size_hint: 1, 1
        text:''
        	
    Button:
    	id:b2
        text:'Press to remove button'
        on_release: threading.Thread(target=root.removeBtn).start()


''')

class MyApp(App):
    
        
    def build(self):
        return builder


if __name__ == '__main__':
    MyApp().run()