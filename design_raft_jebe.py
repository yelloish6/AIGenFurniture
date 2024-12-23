from furniture_design.order import Order
from furniture_design.cabinets.Kitchen.kitchen import *
from furniture_design.cabinets.Dressing.dressing import *
from furniture_design.cabinets.elements.board import *
from furniture_design.cabinets.elements.accessory import *
from manufacturing.generate_files import generate_manufacturing_files
import os

order_data = {
    "client": "Jeberean Cosmin",
    "Client Proficut": "Bogdan Urs",
    "Tel Proficut": "0740472185",
    "Transport": "Nu",
    "Adresa": "Mosnita Veche, str. Borsa, Nr. 38",
    "h_bucatarie": 2200,
    "h_faianta_top": 1470,
    "h_faianta_base": 900,
    "depth_base": 600,
    "top_height": 492,
    "top_height_2": 400,
    "top_depth": 140,
    "top_depth_2": 500,
    "blat_height": 850,
    "cuptor_height": 595,
    "MsV_height_min": 815,
    "MsV_height_max": 875,
    "material_pal": "Smoke Green K521 SU",
    "material_front": "A34R3",
    "material_blat": "Stejar Alpin Keindl",
    "material_pfl": "Alb",
    "h_rate": 70,
    "discount": 100,
    "nr_electrocasnice": 0,
    "h_proiect": 1
}

rules = {
    "thick_pal": 18,
    "thick_front": 18,
    "thick_blat": 38,
    "height_legs": 50,
    "general_width": 600,
    "width_blat": 600,
    "gap_spate": 50,
    "gap_fata": 50,
    "gap_front": 2,
    "cant_general": 2,
    "cant_pol": 2,
    "cant_separator": 2,
    "pol_depth": 0
}

order = Order(order_data)

r1 = TopBox("R1", order_data["top_height"], order_data["top_height"], order_data["top_depth"], rules)
r1.remove_all_pfl()

int_gap = (order_data["top_height"] - 4 * rules["thick_pal"])/3

r1.add_sep_h(order_data["top_height"]- 2 * rules["thick_pal"], 0, int_gap, rules["cant_separator"], 2)
r1.get_item_by_type_label("pal", "R1.sep.h").__setattr__("label", "R1.sep.h1")
placa1 = r1.get_item_by_type_label("pal", "R1.sep.h1")
placa2 = r1.get_item_by_type_label("pal", "R1.lat1")
r1.assemble_pal(placa1, placa2, "wood_dowel", 6, 2)
r1.assemble_pal(r1.get_item_by_type_label("pal", "R1.sep.h1"),r1.get_item_by_type_label("pal", "R1.lat2"),"wood_dowel", 6, 2)
r1.add_sep_h(order_data["top_height"]- 2 * rules["thick_pal"], 0, 2 * int_gap + rules["thick_pal"], rules["cant_separator"], 2)

r1.add_sep_v(int_gap, rules["thick_pal"] + int_gap, 0, rules["cant_separator"], 4)
r1.add_sep_v(int_gap, 2 * (rules["thick_pal"] + int_gap), 0, rules["cant_separator"], 4)
r1.add_sep_v(int_gap, rules["thick_pal"] + int_gap, rules["thick_pal"] + int_gap, rules["cant_separator"], 4)
r1.add_sep_v(int_gap, 2 * (rules["thick_pal"] + int_gap), rules["thick_pal"] + int_gap, rules["cant_separator"], 4)
r1.add_sep_v(int_gap, rules["thick_pal"] + int_gap, 2 * (rules["thick_pal"] + int_gap), rules["cant_separator"], 4)
r1.add_sep_v(int_gap, 2 * (rules["thick_pal"] + int_gap), 2 * (rules["thick_pal"] + int_gap), rules["cant_separator"], 4)

for i in range(2):
    order.append(r1)

output_directory = "output"
os.makedirs(output_directory, exist_ok=True)
customer_output_directory = os.path.join(output_directory, str(os.path.basename(__file__)).replace(".py", "_output"))
os.makedirs(customer_output_directory, exist_ok=True)

generate_manufacturing_files(order, customer_output_directory)
