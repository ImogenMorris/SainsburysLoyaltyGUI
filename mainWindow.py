import PySimpleGUI as sg

import productDatabase

def mainWindowAppear(customer_name, total_points):
    column = [sg.Column(layout=productDatabase.productLayout,scrollable=True,vertical_scroll_only=True,element_justification='left',background_color='white')]
    windowLayout = [[sg.Text('Month',background_color='orange'),sg.Text(customer_name, background_color='orange')
                   ,sg.Text(total_points, background_color='orange',key='-POINTS-')],
               column]
    return sg.Window(title="Sainsburys Loyalty Rewards", layout = windowLayout, size=(460,300),background_color='white').read()
