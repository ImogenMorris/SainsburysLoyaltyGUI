# Sainsburys loyalty programme window

import PySimpleGUI as sg

imageLayout = [[sg.Image('acting_artifical_logo.png', size =(100,100))]]

treeFrame = sg.Frame("Tree", imageLayout, title_color='green')

firstLayout = [[sg.Text('Month'),sg.Text('Customer name'),sg.Text('Points')],
               [treeFrame]]

sg.Window(title="Sainsburys Loyalty Rewards", layout = firstLayout, margins=(100, 50)).read()



top.mainloop()