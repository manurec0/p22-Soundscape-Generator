import os

import PySimpleGUI as sg
import text_synthesis as ts
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""This file contains the basic version of the program's interface using PySimpleGUI library for python.
"""


def run():
    sg.theme('LightBrown5')
    sg.set_options(font='Arial')
    layout = [[sg.Text('Provide a sentence describing the soundscape you want to recreate: ')],
              [sg.Input()],
              [sg.OK()],
              [sg.Frame('', [[sg.Image("image.png",
                                       size=(950, 400), key='image', enable_events=True)]])]]

    window = sg.Window('Soundscape', layout, size=(700, 500))
    graph = window.Element("image")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'OK':
            query = values[0]
            return query

        elif event == 'image':
            print(event, values)

