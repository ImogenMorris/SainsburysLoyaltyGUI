# Sainsburys loyalty programme window

import PySimpleGUI as psg

#attribution link requirement <a href='https://pngtree.com/so/Vector'>Vector png from pngtree.com/</a>

firstLayout = [[psg.Text('Month'),psg.Text('Customer name'),psg.Text('Points')],
               [psg.Image('acting_artifical_logo.png')]]

psg.Window(title="Sainsburys Loyalty Rewards", layout = firstLayout, margins=(100, 50)).read()


top.mainloop()