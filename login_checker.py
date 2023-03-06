
import front_back_connector
def login_info_checker(submitted_username, submitted_password):

    for user_row in front_back_connector.table_to_list():
        user_user = user_row[2]
        user_pass = user_row[3]

        if (user_user == submitted_username) and (user_pass == submitted_password):
            return [user_row[1], user_row[8],'success']
        pass
  #  return sg.popup("Wrong Login Information, Aborting")