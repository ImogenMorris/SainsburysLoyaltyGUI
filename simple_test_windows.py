import PySimpleGUI as sg

import mainWindow
import productDatabase
import login_checker
"""
    Demo - 2 simultaneous windows using read_all_window

    Window 1 launches window 2
    BOTH remain active in parallel

    Both windows have buttons to launch popups.  The popups are "modal" and thus no other windows will be active

    Copyright 2020 PySimpleGUI.org
"""

def make_win1():
    layout = [[sg.Text('Welcome to Sainsburys Loyalty Rewards'), sg.Text('      ', key='-OUTPUT-')],
              [sg.Button('Login')]]
    return sg.Window('Window Title', layout, location=(800,600), finalize=True)


window1, window2 = make_win1(), None        # start off with 1 window open

while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'Login' and not window2:
        window2 = mainWindow.mainWindowAppear('name',222)
    if event in (productDatabase.key_list):
        print('bought ' + event)
window.close()