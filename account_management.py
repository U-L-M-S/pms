import json
import os
import password

class Account:

    @staticmethod
    def change_pw(new_pw, user_path):
        #get the whole user data to change just one item (password)
        with open(user_path, 'r') as f:
            data = json.load(f)
            data["password"] = new_pw

        with open(user_path, 'w') as f:
            json.dump(data, f)
            f.close()
        return True



    @staticmethod
    def login(username,pw):
        user_path_exists = os.path.exists('users/' + username + '.json')
        if user_path_exists == False:
            print("Account does not exist")
            return False
        else:
            #get the hashed pw from user json file
            users_path = os.getcwd() + '/users/' + username + '.json'
            with open(users_path, "r") as f:
                data_user = json.load(f)
                encrypted_pw = data_user.get('password')
            #compare the user input (hashed) with the hash that is saved in the json file
            object_compare_passwords = password.Password.pw_comparation(pw, encrypted_pw)
            if object_compare_passwords == False:
                print("username or password is wrong")
                return False
            #if the hashes are the same then check if the users_input fallows the criteria (even after a policies update)
            if object_compare_passwords == True:
                object_compare_userinput_with_policies = password.Password.check_password_criteria_L_and_CA(pw)
                if object_compare_userinput_with_policies == False:
                    print("Your password do not match with own new password policies\n")
                    show_user_policies = password.Password.getPolicies()
                    print("Minimal length: " + str(show_user_policies.get("pw_minimal_length")))
                    print("Use of uppercase: " + str(show_user_policies.get("pw_uppercase")))
                    print("Use of lowercase: " + str(show_user_policies.get("pw_lowercase")))
                    print("Use of digits:  " + str(show_user_policies.get("pw_digits")))
                    print("Use of symbols:  " + str(show_user_policies.get("pw_symbol")))
                    user_new_pw = input("Input a new password: ")

                    #hash new user pw
                    hashed_user_new_pw = password.Password.pw_encrypt(user_new_pw)
                    #change old pw to new one
                    Account.change_pw(hashed_user_new_pw,users_path)

                if object_compare_userinput_with_policies == True:
                    print(f"Welcome {username} !")
                    return True





    @staticmethod
    def save_userdata_in_json(userdata, path_user):
        j = json.dumps(userdata)
        with open(path_user, "w") as f: #, encoding='utf-8'
            f.write(j)
            f.close()


    @staticmethod
    def check_for_double_users(username):
        # check if there is another user with the same username (return True if another user is found)
        users_path = os.getcwd() + '/users/'
        for root, dirs, files in os.walk(users_path):
            if username in files:
                return True
            else:
                return False
    @staticmethod
    def create_account(username, pw):
        users_path = os.getcwd() + '/users/'  + username + '.json'
        if Account.check_for_double_users(username + '.json') == True:
            print("ERROR! The username is already used by other user! Try a new one")
            return False
        if Account.check_for_double_users(username) == False:
            # check the user pw with policies
            check_policies_for_login = password.Password.check_password_criteria_L_and_CA(pw)
            if check_policies_for_login == False:
                print("ERROR! pw does NOT match with own policies. Please try another one")
                return False
            if check_policies_for_login == True:
                # encrypt user PW
                hashed_user_pw = password.Password.pw_encrypt(pw)
                user_data = {'username': username, 'password': hashed_user_pw, 'admin': False}
                user_location_data = users_path
                Account.save_userdata_in_json(user_data, user_location_data)
                return True



