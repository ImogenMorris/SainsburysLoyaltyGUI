# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Hello Anthony


import PySimpleGUI as sg

#[sg.Image(tree.png))]

firstLayout = [  [sg.Text('Month'),sg.Text('Customer name'),sg.Text('Points')],]

sg.Window(title="Sainsburys Loyalty Rewards", layout = firstLayout, margins=(100, 50)).read()


top.mainloop()