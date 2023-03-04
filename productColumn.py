import PySimpleGUI as sg

import productDatabase

productLayout = [
               [productDatabase.treeFrame, productDatabase.laptopFrame, productDatabase.beeFrame],
               [productDatabase.waterBottleFrame, productDatabase.wildflowerFrame, productDatabase.earbudsFrame],
               [productDatabase.teddyFrame, productDatabase.stickerFrame, productDatabase.voucher50Frame],
               [productDatabase.voucher100Frame, productDatabase.voucher200Frame]
               ]

columnLayout = [sg.Column(layout=productLayout, size=(3000,7000),scrollable=True,vertical_scroll_only=True,element_justification='center')]

sg.Window(title="Sainsburys Loyalty Rewards", layout=[columnLayout], margins=(100, 50)).read()