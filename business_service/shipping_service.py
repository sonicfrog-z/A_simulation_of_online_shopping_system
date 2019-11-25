from business_service.shipment import Shipment
from business_service.order_service import OrderService
from business_service.inventory_service import InventoryService
import os
import pickle
from datetime import datetime


class ShippingService:
    FILENAME = os.path.join(os.path.dirname(__file__), '../data/shipping_data.dat')
    COUNTER_FILE = os.path.join(os.path.dirname(__file__), '../data/shipment_id_counter.txt')

    def __init__(self):
        self.shipments_info = {}
        self.pending_shipments =[]
        self.load()
        self.od_sv = OrderService()
        self.iv_sv = InventoryService()
        self.get_pending_shipments()

    def load(self):
        try:
            with open(self.FILENAME, 'rb') as fin:
                self.shipments_info = pickle.load(fin)
        except FileNotFoundError:
            return None

    def save(self):
        with open(self.FILENAME, 'wb') as fout:
            pickle.dump(self.shipments_info, fout)

    def create_shipment(self, od_id):
        with open(self.COUNTER_FILE, 'r+') as file:
            id_counter = int(file.read().strip()) + 1
            id_counter = str(id_counter)
            file.seek(0)
            file.write(id_counter)
        shipping_status = 1
        self.shipments_info[id_counter] = Shipment(id_counter, od_id, shipping_status)
        self.save()
        order_item = self.od_sv.order_info[od_id].order_item
        for it_id in order_item:
            self.iv_sv.reduce_num_for_ship(it_id, order_item[it_id])
        self.od_sv.ready_to_ship(od_id)

    def show_all_shipments(self):
        for ship_id in self.shipments_info:
            print('************************************************************************')
            print(self.shipments_info[ship_id])
            self.od_sv.print_order(self.shipments_info[ship_id].od_id)
            print('************************************************************************')

    def get_pending_shipments(self):
        for sh_id in self.shipments_info:
            if self.shipments_info[sh_id].shipping_status == 1:
                self.pending_shipments.append(sh_id)

    def show_pending_shipments(self):
        for sh_id in self.pending_shipments:
            print('************************************************************************')
            print(self.shipments_info[sh_id])
            self.od_sv.print_order(self.shipments_info[sh_id].od_id)
            print('************************************************************************')

    def set_to_finish(self, sh_id):
        if sh_id in self.pending_shipments:
            od_id= self.shipments_info[sh_id].od_id
            self.shipments_info[sh_id].shipping_status = 2
            self.shipments_info[sh_id].delivered_time = datetime.now()
            self.save()
            self.od_sv.order_info[od_id].shipping_status = 2
            self.od_sv.save()
        else:
            raise Exception('Invalid shipment ID.')

    def set_all_finish(self):
        if self.pending_shipments:
            for sh_id in self.pending_shipments:
                od_id = self.shipments_info[sh_id].od_id
                self.shipments_info[sh_id].shipping_status = 2
                self.shipments_info[sh_id].delivered_time = datetime.now()
                self.od_sv.order_info[od_id].shipping_status = 2
            self.save()
            self.od_sv.save()
        else:
            raise Exception('There is no shipment needs to finish.')


if __name__ == '__main__':
    sh_sv = ShippingService()
    # sh_sv.create_shipment('10001')
    sh_sv.show_all_shipments()
    # sh_sv.show_pending_shipments()
    # sh_sv.set_to_finish('10001')
    # sh_sv.set_all_finish()
