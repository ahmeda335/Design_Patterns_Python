from Vechiles import Car, Bike, Truck

class Factory:
    @staticmethod
    def get_vechile(vechile):
        try:
            if vechile == 'car':
                return Car()
            elif vechile == 'bike':
                return Bike()
            elif vechile == 'truck':
                return Truck()
            else:
                return "No vechile found"
        except:
            return "Error happened"
        