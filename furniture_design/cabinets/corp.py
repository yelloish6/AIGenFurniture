from .elements.placa import *
from .elements.accesoriu import *
from manufacturing.export_stl import *
import math
import csv


class Corp:
    def __init__(self, label, height, width, depth, rules):
        """
        collection of boards forming one cabinet
        all items collected in "self.material_list[]"
        :param label: eticheta
        :param height: inaltimea
        :param width: latimea
        :param depth: adancimea
        :param rules: lista de reguli
        """
        self.label = label
        self.height = height
        self.width = width
        self.depth = depth
        self.thick_pal = rules["thick_pal"]
        self.thick_front = rules["thick_front"]
        self.thick_blat = rules["thick_blat"]
        self.width_blat = rules["width_blat"]
        self.cant_lab = rules["cant_general"]
        self.cant = round(rules["cant_general"])
        self.front_gap = float(rules["gap_front"])
        self.material_list = []
        # self.pal = []
        # self.palOO = []
        # self.pfl = []
        # self.pflOO = []
        # self.front = []
        # self.frontOO = []
        # self.blat = 0
        # self.acc = []
        self.sep_space_h = self.height - (2 * self.thick_pal)
        self.sep_space_w = self.width - (2 * self.thick_pal)
        self.sep_max_depth = depth - self.cant
        # self.sep_prev = ""
        # self.arch = []  # matricea de arhitectura care contine elementele corpului orientate si cu offset
        self.position = [0, 0, 0, 0, 0, 0]  # TODO de folosit pozitia corpului
        self.cant_length = [['0.4', 0], ['2', 0]]

    def append(self, obj):
        self.material_list.append(obj)

    def remove_material(self, item_type, label):
        index = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == item_type and self.material_list[i].label == label:
                index = i
        self.material_list.pop(index)

    def remove_all_pfl(self):
        index = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == "pfl":
                index = i
        self.material_list.pop(index)

    def add_pfl(self):
        placa = Pfl(self.label + ".pfl", self.width - 4, self.height - 4)
        placa.rotate("x")
        placa.move("y", self.depth + 1 + 4)
        placa.move("x", 2)
        placa.move("z", 2)
        self.append(placa)
        self.append(accesoriu("surub PFL", 2 * round(self.height / 150) + 2 * round(self.width / 150)))

    def get_item_by_type_label(self, typ, lab):
        """

        :param typ: type of item to be returned
        :param lab: label of item to be returned
        :return: index of item found in material_list vector
        """
        index = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == typ and self.material_list[i].label == lab:
                index = i
        if 'index' in locals():
            return self.material_list.__getitem__(index)
        else:
            raise NameError("ERROR: element ", lab, " of type ", typ, " not found.")

    def add_front(self, split_list, tip):
        """

        :param split_list: [[front1_%height,front1_%width][front2_%height,front2_%width]]
        :param tip: "door" "drawer" "cover"
        :return: none
        """

        h_tot = self.height - self.front_gap
        h_count = 0
        w_count = 0
        w_tot = self.width - self.front_gap
        origin = [self.front_gap, self.front_gap]
        for i in range(len(split_list)):
            split = split_list[i]
            h = int((h_tot * split[0] / 100) - self.front_gap)
            w = int((w_tot * split[1] / 100) - self.front_gap)
            usa = Front(self.label + "_" + str(i + 1), h, w, self.thick_front)
            usa.rotate("x")
            usa.move("x", origin[0])
            usa.move("z", origin[1])
            usa.rotate("y")
            usa.move("x",usa.width)
            if w_count != 100:
                origin[0] += usa.width + int(self.front_gap / 2)
                w_count += split[1]
                if w_count == 100:
                    origin[0] = self.front_gap
                    w_count = 0
                    if h_count != 100:
                        origin[1] += usa.length + int(self.front_gap / 2)
                        h_count += split[0]

            self.append(usa)
            if tip == "door":
                if (h * w) > 280000:
                    self.append(accesoriu("balama aplicata", 3))
                    self.append(accesoriu("amortizor", 2))
                    self.append(accesoriu("surub 3.5x16", 12))
                else:
                    self.append(accesoriu("balama aplicata", 2))
                    self.append(accesoriu("amortizor", 1))
                    self.append(accesoriu("surub 3.5x16", 8))
                self.append(accesoriu("maner", 1))
            elif tip == "cover":
                self.append(accesoriu("surub intre corpuri", math.ceil(h * w / 40000)))
            elif tip == "drawer":
                self.append(accesoriu("maner", 1))

    def add_pol(self, nr, cant):
        """
        adauga polite intr-un corp
        :param nr: numarul politelor de adaugat in corp
        :param cant: tipul de cant 0,4 sau 2 (ca si numar)
        :return: none
        """
        # TODO: adancimea trebe scazuta cu grosimea cantului si inca nu merge corect
        pol_lung = self.width - (2 * self.thick_pal)
        pol_lat = (self.depth - 20)
        for i in range(nr):
            pol = PlacaPal(self.label + ".pol", pol_lung, pol_lat, self.thick_pal, cant, "", "", "")
            pol.move("x", self.thick_pal)
            pol.move("z", round(self.height / (nr + 1)) * (i + 1))
            pol.move("y", 20)
            self.append(pol)
            self.append(accesoriu("bolt polita", 4))
            self.append(accesoriu("surub PFL", 2))

    def add_separator(self, orient, sep_cant):

        sep_cant_thk = round(sep_cant)
        if orient == "h":
            sep_l = self.sep_space_w
            sep_w = self.sep_max_depth
            sep = PlacaPal(self.label + ".sep" + ".h", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")
            # self.addPalObject(sep)
            # self.addPal(self.label + ".sep" + ".h", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")

            self.sep_space_h = round((self.sep_space_h - self.thick_pal) / 2)
            if self.sep_prev == "v" or "":
                self.sep_max_depth = self.sep_max_depth - sep_cant_thk
                self.sep_prev = "h"
            self.addAcces("surub", 4)
            sep.move("x", self.thick_pal)
            sep.move("z", round(self.sep_space_h))
        if orient == "v":
            sep_l = self.sep_space_h
            sep_w = self.sep_max_depth
            sep = PlacaPal(self.label + ".sep" + ".v", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")
            self.addPalObject(sep)

            self.sep_space_w = round((self.sep_space_w - self.thick_pal) / 2)
            # self.addPal(self.label + ".sep" + ".v", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")
            if self.sep_prev == "h" or "":
                self.sep_max_depth = self.sep_max_depth - sep_cant_thk
                self.sep_prev = "v"

            sep.rotate("y")
            sep.move("x", self.thick_pal + round(self.sep_space_w))
            sep.move("z", self.thick_pal)
            self.addAcces("surub", 4)

    def add_wine_shelf(self, goluri, left_right, cant):
        offset_z = round((self.height - ((goluri + 1) * self.thick_pal)) / goluri)
        if left_right == "left":
            self.add_sep_v(self.height - (2 * self.thick_pal), offset_z, 0, cant)
            for x in range(goluri - 1):
                self.add_sep_h(offset_z, 0, (offset_z * (x + 1)) + (self.thick_pal * (x)), cant)
        if left_right == "right":
            self.add_sep_v(self.height - (2 * self.thick_pal), self.width - offset_z - (3 * self.thick_pal), 0, cant)
            for x in range(goluri - 1):
                self.add_sep_h(offset_z, self.width - offset_z - (2 * self.thick_pal),
                               (offset_z * (x + 1)) + (self.thick_pal * x), cant)
        if offset_z < 90:
            print("ERROR: nu incap sticlele de vin in " + self.label)

    def add_sep_v(self, height, offset_x, offset_z, sep_cant):
        """

        :param height:
        :param offset_x:
        :param offset_z:
        :param sep_cant:
        :return:
        """
        sep_l = height
        sep_w = self.depth
        sep = PlacaPal(self.label + ".sep" + ".v", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")
        self.append(sep)
        self.sep_space_w = round((self.sep_space_w - self.thick_pal) / 2)

        sep.rotate("y")
        sep.move("x", self.thick_pal + offset_x)
        sep.move("z", self.thick_pal + offset_z)
        self.append(accesoriu("surub", 4))

    def add_sep_h(self, width, offset_x, offset_z, sep_cant):
        sep_l = width
        sep_w = self.depth
        sep = PlacaPal(self.label + ".sep" + ".h", sep_l, sep_w, self.thick_pal, sep_cant, "", "", "")
        self.append(sep)
        self.sep_space_w = round((self.sep_space_w - self.thick_pal) / 2)

        sep.move("x", self.thick_pal + offset_x)
        sep.move("z", self.thick_pal + offset_z)
        self.append(accesoriu("surub", 4))

    def add_front_lateral_2(self, left_right):
        front = Front(self.label + ".fr_lat", self.height, self.depth, self.thick_front)
        if left_right == "left":
            front.rotate("y")
        elif left_right == "right":
            front.rotate("y")
            front.move("x", self.width)
        self.append(front)

    def add_front_lateral(self):
        self.front = self.front + [["front", self.label + ".lat", self.height, self.depth]]

    def add_front_manual(self, height, width, offset_x, offset_z):
        fr = Front(self.label + ".man", height, width, self.thick_front)
        fr.rotate("x")
        fr.rotate("y")
        fr.move("x", fr.width)
        fr.move("x", self.front_gap)
        fr.move("z", self.front_gap)
        fr.move("x", offset_x)
        fr.move("z", offset_z)
        # fr.move("y", - self.thick_front)
        self.append(fr)

    def add_tandem_box(self, tip):
        fund_label = self.label + ".ser.jos"
        spate_label = self.label + ".ser.sp"
        fund_lung = int(self.width - (2 * self.thick_pal) - (37.5 * 2))
        spate_lung = self.width - 2 * 18 - 87
        fund_lat = self.depth - 20
        if tip == "M":
            spate_lat = 68
        elif tip == "D":
            spate_lat = 183
        fund = PlacaPal(fund_label, fund_lung, fund_lat, 16, "", "", "", "")
        fund.move("x", self.thick_pal + 13)
        fund.move("z", self.thick_pal + 3)
        self.append(fund)

        spate = PlacaPal(spate_label, spate_lung, spate_lat, 16, self.cant_lab, "", "", "")
        spate.rotate("x")
        spate.move("x", self.thick_pal + 20)
        spate.move("y", fund.width)
        self.append(spate)
        self.append(accesoriu("tandembox " + tip, 1))
        self.append(accesoriu("surub 3.5x16", 18))

    def add_sertar(self, sert_h, offset):
        # sertar de tacamuri de 100, sertare adanci de 200

        gap_glisiera = 13
        height_offset = offset
        sert_thick_pal = self.thick_pal
        sert_lat = self.width - (2 * self.thick_pal) - (2 * gap_glisiera)
        sert_depth = self.depth - gap_glisiera

        long1 = PlacaPal(self.label + ".ser.long", sert_depth, sert_h, sert_thick_pal, self.cant_lab, "", "", "")
        long1.rotate("x")
        long1.rotate("z")
        long1.move("x", self.thick_pal + gap_glisiera)
        long1.move("z", height_offset)
        self.addPalObject(long1)

        lat1 = PlacaPal(self.label + ".ser.lat", sert_lat - (2 * sert_thick_pal), sert_h, sert_thick_pal,
                        self.cant_lab, "", "", "")
        lat1.rotate("x")
        lat1.move("x", self.thick_pal + sert_thick_pal + gap_glisiera + 1)
        lat1.move("z", height_offset)
        self.addPalObject(lat1)

        lat2 = PlacaPal(self.label + ".ser.lat", sert_lat - (2 * sert_thick_pal), sert_h, sert_thick_pal,
                        self.cant_lab, "", "", "")
        lat2.rotate("x")
        lat2.move("x", self.thick_pal + sert_thick_pal + gap_glisiera + 1)
        lat2.move("y", long1.length - lat2.thick)
        lat2.move("z", height_offset)
        self.addPalObject(lat2)

        long2 = PlacaPal(self.label + ".ser.long", sert_depth, sert_h, sert_thick_pal, self.cant_lab, "", "", "")
        long2.rotate("x")
        long2.rotate("z")
        long2.move("x", self.thick_pal + lat1.thick + gap_glisiera + lat2.length + 2)
        long2.move("z", height_offset)
        self.addPalObject(long2)

        # self.addPal(self.label + ".ser.lat", sert_lat - (2 * self.thick_pal), sert_h,self.thick_pal, self.cant_lab, "", "", "")
        # self.addPal(self.label + ".ser.lat", sert_lat - (2 * self.thick_pal), sert_h,self.thick_pal, self.cant_lab, "", "", "")
        # self.addPal(self.label + ".ser.long", sert_depth, sert_h, self.thick_pal, self.cant_lab, "", "", "")
        # self.addPal(self.label + ".ser.long", sert_depth, sert_h, self.thick_pal, self.cant_lab, "", "", "")
        self.pfl = self.pfl + [["pfl", self.label + ".ser.pfl", sert_lat - 4, sert_depth - 4]]
        self.addAcces("pereche glisiera " + str(self.depth) + " mm", 1)
        self.addAcces("surub 3.5x16", 12)
        self.addAcces("surub", 8)
        self.addAcces("surub PFL", 2 * round(sert_lat / 100) + 2 * round(sert_depth / 100))

    def get_corp(self):
        return self

    def print_corp(self):
        print(f"[corp.py] Printing corp:")
        print(f"Label: {self.label}")
        print(f"Dimensions: height {self.height}, width {self.width}, depth {self.depth}")
        print(f"Materials list:")
        for material in self.material_list:
            if material.type == "accesoriu":
                material.print_accesoriu()
            elif material.type == "pal" or "blat" or "front":
                material.print_placa()

    def get_m2_pal(self):

        m2pal = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == "pal":
                m2pal = m2pal + self.material_list[i].get_m2()
        return m2pal

    def get_m2_pfl(self):

        m2pfl = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == "pfl":
                m2pfl = m2pfl + self.material_list[i].get_m2()
        return m2pfl

    def get_m2_front(self):

        m2 = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == "front":
                m2 = m2 + self.material_list[i].get_m2()
        return m2

    def get_m_cant(self, type):
        '''
        :param type: "0.4" sau "2"
        :return: lungimea cantului selectat din tot corpul
        '''
        m = 0
        for i in range(len(self.material_list)):
            if self.material_list[i].type == "pal":
                m = m + self.material_list[i].get_m_cant(type)
        return m

    def rotate_corp(self, axis):
        for i in range(len(self.material_list)):
            if isinstance(self.material_list[i], Placa):
                self.material_list[i].rotate(axis)
                initial_position = self.material_list[i].__getattribute__("position")
                final_position = initial_position
                offset_x = initial_position[3]
                offset_y = initial_position[4]
                offset_z = initial_position[5]
                if axis == "x":
                    final_position[3] = offset_x
                    final_position[4] = -offset_z
                    final_position[5] = offset_y
                elif axis == "y":
                    final_position[3] = -offset_z
                    final_position[4] = offset_y
                    final_position[5] = offset_x
                elif axis == "z":
                    final_position[3] = offset_y
                    final_position[4] = -offset_x
                    final_position[5] = offset_z
                self.material_list[i].position = final_position

    def move_corp(self, axis, offset):
        for i in range(len(self.material_list)):
            if isinstance(self.material_list[i], Placa):
                self.material_list[i].move(axis,offset)

    def display_summary(self):
        print("Cabinet Summary:")
        print(f"Height: {self.height}")
        print(f"Width: {self.width}")
        print(f"depth: {self.depth}")
        #print(f"Additional Features: {', '.join(self.additional_features)}")