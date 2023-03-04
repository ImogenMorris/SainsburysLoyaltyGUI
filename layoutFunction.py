import PySimpleGUI as sg
def layoutF(title,image,environmental):
    imageLayout = [[sg.Image(image, size=(100, 100))]]
    color = 'purple'
    if environmental:
        color = 'green'
    else:
        color = 'purple'
    return sg.Frame(title, imageLayout, title_color=color)