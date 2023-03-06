import PySimpleGUI as sg

import login_checker
import mainWindow


user_login = "blank"
user_password = "blankest"

def make_user_login_window():
    layout = [
        [sg.Text('-----User Login Window-----', size=(30, 1), font='Any 15')],
        [sg.Text('Username'), sg.Input(size=(30, 1), key='login')],
        [sg.Text('Password'), sg.Input('', size=(30, 1), key='password', password_char='*')],
        [sg.Button('Submit', button_color=('white', 'springgreen4'), key= "submit")]
    ]

    return sg.Window('User Login Window', layout,
                       auto_size_text=False,
                       default_element_size=(10, 1),
                       text_justification='r',
                       return_keyboard_events=True,
                       grab_anywhere=False,
                       modal=True)


#mainWindow.mainWindowAppear

window1, window2 = make_user_login_window(), None        # start off with 1 window open

while True:  # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
    if event == 'login':
        user_login = values['login']
        print(user_login)
    if event == 'password':
        user_password = values['password']
    if event == 'submit':
        inputted_username = values['login']
        inputted_password = values['password']
        login_check = login_checker.login_info_checker(inputted_username, inputted_password)
        login_result = login_check[3]
        login_customer = login_check[1]
        login_points = login_check[2]
        if login_result[3] == 'login_success' and not window2:
            window2 = mainWindow.mainWindowAppear(login_customer,login_points)
        if event in (productDatabase.key_list):
            print('bought ' + event)
        pass

window.close()
