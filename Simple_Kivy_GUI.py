import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.lang import Builder
from kivy.logger import Logger
kivy.require('1.0.9')

class main(App):
     def setup (self):
           print "Access of setup successfull" # debug
           FULLSCREEN=0 
           x=200 # size Window X 
           y=300 # size Window Y 
           NameWindow="My application in kivy"
           TitleApp = 'Basic Application'
           icon = 'custom-kivy-icon.png'
           if FULLSCREEN!=0:
               print "Set up Fullscreen my application! "
               Config.set('graphics' , 'fullscreen' , 'auto')
           else:
               print "Setup window at \nX = ",x , "\nY = " ,y
               Config.set('graphics' , 'height' , x)
               Config.set('graphics' , 'height' , y)
           Config.write()
           
class RunIT(  ):
    main().setup()
    def RUN (self):
           print "This message it's wrote at run"
           KIVY="./style_page.kv"
           print ("Load my file ", KIVY)
           Builder.load_file(KIVY)  # load Kivy file

if __name__ =="__main__":
    RunIT().RUN()
