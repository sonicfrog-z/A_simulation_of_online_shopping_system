import pickle
from item import Item
from cart import Cart


class ItemList:

    def __init__(self, uid):
        self.user_id = uid
        self.item_dic = {}  # {item_id1 : <item1>, item_id2 : <item2>}
        self.load()

    def show_menu(self):
        print("+-----------------------------+")
        print("| *********Item List********* |")
        print("| 1) Show items               |")
        print("| 2) Add item to cart         |")
        print("| q) Exit to home             |")
        print("+-----------------------------+")

    def show_items(self):
        print('========================================================================')
        for key in self.item_dic:
            print(self.item_dic[key])
        print('========================================================================')

    def add_to_cart(self):
        print('Enter item id and quantity')
        item_id = input('item id: ')
        if item_id in self.item_dic:
            quant = int(input('item quantity: '))
            cart_ = Cart(self.user_id)
            cart_.add_cart(item_id, quant)
            cart_.save()
            print('Item {} * {} successfully add to cart.'.format(item_id, quant))
        else:
            print('Item id you entered not exist')

    def load(self):
        try:
            with open(Item.FILENAME, 'rb') as fin:
                # self.title = pickle.load(fin)
                while True:
                    try:
                        self.item_dic = pickle.load(fin)
                    except EOFError:
                        break
        except FileNotFoundError:
            return None

    def save(self):
        with open(Item.FILENAME, 'wb') as fout:
            # pickle.dump(self.title, fout)
            # for key in self.item_dic:
            #     pickle.dump(self.item_dic[key], fout)
            pickle.dump(self.item_dic, fout)

    def add_item(self, id, name, price, description):
        self.item_dic[id] = Item(id, name, price, description)

    # def __str__(self):
    #     result = ''
    #     # result = '{}:\n'.format(self.title)
    #     for index, item in enumerate(self.item_lst, start=1):
    #         result += '{}. {}\n'.format(index, item)
    #     return result


if __name__ == '__main__':
    ilst = ItemList('1001')
    # ilst.add_item('101', 'Eggs', 200, 'Organic! Great value! Best quality!')
    # ilst.add_item('102', 'Pencil', 239, 'Pre-Sharpened with Eraser, Includes Bonus Sharpener, Yellow, 4-Pack.')
    # ilst.add_item('103', 'Eraser', 50, 'Durable and designed for long lasting use by both children and adults.')
    # ilst.add_item('104', 'T-shirt', 2500, 'Dry Fit Athletic Shirts for Men Short/Long Sleeve Workout Shirt.')
    # ilst.add_item('105', 'Toilet Paper', 1898, 'Soft Bath Tissue, Septic-Safe, 12 Big Rolls.')
    # ilst.add_item('106', 'Paper Towels', 3044, 'Bounty Quick-Size Paper Towels, 12 Count,Equal to 30 Regular Rolls.')
    # ilst.add_item('107', 'Coke', 2415, 'Coca-Cola Drink Cans, 12 Fl. Oz. (Pack Of 35).')
    # ilst.add_item('108', 'Wireless Mouse', 5495, 'Logitech MX Anywhere 2S Wireless Mouse – Hyper-Fast Scrolling.')
    # ilst.add_item('109', 'Keyboard', 9999, 'Logitech MX Keys Advanced Wireless Illuminated Keyboard - Graphite.')
    # ilst.add_item('110', 'Monitor', 15999, 'Dell P Series 24" Screen LED-Lit Monitor Black (P2419H).')
    # print(ilst)
    # ilst.show_items()
    # John's Notes:
    # 1. Drink a lot of water (health)
    # 2. ...
    # ilst.save()
    # print(ilst.item_dic)
    ilst.add_to_cart()
