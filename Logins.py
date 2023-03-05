import PySimpleGUI as sg

import front_back_connector
import mainWindow

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
        [sg.Text('Password'), sg.Input('', size=(30, 1), key='password', password_char='*')],
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

            return login_info_checker(inputted_username, inputted_password)

        pass

    window.close()


def login_info_checker(submitted_username, submitted_password):

    for user_row in front_back_connector.table_to_list():
        user_user = user_row[2]
        user_pass = user_row[3]

        if (user_user == submitted_username) and (user_pass == submitted_password):
            print('if statement triggered')
            return mainWindow.mainWindowAppear(user_row[1], user_row[8])

    return sg.popup("Wrong Login Information, Aborting")










