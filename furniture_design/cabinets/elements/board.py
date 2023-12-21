import csv
# TODO add a method to cut-out boards, and add the effect in all output files

DEFAULT_SHEET_LENGTH = 2800
DEFAULT_SHEET_WIDTH = 2070
DEFAULT_LOSS = 0.1


class Board:
    def __init__(self, label, length, width, thick):
        """
        :param label: eticheta
        :param length: lungimea
        :param width: latimea
        :param thick: grosimea
        """

        self.label = label
        self.length = length
        self.width = width
        self.thick = thick
        self.obs = ""
        self.position = [self.length,  # dim x
                         self.width,  # dim y
                         self.thick,  # dim z
                         0,  # offset x
                         0,  # offset y
                         0]  # offset z
        self.type = ""  # pal, pfl, front
        self.material = ""
        self.price = 0

    def add_obs(self, text):
        """
        append text to obs attribute
        :param text: string to be appended
        :return: n/a
        """
        self.obs = self.obs + text

    def set_material(self, material):
        self.material = material

    def rotate(self, axis):
        """
        rotate the plank by 90 deg on the specified axis. dimensions are re-set to match the rotated position
        :param axis: axis to rotate around
        :return: n/a
        """
        # axis = "x"/"y"/"z"
        init_x = self.position[0]
        init_y = self.position[1]
        init_z = self.position[2]
        if axis == "x":
            self.position[0] = init_x
            self.position[1] = -init_z
            self.position[2] = init_y
        elif axis == "y":
            self.position[0] = -init_z
            self.position[1] = init_y
            self.position[2] = init_x
        elif axis == "z":
            self.position[0] = init_y
            self.position[1] = -init_x
            self.position[2] = init_z
        else:
            self.position[0] = init_x
            self.position[1] = init_y
            self.position[2] = init_z

    def move(self, axis, offset):
        """
        move a plank on a specified axis, by a specified amount
        :param axis: axis to move on
        :param offset: amount to move by
        :return: n/a
        """
        if axis == "x":
            self.position[3] = self.position[3] + int(offset)
        if axis == "y":
            self.position[4] = self.position[4] + int(offset)
        if axis == "z":
            self.position[5] = self.position[5] + int(offset)

    def get_m2(self):
        return float(self.length * self.width / 1000000)

    def print(self):
        print(f"Board type {self.type}, {self.label}, [{self.length} x {self.width} x {self.thick}], {self.material}")

    def get_price_for_item(self, item_type, material):
        """
        this method searches the price_list.csv file for a matching accessory name and returns the matching price.
        :return: price of the accessory
        """
        with open('manufacturing/templates/price_list.csv') as price_list_file:
            price_reader = csv.DictReader(price_list_file, delimiter=',')
            found = False
            for row in price_reader:
                if row["Item"] == item_type and row["Material"] == material:
                    found = True
                    return float(row["Price"])
            if not found:
                print("ERROR: Price for " + item_type + ":" + material + " not found. Setting to 0 RON.")
                return 0

    def get_unit_for_item(self, type, material):
    # TODO wrong implementation of unit management. To be corrected
        """
        this method searches the price_list.csv file for a matching accessory name and returns the matching price.
        :return: price of the accessory
        """
        with open('manufacturing/templates/price_list.csv') as price_list_file:
            price_reader = csv.DictReader(price_list_file, delimiter=',')
            found = False
            for row in price_reader:
                if row["Item"] == type and row["Material"] == material:
                    found = True
                    return row["Unit"]
            if not found:
                print("ERROR: Unit for " + type + ":" + material + " not found.")
                return 0

    def get_price(self):
        """
        this method searches the price_list.csv file for a matching material name and returns the price of the board
        based on it's size in m2
        :return: price of the accessory
        """
        board_size = self.get_m2()
        price = self.get_price_for_item(self.type, self.material)
        unit = self.get_unit_for_item(self.type, self.material)
        if unit == "m2":
            return int(board_size * price)
        elif unit == "m":
            return int(self.length / 1000 * price)
        elif unit == "sheet":
            return int(price / ((DEFAULT_SHEET_LENGTH * DEFAULT_SHEET_WIDTH / 1000000) * (1 - DEFAULT_LOSS)) * board_size)


class BoardPal(Board):

    def __init__(self, label, length, width, thick, cant_L1, cant_L2, cant_l1, cant_l2):
        super().__init__(label, length, width, thick)
        self.cant_list = [cant_L1, cant_L2, cant_l1, cant_l2]
        self.type = "pal"
        self.material = ""

    def get_m_cant(self, cant_type):
        """
        :param cant_type: "0.4" sau "2"
        :return: length of selected cant
        """
        length_cant04 = 0
        length_cant2 = 0
        for i in range(2):
            if self.cant_list[i] == 0.4 or self.cant_list[i] == 1 or self.cant_list[i] == "0.4" or \
                    self.cant_list[i] == "1":
                length_cant04 = length_cant04 + self.length
            if self.cant_list[i] == 2 or self.cant_list[i] == "2":
                length_cant2 = length_cant2 + self.length
            if self.cant_list[i + 2] == 0.4 or self.cant_list[i + 2] == 1 or self.cant_list[i + 2] == "0.4" or \
                    self.cant_list[i + 2] == "1":
                length_cant04 = length_cant04 + self.width
            if self.cant_list[i + 2] == 2 or self.cant_list[i + 2] == "2":
                length_cant2 = length_cant2 + self.width
        cant_length = [['0.4', length_cant04], ['2', length_cant2]]

        if cant_type == "0.4":
            return float(cant_length[0][1] / 1000)
        elif cant_type == "2":
            return float(cant_length[1][1] / 1000)
        else:
            raise Exception("ERROR: Unknown cant type!")

    def get_price(self):
        """
        gets the board price and adds the cant price
        :return:
        """
        price = super().get_price()
        m_cant_1 = self.get_m_cant("0.4")
        price_cant1 = self.get_price_for_item("cant", "0.4")
        m_cant_2 = self.get_m_cant("2")
        price_cant2 = self.get_price_for_item("cant", "2")
        return price + (m_cant_1 * price_cant1) + (m_cant_2 * price_cant2)


class Front(Board):
    def __init__(self, label, length, width, thick):
        super().__init__(label, length, width, thick)
        self.type = "front"
        self.material = ""


class Pfl(Board):
    def __init__(self, label, length, width):
        super().__init__(label, length, width, 4)
        self.type = "pfl"
        self.material = ""


class Blat(Board):
    def __init__(self, label, length, width, thick):
        super().__init__(label, length, width, thick)
        self.type = "blat"
        self.material = ""