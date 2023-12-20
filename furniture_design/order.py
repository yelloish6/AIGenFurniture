import os
import csv
import math
#import openpyxl
import shutil

PAL_LOSS = 0.1  # used to calculate number of sheets needed


class Order:
    def __init__(self, customer_data):

        self.client = customer_data.get("client")
        self.client_proficut = customer_data.get("Client Proficut")
        self.tel_proficut = customer_data.get("Tel Proficut")
        self.transport = customer_data.get("Transport")
        self.address = customer_data.get("Adresa")
        self.discount = customer_data.get("discount")
        self.h_rate = customer_data.get("h_rate")
        self.nr_electrocasnice = customer_data.get("nr_electrocasnice")
        self.mat_pal = customer_data.get("material_pal")
        self.mat_pfl = customer_data.get("material_pfl")
        self.mat_blat = customer_data.get("material_blat")
        self.mat_front = customer_data.get("material_front")
        self.cabinets_list = []
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

    def append(self, cabinet):
        """
        Set material for all elements from the cabinet based on materials from order if material in the cabinet
        is empty, and append the cabinet to the order.
        :param cabinet:
        :return:
        """
        for element in cabinet.elements_list:
            if element.type == "pal":
                if element.material == "":
                    element.material = self.mat_pal
            elif element.type == "front":
                if element.material == "":
                    element.material = self.mat_front
            elif element.type == "pfl":
                if element.material == "":
                    element.material = self.mat_pfl
            elif element.type == "blat":
                if element.material == "":
                    element.material = self.mat_blat
            elif element.type == "accessory":
                element.material = element.label
        self.cabinets_list.append(cabinet)

    def print(self):
        print(f"[order.py] Printing order:")
        print(f"Customer, {self.client}")
        print(f"Discount, {self.discount}")
        print(f"Material Pal, {self.mat_pal}")
        print(f"Material PFL, {self.mat_pfl}")
        print(f"Material blat, {self.mat_blat}")
        print(f"Material front, {self.mat_front}")
        for corp in self.cabinets_list:
            corp.print()

    def draw(self, ox, oy, oz):
        folder_name = self.create_folder()

        name = os.path.join(folder_name, "3D " + self.client)
        if os.path.exists(name+".stl"):
            os.remove(name+".stl")
        ofset = 0
        for i in range(len(self.corpuri)):
            self.corpuri[i].draw_cabinet(name, ox + ofset, oy, oz)
            ofset = ofset + self.corpuri[i].width + 1

