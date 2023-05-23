from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, SN, color, brand, plate_no, door, passenger, price, owner):
        super().__init__(SN, color, brand, plate_no)
        self.door = door
        self.passenger = passenger
        self.price = price
        self.owner = owner

    def getDoorPass(self):
        return f'{self.door} - {self.price}'

    def getPrice(self):
        return f'{self.price}'
