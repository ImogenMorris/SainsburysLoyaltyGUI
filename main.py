# Sainsburys loyalty programme window

import PySimpleGUI as sg

treeLayout = [[sg.Image('acting_artifical_logo.png', size =(100,100))]]

treeFrame = sg.Frame("Tree", treeLayout, title_color='green')

laptopLayout = [[sg.Image('acting_artifical_logo.png', size =(100,100))]]

laptopFrame = sg.Frame("Laptop", laptopLayout, title_color='purple')

beeLayout = [[sg.Image('acting_artifical_logo.png', size =(100,100))]]

beeFrame = sg.Frame("Bee", beeLayout, title_color='green')

waterBottleLayout = [[sg.Image('acting_artifical_logo.png', size =(100,100))]]

waterBottleFrame = sg.Frame("Water Bottle", waterBottleLayout, title_color='purple')

firstLayout = [[sg.Text('Month',background_color='orange'),sg.Text('Customer name',background_color='orange')
                   ,sg.Text('Points',background_color='orange')],
               [treeFrame,laptopFrame],
               [beeFrame,waterBottleFrame]]

sg.Window(title="Sainsburys Loyalty Rewards", layout = firstLayout, margins=(100, 50)).read()



top.mainloop()