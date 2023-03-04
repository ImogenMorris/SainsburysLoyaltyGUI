import PySimpleGUI as sg


# def isSubmitPressed(isPressed):
#     if isPressed:
#
#         return isPressed

user_login = "blank"
user_password = "blankest"
def user_login_window():
    layout = [
        [sg.Text('-----User Login Window-----', size=(30, 1), font='Any 15')],
        [sg.Text('Username'), sg.Input(size=(30, 1), key='login')],
        [sg.Text('Password'), sg.Input('', size=(30, 1), key='password')],
        [sg.Button('Submit', button_color=('white', 'springgreen4'), key= "submit")]
    ]

    window = sg.Window('User Login Window', layout,
                       auto_size_text=False,
                       default_element_size=(10, 1),
                       text_justification='r',
                       return_keyboard_events=True,
                       grab_anywhere=False)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'login':
            user_login = values['login']
            print(user_login)

        if event == 'password':
            user_password = values['password']


        if event == 'submit':
            inputted_username = values['login']
            inputted_password = values['password']
            return inputted_username, inputted_password

        pass



    window.close()



