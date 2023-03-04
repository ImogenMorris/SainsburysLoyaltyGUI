# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Hello Anthony


import PySimpleGUI as sg
#[sg.Image(tree.png))]
#[sg.Image(—Pngtree—vector nature material cartoon trees_5563919.png))]
#attribution link requirement <a href='https://pngtree.com/so/Vector'>Vector png from pngtree.com/</a>

image = sg.Image('tree.png')

firstLayout = [  [sg.Text('Month'),sg.Text('Customer name'),sg.Text('Points')],
                 [sg.Image(size=(300, 300), key='-IMAGE-')]]

sg.Window(title="Sainsburys Loyalty Rewards", layout = firstLayout, margins=(100, 50)).read()

# update image in sg.Image
window['-IMAGE-'].update(data=image)


top.mainloop()