@@ -0,0 +1,50 @@
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
           #inizializzazione
           '''____________________________________________
          |     GestioneFinestra - Manage Window!      |
          |                                                                    |
          |                      SETUP SCREEN                       |
          |                                                                    |              
          |     1 -> FULLSCREEN  Schermo intero         |
          |     0 -> Window         Finestra                    |
          |                                                                   |
          |____________________________________________|
           '''
           print "test eseguito"
           tuttoschermo=0 
           x=200 # Grandezza schermo x ( size Window x )
           y=300 # Grandezza schermo y ( size Window Y )
           nomefinestra="Mia applicazione kivy"
           title = 'Basic Application'
           icon = 'custom-kivy-icon.png'
           if tuttoschermo!=0:
               print "imposto a tutto schermo!"
               Config.set('graphics' , 'fullscreen' , 'auto')
           else:
               print "imposto a finestra con grandezza \nX = ",x , "\nY = " ,y
               Config.set('graphics' , 'height' , x)
               Config.set('graphics' , 'height' , y)
           Config.write()
           
class RunIT(  ):
    main().setup()
    def avvio (self):
           print "ciao sono dentro il main"
           KIVY="./stile_pagina.kv"
           print ("carico il file ", KIVY)
           Builder.load_file(KIVY)  # Carica il file Kivy
           pass

if __name__ =="__main__":
    RunIT().avvio()
