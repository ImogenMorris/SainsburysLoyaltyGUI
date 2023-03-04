import PySimpleGUI as sg

import productDatabase

def mainWindowAppear():
    productLayout = [
        [productDatabase.treeFrame, productDatabase.laptopFrame, productDatabase.beeFrame],
        [productDatabase.waterBottleFrame, productDatabase.wildflowerFrame, productDatabase.earbudsFrame],
        [productDatabase.teddyFrame, productDatabase.stickerFrame, productDatabase.voucher50Frame],
        [productDatabase.voucher100Frame, productDatabase.voucher200Frame]
    ]
    column = [sg.Column(layout=productLayout,scrollable=True,vertical_scroll_only=True,element_justification='left',background_color='white')]
    windowLayout = [[sg.Text('Month',background_color='orange'),sg.Text('Customer name',background_color='orange')
                   ,sg.Text('Points',background_color='orange')],
               column]
    return sg.Window(title="Sainsburys Loyalty Rewards", layout = windowLayout, size=(460,300),background_color='white').read()


