import PySimpleGUI as sg

import productDatabase

productLayout = [
               [productDatabase.treeFrame, productDatabase.laptopFrame, productDatabase.beeFrame],
               [productDatabase.waterBottleFrame, productDatabase.wildflowerFrame, productDatabase.earbudsFrame],
               [productDatabase.teddyFrame, productDatabase.stickerFrame, productDatabase.voucher50Frame],
               [productDatabase.voucher100Frame, productDatabase.voucher200Frame]
               ]
layout=[[sg.Column(productLayout,scrollable=True)]]
window = sg.Window('Column Example', layout, size=(500,300))

while True:
   event, values = window.read()
   if event in (sg.WIN_CLOSED, 'Exit'):
      break
   if event in (productDatabase.key_list):
       print('bought '+event)
window.close()