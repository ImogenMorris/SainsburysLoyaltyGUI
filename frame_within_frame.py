import PySimpleGUI as sg

import blank_framer

def blank_frame():
    return sg.Frame("", [[]], pad=(5, 3), expand_x=True, expand_y=True, background_color='#404040', border_width=0)

def button_frame():
    return sg.Frame("", [[]], pad=(5, 3), expand_x=True, expand_y=True, background_color='#404040', border_width=0)



def layoutF(title,image,environmental,points):
    imageLayout = [[sg.Image(image, size=(100, 100))]]
    color = 'purple'
    if environmental:
        color = 'green'
    else:
        color = 'purple'

    return frame_to_return(sg.Frame((title+' '+str(points)+' points'), imageLayout, background_color=color, title_color='white'))

def frame_creator():
    sg.theme('DarkGrey4')

    layout_frame1 = [
        [blank_frame()],
        [sg.Frame("Frame 3", [[blank_frame()]], pad=(5, 3), expand_x=True, expand_y=True, title_location=sg.TITLE_LOCATION_TOP)],
    ]

    layout_frame2 = [[blank_frame()]]

    layout = [
        [sg.Frame("Frame 1", layout_frame1, size=(280, 250)),
        ], ]

    return layout

def frame_to_return(top_frame):
    layout_frame1 = [
        [blank_frame(), blank_frame()],
        [sg.Frame("Offer", [[top_frame]], pad=(5, 3), expand_x=True, expand_y=True,
                  title_location=sg.TITLE_LOCATION_TOP)],
    ]

    layout_frame2 = [[blank_frame()]]

    layout = [
        [sg.Frame("Frame 1", layout_frame1, size=(280, 250)),
         ], ]


    layout_frame1 = [
        [top_frame],
        [frame_creator()]]

    return layout