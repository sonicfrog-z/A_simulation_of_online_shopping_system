from item_list import ItemList
from cart import Cart
from order_page import OrderPage


class Home:
    def __init__(self, userid):
        self.user_id = userid

    def show_menu(self):
        print("+-----------------------------+")
        print("| *********Home Page********* |")
        print("| 1) Go to item list          |")
        print("| 2) Go to shopping cart      |")
        print("| 3) Go to order page         |")
        print("| q) Exit program             |")
        print("+-----------------------------+")

    def run_item_list(self):
        item_list = ItemList(self.user_id)
        while True:
            item_list.show_menu()
            key = input('Enter your command: ')
            if key == 'q':
                break
            elif key == '1':
                item_list.show_items()
            elif key == '2':
                item_list.add_to_cart()

    def run_cart(self):
        cart = Cart(self.user_id)
        while True:
            cart.show_menu()
            key = input('Enter your command: ')
            if key == 'q':
                break
            elif key == '1':
                cart.show_cart()
            elif key == '2':
                cart.place_order()

    def run_order_page(self):
        order_page = OrderPage(self.user_id)
        while True:
            order_page.show_menu()
            key = input('Enter your command: ')
            if key == 'q':
                break
            elif key == '1':
                order_page.show_order_info()
            elif key == '2':
                order_page.check_out()
