from furniture_design.order import Order
from furniture_design.cabinets.Kitchen.kitchen import *
from furniture_design.cabinets.Dressing.dressing import *
from furniture_design.cabinets.elements.board import *
from furniture_design.cabinets.elements.accessory import *
from manufacturing.generate_files import generate_manufacturing_files
import os

order_data = {
    "client": "Test",
    "Client Proficut": "Bogdan Urs",
    "Tel Proficut": "0740472185",
    "Transport": "Da",
    "Adresa": "Mosnita Veche, str. Borsa, Nr. 38",
    "h_bucatarie": 2070,
    "h_faianta_top": 1470,
    "h_faianta_base": 900,
    "depth_base": 500,
    "top_height": 600,
    "top_height_2": 400,
    "top_depth": 600,
    "top_depth_2": 500,
    "blat_height": 850,
    "cuptor_height": 595,
    "MsV_height_min": 815,
    "MsV_height_max": 875,
    "material_pal": "Alb W962ST2",
    "material_front": "Alb Riflat A356R3",
    "material_blat": "Stejar Halifax 600",
    "material_pfl": "Alb",
    "h_rate": 110,
    "discount": 0,
    "nr_electrocasnice": 1,
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
    "cant_general": 1,
    "cant_pol": 2,
    "cant_separator": 1,
    "pol_depth": 20
}

order = Order(order_data)

c1 = BaseBox("C1", 900, 600, 500, rules)
c1.remove_all_pfl()
c1.remove_element("blat", "C1.blat")
# c1.remove_element("pal", "C1.lat")
# c1.remove_element("pal", "C1.jos")
# c1.remove_element("pal", "C1.lat")
# c1.remove_element("pal", "C1.leg1")
# c1.remove_element("pal", "C1.leg2")
order.append(c1)

output_directory = "output"
os.makedirs(output_directory, exist_ok=True)
customer_output_directory = os.path.join(output_directory, str(os.path.basename(__file__)).replace(".py", "_output"))
os.makedirs(customer_output_directory, exist_ok=True)

generate_manufacturing_files(order, customer_output_directory)
