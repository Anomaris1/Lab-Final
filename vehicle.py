class Vehicle:
    def __init__(self, SN, color, brand, plate_no):
        self.SN = SN
        self.color = color
        self.brand = brand
        self.plate_no = plate_no

    def getBrandColor(self):
        return f'{self.brand} - {self.color}'

    def getPlateNo(self):
        return f'{self.plate_no}'
