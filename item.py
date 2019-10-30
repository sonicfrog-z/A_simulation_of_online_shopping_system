class Item:
    FILENAME = 'item_data.dat'

    def __init__(self, id, name, price, description):
        self.id = id
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return '*{}(id: {})\nPrice: ${}\nDescription:\n{}\n'.format(self.name, self.id, self.price / 100,
                                                                   self.description)



if __name__ == '__main__':
    i1 = Item(101, 'Eggs', 200, 'Organic! Great value! Best quality!')
    i2 = Item(102, 'Pencil', 239, 'Pre-Sharpened with Eraser, Includes Bonus Sharpener, Yellow, 4-Pack.')
    i3 = Item(103, 'Eraser', 50, 'Durable and designed for long lasting use by both children and adults.')

    print(i1)
    print(i2)
    print(i3)
