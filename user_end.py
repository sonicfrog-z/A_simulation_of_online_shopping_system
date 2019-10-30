from home import Home


class UserEnd:
    def __init__(self):
        user_id = None

    def welcome(self):
        self.user_id = '1001'
        print('Welcome {}, enjoy your shopping!'.format(self.user_id))

    def run_home(self, ):
        hm_page = Home(self.user_id)
        while True:
            hm_page.show_menu()
            key = input('Enter your command: ')
            if key == 'q':
                return
            elif key == '1':
                hm_page.run_item_list()
            elif key == '2':
                hm_page.run_cart()
            elif key == '3':
                hm_page.run_order_page()
