import csv

class accesoriu:
    def __init__(self, name, pieces):
        self.name = name
        self.pieces = pieces
        self.type = "accesoriu"
        with open('furniture_design/cabinets/elements/price_list.csv', 'r') as price_list_file:
            price_reader = csv.DictReader(price_list_file, delimiter=',')
            found = False
            for row in price_reader:
                if row["Material"] == self.name:
                    found = True
                    # print(row["Price"])
                    self.price = float(row["Price"])
            if not found:
                print("ERROR: Price for ", self.name, " not found. Setting to 0 RON.")

    def print_accesoriu(self):
        print("Accesoriu: ", self.name, " Pieces:", self.price, " Price: ", self.price)

    def add_pieces(self, number):
        self.pieces = self.pieces + number
