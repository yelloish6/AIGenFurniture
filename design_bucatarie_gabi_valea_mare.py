from furniture_design.order import Order
from furniture_design.cabinets.Kitchen.kitchen import *
from furniture_design.cabinets.Dressing.dressing import *
from furniture_design.cabinets.elements.board import *
from furniture_design.cabinets.elements.accessory import *
from manufacturing.generate_files import generate_manufacturing_files
import os

order_data = {
    "client": "Gabi Valea Mare",
    "Client Proficut": "Bogdan Urs",
    "Tel Proficut": "0740472185",
    "Transport": "Da",
    "Adresa": "Mosnita Veche, str. Borsa, Nr. 38",
    "h_bucatarie": 2200,
    "h_faianta_top": 1470,
    "h_faianta_base": 900,
    "depth_base": 600,
    "top_height": 600,
    "top_height_2": 400,
    "top_depth": 600,
    "top_depth_2": 500,
    "blat_height": 850,
    "cuptor_height": 595,
    "MsV_height_min": 815,
    "MsV_height_max": 875,
    "material_pal": "Alb W962ST2",
    "material_front": "A34R3",
    "material_blat": "Stejar Alpin Keindl",
    "material_pfl": "Alb",
    "h_rate": 70,
    "discount": 100,
    "nr_electrocasnice": 3,
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

c1 = BaseBox("C1", 860, 900, 600, rules)
c1.add_pol(1, 2)
c1.add_front([[100, 50],[100, 50]], "door")
c1.append(Blat("blat1", 1800, 600, 38))
order.append(c1)

c2 = BaseBox("C2", 860, 900, 600, rules)
c2.add_pol(1, 2)
c2.add_front([[100, 50],[100, 50]], "door")
order.append(c2)

c3 = BaseBox("C3", 860, 800, 600, rules)
c3.add_pol(1, 2)
c3.add_front([[100, 50],[100, 50]], "door")
c1.append(Blat("blat1", 1400, 600, 38))
order.append(c3)

c4 = BaseBox("C4", 860, 600, 600, rules)
c3.add_drawer_a_pfl(200, 20)
c3.add_drawer_a_pfl(200, 300)
c3.add_drawer_a_pfl(100, 600)
c3.add_front([[40, 100], [40, 100], [20, 100]], "drawer")
order.append(c4)

c5 = TopBox("C5", 600, 900, 400, rules)
c5.add_pol(1,2)
c5.add_front([[100, 50], [100, 50]],"door")
order.append(c5)

c6 = TopBox("c6", 600, 800, 400, rules)
c6.add_pol(1,2)
c6.add_front([[100, 50], [100, 50]],"door")
order.append(c6)

c7 = TopBox("c7", 600, 600, 400, rules)
c7.add_pol(1,2)
c7.add_front([[100, 50], [100, 50]],"door")
order.append(c7)

output_directory = "output"
os.makedirs(output_directory, exist_ok=True)
customer_output_directory = os.path.join(output_directory, str(os.path.basename(__file__)).replace(".py", "_output"))
os.makedirs(customer_output_directory, exist_ok=True)

generate_manufacturing_files(order, customer_output_directory)
