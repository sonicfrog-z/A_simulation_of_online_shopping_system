from home import Home
import os
import sys

sys.path.append('..')
from business_service.user_service import UserService


class UserEnd:
    def __init__(self):
        self.user_id = None

    def show_menu(self):
        print("+-----------------------------+")
        print("| **********Welcome********** |")
        print("| 1) Log in                   |")
        print("| 2) Register as new user     |")
        print("| q) Exit program             |")
        print("+-----------------------------+")

    def welcome(self):
        user_sv = UserService()
        print('Welcome to Yabin\'s online shopping program!')
        while True:
            self.show_menu()
            key = input('Enter your command: ')
            if key == 'q':
                print('Thanks for using Yabin\'s online shopping program, bye bye.')
                return
            elif key == '1':
                self.log_in(user_sv)
            elif key == '2':
                self.register(user_sv)

    def log_in(self, user_sv):
        uid = input('Input your user id (4 digits): ')
        pass_word = input('Input your pass word (only number): ')
        try:
            if user_sv.validate_user(uid, pass_word):
                self.user_id = uid
                print('*******************************')
                print('Welcome {} (user id: {}) !'.format(user_sv.user_info[uid].name, uid))
                print('*******************************')
                self.run_home()
        except Exception as e:
            print(e)
            print('Log in failed, please retry.')

    def register(self, user_sv):
        name = input('Input your name: ')
        address = input('Input your address: ')
        pass_word = input('Input your pass word (only 4 characters): ')
        try:
            uid = user_sv.create_user(name, address, pass_word)
            print('Congratulations! Your user id is {}, pass word is: {}. You can log in now.'.format(uid, pass_word))
        except Exception as e:
            print(e)

        # self.user_id = '1001'

    def run_home(self):
        hm_page = Home(self.user_id)
        while True:
            hm_page.show_menu()
            key = input('Enter your command: ')
            if key == 'q':
                print('Thanks for using Yabin\'s online shopping program, bye bye.')
                os._exit(0)
            elif key == '1':
                hm_page.run_item_list()
            elif key == '2':
                hm_page.run_cart()
            elif key == '3':
                hm_page.run_order_page()


if __name__ == '__main__':
    ue = UserEnd()
    ue.welcome()
