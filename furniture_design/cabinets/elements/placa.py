
class Placa:
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

    # def draw_placa(self, file_name, ox, oy, oz):
    #     export_stl(file_name, self.label, self.length, self.width, self.thick, ox, oy, oz)

    def get_m2(self):
        return self.length * self.width / 1000000

    def print_placa(self):
        print(f"{self.label}, [{self.length} x {self.width} x {self.thick}], {self.type}, {self.material}")

class PlacaPal(Placa):

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
            return cant_length[0][1] / 1000
        elif cant_type == "2":
            return cant_length[1][1] / 1000
        else:
            raise Exception("ERROR: Unknown cant type!")


class Front(Placa):
    def __init__(self, label, length, width, thick):
        super().__init__(label, length, width, thick)
        self.type = "front"
        self.material = ""


class Pfl(Placa):
    def __init__(self, label, length, width):
        super().__init__(label, length, width, 4)
        self.type = "pfl"
        self.material = ""
        # with open('price_list.csv') as price_list_file:
        #     price_reader = csv.DictReader(price_list_file, delimiter=',')
        #     found = False
        #     for row in price_reader:
        #         if row["Item"] == self.type and row["Material"] == self.material:
        #             found = True
        #             self.price = float(row["Price"]) / (2.8 * 2.07) * (self.length * self.width / 1000000)
        #             # TODO de folosit pretul pe m2 nu pe coala
        #     if not found:
        #         raise NameError("ERROR: Price for " + self.material + " not found. Setting to 0 RON.")


class Blat(Placa):
    def __init__(self, label, length, width, thick):
        super().__init__(label, length, width, thick)
        self.type = "blat"
        self.material = ""
        # with open('price_list.csv') as price_list_file:
        #     price_reader = csv.DictReader(price_list_file, delimiter=',')
        #     found = False
        #     for row in price_reader:
        #         if row["Item"] == self.material:
        #             found = True
        #             self.price = float(row["Price"]) * length / 1000
        #     if not found:
        #         raise NameError("ERROR: Price for " + self.material + " not found. Setting to 0 RON.")
