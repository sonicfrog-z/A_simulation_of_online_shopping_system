from business_service.user import User
import os
import pickle


class UserService:
    FILENAME = os.path.join(os.path.dirname(__file__), '../data/user_data.dat')
    COUNTER_FILE = os.path.join(os.path.dirname(__file__), '../data/user_id_counter.txt')

    def __init__(self):
        self.user_info = {}
        self.load_user()

    def load_user(self):
        try:
            with open(self.FILENAME, 'rb') as fin:
                self.user_info = pickle.load(fin)
        except FileNotFoundError:
            return None

    def save_user(self):
        with open(self.FILENAME, 'wb') as fout:
            pickle.dump(self.user_info, fout)

    def create_user(self, name, address, pass_word):
        if len(pass_word) != 4:
            raise Exception('Pass word must be 4 characters.')
        with open(self.COUNTER_FILE, 'r+') as file:
            id_counter = int(file.read().strip()) + 1
            id_counter = str(id_counter)
            file.seek(0)
            file.write(id_counter)
        self.user_info[id_counter] = User(id_counter, name, address, pass_word)
        self.save_user()
        return id_counter

    def validate_user(self, uid, pass_word):
        if uid in self.user_info:
            if pass_word == self.user_info[uid].pass_word:
                return True
            raise Exception('Wrong pass word.')
        raise Exception('Can not find this user id.')

    def show_user(self):
        for uid in self.user_info:
            print(self.user_info[uid])


if __name__ == '__main__':
    us = UserService()
    us.show_user()
