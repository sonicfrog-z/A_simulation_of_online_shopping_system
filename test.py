# with open('order_id_counter.txt', 'r+') as file:
#     # print(file.read())
#     id_counter = int(file.read().strip()) + 1
#     id_counter = str(id_counter)
#     file.seek(0)
#     file.write(id_counter)
# print(id_counter)

import os

for root, dirs, files in os.walk('./data/order/'):
    for name in files:
        print(os.path.join(root, name))
