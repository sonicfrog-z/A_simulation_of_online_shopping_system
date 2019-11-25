class User:
    def __init__(self, uid, name, address, pass_word = '1111'):
        self.uid = uid
        self.name = name
        self.address = address
        self.pass_word = pass_word

    def __str__(self):
        return 'User ID: {}\n' \
               'User Name: {}\n' \
               'Address: {}\n' \
               'Pass word: {}'\
                .format(self.uid,
                        self.name,
                        self.address,
                        self.pass_word)


if __name__ == '__main__':
    user = User('1111', 'yabin zhang', '1805 andersen rd')
    print(user)