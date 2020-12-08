from model import User
from database import Database


class UserAccess:
    user_logged_in = False

    def ask_user_to_login_or_register(self):
        new_or_existing_user = input("Do you have an account(Y/N)? ")
        if new_or_existing_user.upper() != "Y" or "N":
            if new_or_existing_user.upper() == 'Y':
                print('-------User has an account-------')
                user_name = str(input("Please enter your username? "))
                user_password = str(input("Please enter your password? "))
                self.user_login(user_name, user_password)

            elif new_or_existing_user.upper() == 'N':
                print('New user')
                username = str(input("Please enter a username? "))
                user_name = str(input("Please enter your name? "))
                user_surname = str(input("Please enter your last name? "))
                user_password = str(input("Please enter your password? "))
                user_confirmed_password = str(input("Please enter your password? "))
                self.create_new_user(username, user_name, user_surname, user_password, user_confirmed_password)
        else:
            print("-------Please select between the two options-------")
            return self.ask_user_to_login_or_register()

    def user_login(self, username, password):
        user = User.from_mongo({'username': username})
        if user and password == user['password']:
            print('-------you entered the correct details-------')
            self.user_logged_in = True
            return user
        else:
            print('-------please check your credential-------')
            self.ask_user_to_login_or_register()

    def create_new_user(self, username, name, surname, password, confirmed_password):
        user = User.from_mongo({'username': username})
        if not user and password == confirmed_password:
            new_user = User(1, username, name, surname, password, confirmed_password)
            new_user.save_to_mongo()
            self.user_logged_in = True
            return user
        elif User.from_mongo({'username': username}):
            print('-------This username already exists if you have an account please login-------')
            self.ask_user_to_login_or_register()
        else:
            print('-------Please check the entered passwords-------')
            self.ask_user_to_login_or_register()


if __name__ == '__main__':
    Database.initialize()
    authenticate_user = UserAccess()
    current_logged_in_user = authenticate_user.ask_user_to_login_or_register()




