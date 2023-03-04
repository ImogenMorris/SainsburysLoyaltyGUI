import PySimpleGUI as sg

import productDatabase
#a test of the product column layout
productLayout = [
               [productDatabase.treeFrame, productDatabase.laptopFrame, productDatabase.beeFrame],
               [productDatabase.waterBottleFrame, productDatabase.wildflowerFrame, productDatabase.earbudsFrame],
               [productDatabase.teddyFrame, productDatabase.stickerFrame, productDatabase.voucher50Frame],
               [productDatabase.voucher100Frame, productDatabase.voucher200Frame]
               ]

columnLayout = [[sg.Column(layout=productLayout,scrollable=True,vertical_scroll_only=True,element_justification='left')]]

sg.Window(title="Sainsburys Loyalty Rewards", layout=columnLayout, size=(450,300)).read()