import PySimpleGUI as sg
def layoutF(title,image,environmental,points):
    imageLayout = [[sg.Image(image, size=(100, 100))]]
    color = 'purple'
    if environmental:
        color = 'green'
    else:
        color = 'purple'
    return sg.Frame((title+' '+str(points)+' points'), imageLayout, background_color=color, title_color='white')
