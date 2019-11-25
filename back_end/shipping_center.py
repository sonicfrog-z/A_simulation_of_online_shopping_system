import sys
sys.path.append("..")
from business_service.shipping_service import ShippingService


class ShippingCenter:
    def __init__(self):
        self.sh_sv = ShippingService()

    def show_menu(self):
        print("+-----------------------------+")
        print("| ***Shipments Management**** |")
        print("| 1) Show all shipments       |")
        print("| 2) Show pending shipments   |")
        print("| 3) Finish a shipment        |")
        print("| 4) Make all pending-->finish|")
        print("| q) Exit to home             |")
        print("+-----------------------------+")

    def show_all_shipments(self):
        self.sh_sv.show_all_shipments()

    def show_pending_shipments(self):
        self.sh_sv.show_pending_shipments()

    def set_to_finish(self):
        print('Enter the shipment ID you want to change to finish')
        sh_id = input('Shipment ID: ')
        try:
            self.sh_sv.set_to_finish(sh_id)
            print('Shipment {} is finished.'.format(sh_id))
        except Exception as e:
            print(e)

    def set_all_finish(self):
        try:
            self.sh_sv.set_all_finish()
            print('All shipments are finished.')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    sc = ShippingCenter()
    sc.show_all_shipments()
