import os

import PySimpleGUI as sg
import text_synthesis as ts
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sg.theme('LightBrown5')
sg.set_options(font='Arial')
layout = [[sg.Text('Provide a query text to search for sounds')], 
          [sg.Input()], 
          [sg.OK()],
          [sg.Frame('', [[sg.Image("image.png",
                        size=(950, 400), key='image', enable_events=True )]])]]
            

window = sg.Window('Sounscape', layout, size=(700, 500))
graph = window.Element("image")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'OK':
        query = values[0]
        keyword, synonyms = ts.query(query)
        print('User query',values[0])
        break
        
    elif event == 'image':
        print(event, values)
        '''
        x,y = values['image']
        if x is None:
            print ("UP")
        else:
            print (f"DOWN {values['image']}")
    
    else:
        print(event, values)
        
        '''