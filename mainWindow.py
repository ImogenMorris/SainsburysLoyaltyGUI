import PySimpleGUI as sg

import productDatabase

def mainWindowAppear():
    firstLayout = [[sg.Text('Month',background_color='orange'),sg.Text('Customer name',background_color='orange')
                   ,sg.Text('Points',background_color='orange')],
               [productDatabase.treeFrame,productDatabase.laptopFrame,productDatabase.beeFrame],
               [productDatabase.waterBottleFrame,productDatabase.wildflowerFrame,productDatabase.earbudsFrame],
               [productDatabase.teddyFrame,productDatabase.stickerFrame,productDatabase.voucher50Frame],
               [productDatabase.voucher100Frame,productDatabase.voucher200Frame]
               ]
    return sg.Window(title="Sainsburys Loyalty Rewards", layout = firstLayout, margins=(100, 50)).read()


