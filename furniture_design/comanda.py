import os
import csv
import math
#import openpyxl
import shutil

PAL_LOSS = 0.1  # used to calculate number of sheets needed


class Comanda:
    def __init__(self, customer_data):

        self.client = customer_data.get("client")
        self.client_proficut = customer_data.get("Client Proficut")
        self.tel_proficut = customer_data.get("Tel Proficut")
        self.transport = customer_data.get("Transport")
        self.adresa = customer_data.get("Adresa")
        self.discount = customer_data.get("discount")
        self.h_rate = customer_data.get("h_rate")
        self.mat_pal = customer_data.get("material_pal")
        self.mat_pfl = customer_data.get("material_pfl")
        self.mat_blat = customer_data.get("material_blat")
        self.mat_front = customer_data.get("material_front")
        self.designed_cabinets = []
        '''
        self.length = 0
        self.pret_manop = 0
        self.acc = []
        self.m2pal = 0
        self.mat_pal = ""
        self.m2front = 0
        self.frezare = ""
        self.m2pfl = 0
        self.mat_pfl = ""
        self.m_blat = 0
        self.mat_blat = ""
        self.m_cant = [0, 0]
        self.price_pal = 1
        self.price_pfl = 1
        self.price_front = 1
        self.price_blat = 1
        self.price_cant = [0, 0]
        self.price_list = []
        self.cost_pal = 0
        self.cost_pfl = 0
        self.cost_front = 0
        self.cost_blat = 0
        self.cost_cant = [0, 0]
        self.cost_acc = 0
        '''


    def append(self, corp):

        #self.length = self.length + corp.width
        self.designed_cabinets.append(corp)

    def print_comanda(self):
        print(f"[comanda.py] Printing comanda:")
        print(f"Customer, {self.client}")
        print(f"Discount, {self.discount}")
        print(f"Material Pal, {self.mat_pal}")
        print(f"Material PFL, {self.mat_pfl}")
        print(f"Material blat, {self.mat_blat}")
        print(f"Material front, {self.mat_front}")
        for corp in self.designed_cabinets:
            corp.print_corp()


    # def addAcces(self, name, buc):
    #     found = False
    #     for i in range(len(self.acc)):
    #         acc_current = self.acc[i]
    #         if (name == acc_current[2]):
    #             acc_current[3] = acc_current[3] + buc
    #             found = True
    #             index_of_acc = -1
    #             for row in self.price_list:
    #                 if acc_current in row:
    #                     index_of_acc = self.price_list.index(row)
    #             acc_current[4] = acc_current[4] + (float(self.price_list[index_of_acc][1]) * float(self.acc[i][3]))
    #     if not found:
    #         self.acc = self.acc + [["accesoriu", "total", name, buc, 0]]

    # for i in range(len(self.acc)):
    #    acc_to_find = self.acc[i][2]
    #    index_of_acc = -1
    #    for row in self.price_list:
    #        if acc_to_find in row:
    #            index_of_acc = self.price_list.index(row)
    #    self.cost_acc = self.cost_acc + (float(self.price_list[index_of_acc][1]) * float(self.acc[i][3]))

    # def setPrice(self, item, price):
    #     if item == "pal":
    #         self.price_pal = price
    #     elif item == "pfl":
    #         self.price_pfl = price
    #     elif item == "front":
    #         self.price_front = price
    #     else:
    #         self.priceList.append(item, price)

    def get_price_for_item(self, type, material):
        with open('elements/price_list.csv') as price_list_file:
            price_reader = csv.DictReader(price_list_file, delimiter=',')
            found = False
            for row in price_reader:
                if row["Item"] == type and row["Material"] == material:
                    found = True
                    return row["Price"]
            if not found:
                raise NameError("ERROR: Price for " + type + ":" + material + " not found. Setting to 0 RON.")

    def get_min_qty_for_item(self, type, material):
        with open('elements/price_list.csv') as price_list_file:
            price_reader = csv.DictReader(price_list_file, delimiter=',')
            found = False
            for row in price_reader:
                if row["Item"] == type and row["Material"] == material:
                    found = True
                    return row["Minimum"]
            if not found:
                raise NameError("ERROR: Minimum quantity for " + type + " : " + material + " not found. "
                                                                                           "Considering 1 unit")
                return 1

    def create_folder(self):
        # create folder with customer name if it doesn't exist
        folder_name =  "projects/Comanda " + self.client
        isExist = os.path.exists(folder_name)

        if not isExist:
            os.mkdir(folder_name)
        return folder_name


    def export_pal_for_proficut(self):
        #self.create_folder()
        folder_name = self.create_folder()
        shutil.copyfile("templates/Cote-Proficut-2018.xlsx", folder_name + "/Comanda_Proficut_"+self.client+".xlsx")

        file = openpyxl.load_workbook(folder_name + "/Comanda_Proficut_"+self.client+".xlsx")
        sheet = file.get_sheet_by_name("Sheet1")

        sheet['C1'] = self.req["Client Proficut"]
        sheet['D2'] = self.req["Tel Proficut"]
        sheet['D3'] = self.req["Transport"]
        sheet['C4'] = self.req["Adresa"]
        sheet['G4'] = self.req["material_pal"]


        counter = 0
        for corp in self.corpuri:
            for element in corp.material_list:
                if element.type == "pal":
                    sheet['A' + str(10 + counter)] = "1"
                    sheet['B' + str(10 + counter)] = element.length
                    sheet['C' + str(10 + counter)] = element.width
                    sheet['D' + str(10 + counter)] = 0
                    sheet['E' + str(10 + counter)] = element.label
                    sheet['F' + str(10 + counter)] = element.cant_list[0]
                    sheet['G' + str(10 + counter)] = element.cant_list[1]
                    sheet['H' + str(10 + counter)] = element.cant_list[2]
                    sheet['I' + str(10 + counter)] = element.cant_list[3]
                    counter += 1
        file.save(folder_name + "/Comanda_Proficut_"+self.client+".xlsx")

    def export_csv(self):
        # create folder with customer name if it doesn't exist
        folder_name = self.create_folder()

        # output comanda pal
        name = os.path.join(folder_name, "comanda_pal_" + self.client + ".csv")
        corpuri = self.corpuri

        with open(name, mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["Bucati", "Lungime", "Latime", "Orientabila", "Eticheta", "L1", "L2", "l1", "l2"])
            for corp in corpuri:
                for element in corp.material_list:
                    if element.type == "pal":
                        comanda_writer.writerow(
                            [1, element.length, element.width, 0, element.label, element.cant_list[0],
                             element.cant_list[1], element.cant_list[2], element.cant_list[3]])

        # output comanda pfl
        name = os.path.join(folder_name, "comanda_pfl_" + self.client + ".csv")

        with open(name, mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["Bucati", "Lungime", "Latime", "Eticheta"])
            for corp in corpuri:
                for element in corp.material_list:
                    if element.type == "pfl":
                        comanda_writer.writerow([1, element.length, element.width, element.label])

        # output comanda fronturi
        name = os.path.join(folder_name, "comanda_front_" + self.client + ".csv")

        with open(name, mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["Eticheta", "Lungime", "Latime", "Pret"])
            comanda_writer.writerow([self.__getattribute__("frezare")])
            for corp in corpuri:
                for element in corp.material_list:
                    if element.type == "front":
                        comanda_writer.writerow([element.label, element.length, element.width, element.price])

        # output comanda accesorii
        name = os.path.join(folder_name, "comanda_accesorii_" + self.client + ".csv")

        with open(name, mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["Nume", "Bucati", "Pret/buc", "Pret total"])
            # pe corpuri

            totals = []  # totals is a list containing total accessories and their amount and price

            for corp in corpuri:
                for element in corp.material_list:
                    if element.type == "accesoriu":
                        comanda_writer.writerow(
                            [element.name, element.pieces, element.price, element.pieces * element.price])
                        found_in_totals = False
                        for i in range(len(totals)):
                            if totals[i][0] == element.name:
                                totals[i][1] += element.pieces
                                found_in_totals = True
                        if not found_in_totals:
                            totals.append([element.name, element.pieces, element.price])

            # total
            for i in range(len(totals)):
                # print(totals2[i][0], totals2[i][1], totals2[i][2], totals2[i][1] * totals2[i][2])
                comanda_writer.writerow(["TOTAL " + totals[i][0], totals[i][1], totals[i][2], totals[i][1] *
                                         totals[i][2]])

        # output pentru optimizare pal
        name = os.path.join(folder_name, "PannelsCuttingList_pal_" + self.client + ".csv")
        mobila = self.corpuri
        with open(name, mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["Length", "Width", "Qty", "Label", "Enabled"])
            for corp in corpuri:
                for element in corp.material_list:
                    if element.type == "pal":
                        comanda_writer.writerow([element.length, element.width, 1, element.label, "TRUE"])

        # pentru optimizare PFL
        name = os.path.join(folder_name, "PannelsCuttingList_pfl_" + self.client + ".csv")
        mobila = self.corpuri
        with open(name, mode='w', newline="") as comanda_pal:
            comanda_writer = csv.writer(comanda_pal, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            comanda_writer.writerow(["Length", "Width", "Qty", "Enabled"])
            # pe corpuri
            for corp in corpuri:
                for element in corp.material_list:
                    if element.type == "pfl":
                        comanda_writer.writerow([element.length, element.width, 1, element.label, "TRUE"])

    def get_m2_pal(self):
        m2pal = 0
        for i in range(len(self.corpuri)):
            m2pal = m2pal + self.corpuri[i].get_m2_pal()
        return m2pal

    def get_m2_pfl(self):
        m2pfl = 0
        for i in range(len(self.corpuri)):
            m2pfl = m2pfl + self.corpuri[i].get_m2_pfl()
        return m2pfl

    def get_m2_front(self):
        m2 = 0
        for i in range(len(self.corpuri)):
            m2 = m2 + self.corpuri[i].get_m2_front()
        return m2

    def get_m_cant(self, type):
        '''
         :param type: "0.4" sau "2"
         :return: lungimea cantului selectat din toata comanda
         '''

        m = 0
        for i in range(len(self.corpuri)):
            m = m + self.corpuri[i].get_m_cant(type)
        return m

    def get_m_blat(self):
        '''

        :return: metri de blat din comanda
        '''

        m = 0
        for i in range(len(self.corpuri)):
            for j in range(len(self.corpuri[i].material_list)):
                if self.corpuri[i].material_list[j].type == "blat":
                    m = m + self.corpuri[i].material_list[j].length / 1000
        return m

    def draw(self, ox, oy, oz):
        folder_name = self.create_folder()

        name = os.path.join(folder_name, "3D " + self.client)
        if os.path.exists(name+".stl"):
            os.remove(name+".stl")
        ofset = 0
        for i in range(len(self.corpuri)):
            self.corpuri[i].drawCorp(name, ox + ofset, oy, oz)
            ofset = ofset + self.corpuri[i].width + 1

    def get_cost_manopera(self):
        '''
        - 8h proictare
        - 2h per corp asamblare, pozitionare si montaj fronturi
        - 2h montaj / electrocasnic
        - 0.5h pe metru de blat, montaj blat
        :return: [pret manopera, pret manopera cu discount]
        '''

        discount = self.req["discount"]
        h_rate = self.req["h_rate"]
        electrocasnice = self.req["nr_electrocasnice"]
        pret_manop = math.ceil((8 + (len(self.corpuri) * 2) + electrocasnice * 2 + self.get_m_blat() * 0.5)) * h_rate
        pret_manop_discount = pret_manop * (100 - discount) / 100
        return [pret_manop, pret_manop_discount]

    def get_sheets_pal(self):
        m2_pal = self.get_m2_pal() * (1 + PAL_LOSS)
        min = float(self.get_min_qty_for_item("pal", self.req["material_pal"])) * (2800 * 2070 / 1000000)
        sheets = math.ceil(m2_pal / (2800 * 2070 / 1000000))
        return sheets
        # if m2_pal < min:
        #     return min
        # else:
        #     return sheets

    def get_cost_pal(self):
        pal_price = float(self.get_price_for_item("pal", self.mat_pal))
        return self.get_sheets_pal() * pal_price

    def print_status(self):

        cant_price_04 = float(self.get_price_for_item("cant", "0.4"))
        cant_price_2 = float(self.get_price_for_item("cant", "2"))
        pfl_price = float(self.get_price_for_item("pfl", self.mat_pfl))
        front_price = float(self.get_price_for_item("front", self.mat_front))
        blat_price = float(self.get_price_for_item("blat", self.mat_blat))
        for i in range(len(self.corpuri)):
            for j in range(len(self.corpuri[i].material_list)):
                if self.corpuri[i].material_list[j].type == "accesoriu":
                    acc_price = float(self.get_price_for_item(self.corpuri[i].material_list[j].type,
                                                              self.corpuri[i].material_list[j].name))
                    self.cost_acc += acc_price * self.corpuri[i].material_list[j].pieces

        print("*** INFORMATII GENERALE ***")
        print("Nume client: ", self.req["client"])
        print("Numar de corpuri: ", len(self.corpuri))
        print("Lungime totala mobila: ", self.length / 1000, " m")
        print("M2 PAL: ", "{:.2f}".format(self.get_m2_pal()),
              " | Nr. coli PAL: ", self.get_sheets_pal(),
              " | Cost pal:", self.get_cost_pal(),
              " | Material:", self.mat_pal)
        print("M Cant 0.4", math.ceil(self.get_m_cant("0.4")),
              " | Pret ", "{:.2f}".format(math.ceil(self.get_m_cant("0.4")) * cant_price_04))
        print("M Cant 2", math.ceil(self.get_m_cant("2")),
              " | Pret ", "{:.2f}".format(math.ceil(self.get_m_cant("2")) * cant_price_2))

        print("M2 PFL: ", "{:.2f}".format(self.get_m2_pfl()),
              " | Nr. coli PFL: ", math.ceil(self.get_m2_pfl() / (2800 * 2070 / 1000000)),
              " | Pret PFL: ", math.ceil(self.get_m2_pfl() / (2800 * 2070 / 1000000)) * pfl_price)

        print("M2 Front: ", "{:.2f}".format(self.get_m2_front()),
              " | Pret ", "{:.2f}".format(self.get_m2_front() * front_price),
              " | Material: ", "NETT FRONT" , self.mat_front)

        print("M Blat: ", "{:.2f}".format(self.get_m_blat()),
              " | Pret", self.get_m_blat() * blat_price)

        print("Cost total accesorii: ", round(self.cost_acc))

        if self.req["discount"] == 0:
            print("Pret manopera:", self.get_cost_manopera()[0])
        else:
            print("Pret manopera:", self.get_cost_manopera()[0],
                  "| Discount[%]:", self.req["discount"],
                  "| Pret manopera cu discount:", self.get_cost_manopera()[1])

        print("Cost TOTAL: ", round(int(self.cost_acc) +
                                    int(self.get_cost_manopera()[1]) +
                                    int(self.get_cost_pal()) +
                                    int(math.ceil(self.get_m2_pfl() / (2800 * 2070 / 1000000)) * pfl_price) +
                                    int(self.get_m2_front() * int(front_price)) +
                                    int(self.get_m_blat() * blat_price) +
                                    int(math.ceil(self.get_m_cant("0.4")) * cant_price_04) +
                                    int(math.ceil(self.get_m_cant("2")) * cant_price_2)))

    def print_m_cant(self):
        """
        for debugging cant length
        :return:
        """
        m1 = 0
        m2 = 0
        for i in range(len(self.corpuri)):
            for j in range(len(self.corpuri[i].material_list)):
                placa = self.corpuri[i].material_list[j]
                if placa.type == "pal":
                    m1 = m1 + placa.get_m_cant("0.4")
                    m2 = m2 + placa.get_m_cant("2")
        print(m1)
        print(m2)