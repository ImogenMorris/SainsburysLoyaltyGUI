# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import PySimpleGUI as pg

#set theme
pg.theme("DarkAmber")

#layout setup
layout = [
    [pg.Text("Enter Name")], [pg.InputText()], pg.Button("Cancel")

]

#create window
window = pg.Window("Form", layout)

while True:
    print(window.read())
    break
#

