import PySimpleGUI as sg

def layoutF(title,image,environmental,points):
    title_string = (title+' '+str(points)+' points')
    buy_button = sg.Button('Buy',key=('-BUY_'+title_string+'-'))
    image_layout = [[sg.Image(image, size=(100, 100))],[buy_button]]
    color = 'purple'
    if environmental:
        color = 'green'
    else:
        color = 'purple'
    return sg.Frame(title_string, image_layout, background_color=color, title_color='white')


